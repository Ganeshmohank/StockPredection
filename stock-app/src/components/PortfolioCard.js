import React from "react";

export default function PortfolioCard({ stock }) {
  return (
    <div className="portfolio-card">
      <div className="card-header">
        <div className="ticker">{stock.ticker}</div>
        <div className="strategy">{stock.strategy}</div>
      </div>
      <div className="card-body">
        <p><strong>Type:</strong> {stock.type} | <strong>Sector:</strong> {stock.sector}</p>
        <p><strong>Shares:</strong> {stock.shares.toFixed(2)}</p>
        <p><strong>Price:</strong> ${stock.price}</p>
        <p><strong>Total:</strong> ${stock.value}</p>
        <p><strong>Trend:</strong> ${stock.trend?.join(" → $")}</p>
        <p className="description">{stock.description}</p>
      </div>
    </div>
  );
}
