# 📈 GitHub Stock Market Auto Commit Logger

Automatically log daily stock market snapshots and calculate simulated profits — fully automated using Python and Git!

This project fetches real stock data using Yahoo Finance, commits multiple daily snapshots to your repository, and tracks the simulated profit/loss of a 1-share-per-stock strategy — all without lifting a finger.

---

## ✨ Features

- ✅ Uses **real-time stock prices** via `yfinance`
- ✅ Logs **2–35 stocks per snapshot**, and **2–35 snapshots per day**
- ✅ Calculates **daily simulated portfolio profit/loss**
- ✅ Auto-commits results to `market_log.txt` and `profit_log.txt`
- ✅ Perfect for automation practice, GitHub streaks, and financial journaling

---

## 🧠 How It Works

Every day at **8:00 AM IST**:

1. `script.py` fetches **yesterday’s closing prices** for a random set of stocks  
2. Logs **2–35 snapshots** per day, each with **2–35 randomly selected stocks**  
3. `calculate_profit.py` compares with the previous day’s data  
4. Computes total **simulated portfolio value** and **profit/loss**
5. All logs are committed automatically to your GitHub repo

---

## 📂 Project Structure

```
your-repo/
├── market_log.txt         # Stores daily stock snapshots
├── profit_log.txt         # Stores daily profit/loss summaries
├── script.py              # Logs daily stock data
├── calculate_profit.py    # Calculates portfolio value & profit/loss
└── README.md              # This file
```

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

### 2. Install requirements

```bash
pip install yfinance
```

### 3. Run manually (optional)

You can test the functionality manually before automating:

```bash
python3 script.py
python3 calculate_profit.py
```

---

## 📊 Simulated Strategy

- You are assumed to "hold" **1 share of each stock** logged the previous day  
- Each day's **profit** is based on the price difference from the day before  
- Results are tracked in `profit_log.txt`

---

## 🧪 Example Output

### `market_log.txt`

```
=== Market Log: 2025-05-01 ===
[2025-05-01 08:00:01] Market Data #1 (27 stocks):
  AAPL: $211.21
  TSLA: $292.03
  ...
```

### `profit_log.txt`

```
=== Profit Log: 2025-05-01 ===
Total Value: $5932.17
Total Profit/Loss: +$187.29
Breakdown:
  AAPL: Prev=$209.00 → Yest=$211.21 | Δ +$2.21
  TSLA: Prev=$289.50 → Yest=$292.03 | Δ +$2.53
  ...
```

---

## 🔧 Tips

- To ensure profit tracking starts correctly, pre-fill `market_log.txt` with at least one day of valid stock data.
- You can manually run `script.py` once to generate initial logs.

---

## 📜 License

MIT License — Free to use, fork, and modify.

---

## ✨ Author

**👨‍💻 Abizer Masavi**  
Made for automation nerds, data tinkerers, and GitHub streakers 📊🚀
