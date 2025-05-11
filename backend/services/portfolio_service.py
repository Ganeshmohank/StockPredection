import yfinance as yf
import requests
from datetime import datetime, timedelta
from utils.strategy_mapping import STRATEGY_MAP, TICKER_META

JSON_SERVER_URL = "http://localhost:3001/history"

def get_5_day_avg(ticker):
    try:
        end = datetime.today()
        start = end - timedelta(days=10)
        data = yf.Ticker(ticker).history(start=start, end=end)
        if data.empty or "Close" not in data:
            raise Exception("No close price")
        return list(data["Close"].tail(5).round(2))
    except Exception as e:
        raise ValueError(f"Unable to fetch 5-day price history for {ticker}: {str(e)}")

def generate_portfolio(amount: float, strategies):
    tickers_by_strategy = {}
    for entry in strategies:
        strat_key = entry.name.lower()
        weight = entry.weight
        if strat_key in STRATEGY_MAP:
            tickers_by_strategy[strat_key] = {
                "tickers": STRATEGY_MAP[strat_key],
                "weight": weight
            }

    if not tickers_by_strategy:
        raise ValueError("No valid strategies provided.")

    prices = {}
    for strat_data in tickers_by_strategy.values():
        for ticker in strat_data["tickers"]:
            if ticker not in prices:
                try:
                    data = yf.Ticker(ticker).history(period="1d")
                    prices[ticker] = float(data["Close"].iloc[-1])
                except:
                    raise ValueError(f"Could not get price for {ticker}")

    portfolio = []
    sector_allocations = {}
    total = 0

    for strat, data in tickers_by_strategy.items():
        weight = data["weight"]
        tickers = data["tickers"]
        strat_budget = amount * weight
        per_stock = strat_budget / len(tickers)

        for ticker in tickers:
            price = prices[ticker]
            shares = per_stock / price
            value = shares * price
            meta = TICKER_META.get(ticker, {})
            sector = meta.get("sector", "Unknown")
            sector_allocations[sector] = sector_allocations.get(sector, 0) + value

            portfolio.append({
                "ticker": ticker,
                "price": round(price, 2),
                "shares": round(shares, 2),
                "value": round(value, 2),
                "sector": sector,
                "description": meta.get("description", ""),
                "type": meta.get("type", "Stock"),
                "strategy": strat,
                "trend": get_5_day_avg(ticker)
            })
            total += value

    # Compute total portfolio history over 5 days
    history = [round(sum(stock["trend"][i] for stock in portfolio) / len(portfolio), 2) for i in range(5)]

    # Save to json-server
    payload = {
        "strategies": [entry.name for entry in strategies],
        "portfolio": portfolio,
        "total_value": round(total, 2),
        "history": history,
        "sector_allocations": sector_allocations
    }

    try:
        requests.post(JSON_SERVER_URL, json=payload)
    except:
        pass

    return portfolio, round(total, 2), history, sector_allocations
