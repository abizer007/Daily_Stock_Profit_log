
<h1 align="center">📈 GitHub Stock Market Auto Commit Logger</h1>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.9+-blue?logo=python" />
  <img src="https://img.shields.io/badge/yfinance-enabled-brightgreen" />
  <img src="https://img.shields.io/badge/automation-100%25-orange" />
<p align="center">
  <img src="https://img.shields.io/github/last-commit/abizer007/Daily_Stock_Profit_log" />
  <img src="https://img.shields.io/github/repo-size/abizer007/Daily_Stock_Profit_log" />
</p>

</p>

<p align="center">
  <img src="https://github.com/abizermasavi/stock-auto-logger/assets/visual-diagram.gif" width="70%" alt="Logger Workflow" />
</p>

---

## ✨ Features

🚀 Real stock prices via `yfinance`  
🧠 Logs 2–35 stocks *per snapshot*, and 2–35 *snapshots per day*  
💸 Simulates daily profit/loss of a 1-share-per-stock portfolio  
📁 Auto-commits to `market_log.txt` and `profit_log.txt`  
🎯 Great for GitHub streaks, journaling, and data tinkering  

---

## 🧠 How It Works

📅 At **8:00 AM IST daily**:

> 📥 `script.py` logs **random stocks' closing prices** from yesterday  
> 📊 `calculate_profit.py` checks **profit/loss delta**  
> 🧾 Logs are saved to `.txt` files  
> 💾 All updates are **committed to GitHub**  


---

## 📂 Project Structure

```
your-repo/
├── market_log.txt         # Daily stock snapshots
├── profit_log.txt         # Daily profit/loss summaries
├── script.py              # Logs daily stock data
├── calculate_profit.py    # Calculates portfolio value & profit/loss
└── README.md              # This file
```

---

## 🚀 Getting Started

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
pip install yfinance
python3 script.py
python3 calculate_profit.py
```

---

## 📊 Strategy

You're "holding" **1 share per stock** from the previous day.  
Profit is the **price delta**.  

---

## 📁 Sample Output

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
  AAPL: Prev=$209.00 → $211.21 | Δ +$2.21
  TSLA: Prev=$289.50 → $292.03 | Δ +$2.53
  ...
```

---

## 🛠️ Pro Tips

- Initialize `market_log.txt` with sample data to kick off logging.
- Use GitHub Actions or cron jobs for hands-free logging.
- Tweak frequency, stock list, or timezone in `script.py`.

---

## 📜 License

MIT — Use it, fork it, hack it. Just credit me. 🙌

---

## ✨ Author

**Abizer Masavi**  
Automation nerd. Financial dabbler. GitHub streaker.  
📊🚀 Made with ❤️ and `yfinance`.

<p align="center">
  <img src="https://media.giphy.com/media/L3nWlmE3wTk2k/giphy.gif" width="120px" />
</p>
