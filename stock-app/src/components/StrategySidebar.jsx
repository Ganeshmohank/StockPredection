import React from "react";

export default function StrategySidebar({ weights, strategyInfo, onSliderChange, onSetPreset, currentPreset }) {
  const allPresets = {
    conservative: {
      label: "Conservative",
      weights: { index: 0.4, value: 0.2, dividend: 0.2, quality: 0.2 }
    },
    balanced: {
      label: "Balanced",
      weights: { index: 0.3, growth: 0.2, value: 0.2, quality: 0.2, dividend: 0.1 }
    },
    aggressive: {
      label: "Aggressive",
      weights: { growth: 0.4, technology: 0.3, ethical: 0.15, index: 0.15 }
    },
    techheavy: {
      label: "Tech Heavy",
      weights: { technology: 0.6, growth: 0.2, quality: 0.2 }
    },
    ethicalfirst: {
      label: "Ethical Focus",
      weights: { ethical: 0.5, index: 0.3, dividend: 0.2 }
    }
  };

  return (
    <div className="sidebar">
      <h2>Presets</h2>
      <div className="preset-buttons">
        {Object.entries(allPresets).map(([key, preset]) => (
          <button
            key={key}
            className={currentPreset === key ? "active" : ""}
            onClick={() => onSetPreset(key, preset.weights)}
          >
            {preset.label}
          </button>
        ))}
      </div>

      <h3 style={{ marginTop: "1rem" }}>
        {currentPreset === "custom" ? "Custom Strategy" : "Edit Strategy Weights"}
      </h3>

      <p className="note">Total must not exceed 100%</p>

      {Object.entries(strategyInfo).map(([name, desc]) => (
        <div key={name} className="slider-row">
          <label>
            {name.charAt(0).toUpperCase() + name.slice(1)} - <span>{desc}</span>
          </label>
          <input
            type="range"
            min="0"
            max="1"
            step="0.01"
            value={weights[name] || 0}
            onChange={(e) => onSliderChange(name, parseFloat(e.target.value))}
          />
          <span>{((weights[name] || 0) * 100).toFixed(0)}%</span>
        </div>
      ))}
    </div>
  );
}
