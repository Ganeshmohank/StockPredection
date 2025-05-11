STRATEGY_MAP = {
    "index": [
        "VTI", "VOO", "IXUS", "ITOT", "ILTB"
    ],
    "ethical": [
        "AAPL", "ADBE", "TSLA", "NSRGY", "MSFT"
    ],
    "growth": [
        "TSLA", "NVDA", "AMZN", "META", "SHOP"
    ],
    "value": [
        "BMY", "CVX", "KO", "WFC", "PFE"
    ],
    "quality": [
        "MSFT", "JNJ", "AAPL", "V", "HD"
    ],
    "dividend": [
        "VYM", "T", "PG", "PEP", "XOM"
    ],
    "technology": [
        "AAPL", "NVDA", "MSFT", "AMD", "CRM"
    ]
}

TICKER_META = {
    "VTI": {"type": "ETF", "sector": "Index", "description": "Vanguard Total US Market"},
    "VOO": {"type": "ETF", "sector": "Index", "description": "S&P 500 Index"},
    "IXUS": {"type": "ETF", "sector": "International", "description": "iShares Core MSCI Total Intl Stock"},
    "ITOT": {"type": "ETF", "sector": "Index", "description": "iShares Core S&P Total US Stock Market"},
    "ILTB": {"type": "ETF", "sector": "Bonds", "description": "iShares 10+ Year Treasury Bond"},
    "AAPL": {"type": "Stock", "sector": "Technology", "description": "Apple Inc."},
    "ADBE": {"type": "Stock", "sector": "Technology", "description": "Adobe Inc."},
    "TSLA": {"type": "Stock", "sector": "Automotive", "description": "Tesla, Inc."},
    "NSRGY": {"type": "Stock", "sector": "Consumer", "description": "Nestlé S.A."},
    "MSFT": {"type": "Stock", "sector": "Technology", "description": "Microsoft Corporation"},
    "NVDA": {"type": "Stock", "sector": "Technology", "description": "NVIDIA Corporation"},
    "AMZN": {"type": "Stock", "sector": "E-Commerce", "description": "Amazon.com, Inc."},
    "META": {"type": "Stock", "sector": "Social Media", "description": "Meta Platforms, Inc."},
    "SHOP": {"type": "Stock", "sector": "E-Commerce", "description": "Shopify Inc."},
    "BMY": {"type": "Stock", "sector": "Healthcare", "description": "Bristol-Myers Squibb"},
    "CVX": {"type": "Stock", "sector": "Energy", "description": "Chevron Corporation"},
    "KO": {"type": "Stock", "sector": "Beverages", "description": "The Coca-Cola Company"},
    "WFC": {"type": "Stock", "sector": "Financial", "description": "Wells Fargo & Company"},
    "PFE": {"type": "Stock", "sector": "Healthcare", "description": "Pfizer Inc."},
    "JNJ": {"type": "Stock", "sector": "Healthcare", "description": "Johnson & Johnson"},
    "V": {"type": "Stock", "sector": "Financial", "description": "Visa Inc."},
    "HD": {"type": "Stock", "sector": "Retail", "description": "The Home Depot, Inc."},
    "VYM": {"type": "ETF", "sector": "Dividend", "description": "Vanguard High Dividend Yield ETF"},
    "T": {"type": "Stock", "sector": "Telecom", "description": "AT&T Inc."},
    "PG": {"type": "Stock", "sector": "Consumer", "description": "Procter & Gamble Co."},
    "PEP": {"type": "Stock", "sector": "Beverages", "description": "PepsiCo, Inc."},
    "XOM": {"type": "Stock", "sector": "Energy", "description": "Exxon Mobil Corporation"},
    "AMD": {"type": "Stock", "sector": "Semiconductors", "description": "Advanced Micro Devices, Inc."},
    "CRM": {"type": "Stock", "sector": "Technology", "description": "Salesforce, Inc."}
}
