
# 📊 Stock Portfolio Suggestion Engine

This is a full-stack web application that suggests stock portfolios based on custom investment strategies, real-time stock data, and user-defined weights. Built with **React** (frontend), **FastAPI** (backend), and **yfinance** for stock data, it also uses a local **JSON server** for tracking portfolio history.

---

## 🚀 Features

### ✅ Strategy-Based Portfolio Suggestions
- Choose from **predefined presets**: Conservative, Balanced, Aggressive, Ethical Focus, Tech Heavy
- Adjust individual strategy weights via sliders
- Automatically switches to "Custom" mode when edited

### 📈 Real-Time and Historical Insights
- Fetches **real-time prices** via yfinance
- Computes **5-day trend** using actual stock close prices
- Displays **sector allocation** and **value trend** using Chart.js

### 🧱 Modular and Responsive UI
- Clean, card-based layout with responsive charts
- Sidebar for strategy control
- Pie + Line charts display portfolio stats

---

## 🧩 Tech Stack

| Layer       | Technology       |
|-------------|------------------|
| Frontend    | React (Vite)     |
| Styling     | Pure HTML & CSS  |
| Backend     | FastAPI (Python) |
| Data Source | yfinance API     |
| Database    | JSON Server      |
| Charts      | Chart.js         |

---

## 🛠️ Setup Instructions

### 1. Backend

```bash
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload
```

> `requirements.txt` should include:
> - fastapi
> - uvicorn
> - yfinance
> - requests

### 2. Frontend

```bash
cd frontend
npm install
npm run dev
```

> Default URL: `http://localhost:5173`

### 3. JSON Server (for history)

```bash
npm install -g json-server
json-server --watch db/history.json --port 3001
```

---

## 📁 Project Structure

```
📦 root
├── backend/
│   ├── main.py
│   ├── services/
│   ├── models/
│   └── utils/
├── frontend/
│   ├── App.jsx
│   ├── App.css
│   ├── components/
│   │   ├── PortfolioCard.jsx
│   │   └── StrategySidebar.jsx
├── db/
│   └── history.json
```

---

## 🔍 Screenshots

### 💡 Strategy Selection & Sliders
> Includes presets + real-time editing

### 📊 Responsive Portfolio Cards & Charts
> Sector Allocation + Portfolio Value Trend

---

## ✨ Future Improvements

- Save/load custom strategies to user profile
- Integrate real-time news sentiment per stock
- Add risk-adjusted return scoring
- PDF/CSV export of portfolio

---

## 📬 Contact

For questions or contributions, feel free to reach out via GitHub Issues or pull requests.

---
