import React, { useState, useEffect } from "react";
import axios from "axios";
import "./App.css";
import { Line, Pie } from "react-chartjs-2";
import {
  Chart, ArcElement, Tooltip, Legend,
  LineElement, CategoryScale, LinearScale, PointElement
} from "chart.js";
import StrategySidebar from "./components/StrategySidebar";
import PortfolioCard from "./components/PortfolioCard";

Chart.register(ArcElement, Tooltip, Legend, LineElement, CategoryScale, LinearScale, PointElement);

const STRATEGY_INFO = {
  index: "Broad market exposure (VTI, VOO)",
  ethical: "Socially responsible companies",
  growth: "High-growth companies (TSLA, AMZN)",
  value: "Undervalued long-term picks",
  quality: "Stable fundamentals",
  dividend: "High dividend yield",
  technology: "Tech sector leaders"
};

export default function App() {
  const [amount, setAmount] = useState(5000);
  const [weights, setWeights] = useState({});
  const [currentPreset, setCurrentPreset] = useState("custom");
  const [result, setResult] = useState(null);
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);

  const handleSliderChange = (strategy, value) => {
    const updated = { ...weights, [strategy]: value };
    setWeights(updated);
    setCurrentPreset("custom");
  };

  const setPreset = (presetKey, presetWeights) => {
    setWeights(presetWeights);
    setCurrentPreset(presetKey);
    setError("");
  };

  const handleSubmit = async () => {
    const selected = Object.entries(weights)
      .filter(([_, w]) => w > 0)
      .map(([name, weight]) => ({ name, weight }));

    if (selected.length === 0) {
      setError("Please select at least one strategy with non-zero weight.");
      return;
    }

    setLoading(true);
    setResult(null);
    setError("");

    try {
      const res = await axios.post("http://localhost:8000/api/portfolio/suggest", {
        amount,
        strategies: selected
      });
      setResult(res.data);
    } catch (e) {
      const detail = e.response?.data?.detail;
      if (Array.isArray(detail)) {
        setError(detail.map(d => d.msg).join(", "));
      } else {
        setError(detail || "Backend error");
      }
    } finally {
      setLoading(false);
    }
  };

  const renderSectorChart = () => {
    const labels = Object.keys(result.sector_allocations);
    const data = Object.values(result.sector_allocations);
    return (
      <Pie
        data={{
          labels,
          datasets: [{
            data,
            backgroundColor: [
              "#4CAF50", "#2196F3", "#FFC107", "#FF5722",
              "#9C27B0", "#00BCD4", "#E91E63", "#8BC34A",
              "#3F51B5", "#F44336", "#009688"
            ]
          }]
        }}
        options={{
          maintainAspectRatio: true,
          aspectRatio: 1.2,
          plugins: { legend: { position: "top" } }
        }}
      />
    );
  };

  const renderHistoryChart = () => {
    return (
      <Line
        data={{
          labels: ["Day 1", "Day 2", "Day 3", "Day 4", "Day 5"],
          datasets: [{
            label: "Total Portfolio Value",
            data: result.history,
            borderColor: "#4CAF50",
            tension: 0.3,
            fill: false
          }]
        }}
        options={{
          maintainAspectRatio: true,
          responsive: true
        }}
      />
    );
  };

  return (
    <div className="app">
      <h1>Stock Portfolio Suggestion Engine</h1>

      <div className="strategy-layout">
        <StrategySidebar
          weights={weights}
          strategyInfo={STRATEGY_INFO}
          onSliderChange={handleSliderChange}
          onSetPreset={setPreset}
          currentPreset={currentPreset}
        />

        <div className="main-panel">
          <label>Investment Amount ($)</label>
          <input type="number" value={amount} min={5000} onChange={(e) => setAmount(Number(e.target.value))} />

          <button onClick={handleSubmit} disabled={loading}>
            {loading ? "Analyzing..." : "Get Portfolio"}
          </button>

          {error && <p className="error">{error}</p>}
          {loading && <div className="loading"><div className="spinner" />Analyzing...</div>}

          {result && (
            <div className="results">
              <h2>Suggested Portfolio</h2>
              <div className="portfolio-grid">
                {result.portfolio.map(stock => (
                  <PortfolioCard key={stock.ticker} stock={stock} />
                ))}
              </div>

              <div className="chart-container">
                <div className="chart-box">
                  <h3>Sector Allocation</h3>
                  {renderSectorChart()}
                </div>
                <div className="chart-box">
                  <h3>5-Day Portfolio Trend</h3>
                  {renderHistoryChart()}
                </div>
              </div>
            </div>
          )}
        </div>
      </div>
    </div>
  );
}
