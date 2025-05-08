import os
import random
from datetime import datetime
import subprocess
import yfinance as yf

# === Config ===
REPO_PATH = os.path.expanduser(".")
FILENAME = "market_log.txt"

# Expanded list of 35+ popular tickers
STOCKS = [
    "AAPL", "GOOGL", "MSFT", "TSLA", "AMZN", "NFLX", "NVDA", "META", "BABA", "INTC",
    "ORCL", "ADBE", "CSCO", "QCOM", "IBM", "AMD", "CRM", "SHOP", "UBER", "LYFT",
    "PYPL", "BA", "V", "MA", "DIS", "WMT", "T", "KO", "PEP", "JNJ", "PFE", "MRNA",
    "NKE", "SBUX", "XOM"
]

def ensure_log_file():
    file_path = os.path.join(REPO_PATH, FILENAME)
    if not os.path.exists(file_path):
        with open(file_path, "w") as file:
            file.write("📈 Daily Market Snapshot Log (powered by yfinance)\n")
            file.write("This file logs previous day's closing prices of randomly selected stocks.\n\n")

def get_yesterday_prices(symbols):
    prices = {}
    for symbol in symbols:
        try:
            stock = yf.Ticker(symbol)
            hist = stock.history(period="2d")
            if not hist.empty and len(hist) > 1:
                yesterday_close = hist['Close'].iloc[-2]
                prices[symbol] = round(yesterday_close, 2)
            else:
                prices[symbol] = "N/A"
        except Exception as e:
            prices[symbol] = f"Error: {e}"
    return prices

def append_market_data(commit_no):
    file_path = os.path.join(REPO_PATH, FILENAME)
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    stock_count = random.randint(2, 35)
    selected = random.sample(STOCKS, stock_count)
    prices = get_yesterday_prices(selected)

    log_line = f"[{now}] Market Data #{commit_no} ({stock_count} stocks):\n"
    for symbol, price in prices.items():
        log_line += f"  {symbol}: ${price}\n"
    log_line += "\n"

    with open(file_path, "a") as file:
        file.write(log_line)
    subprocess.run(["git", "add", FILENAME], check=True)

def git_commit(commit_no):
    msg = f"Market Snapshot #{commit_no} – {datetime.now().strftime('%H:%M:%S')}"
    subprocess.run(["git", "commit", "-m", msg], check=True)

def set_git_credentials():
    token = os.getenv("GITHUB_TOKEN")
    repo = os.getenv("GITHUB_REPOSITORY")
    if token and repo:
        subprocess.run([
            "git", "remote", "set-url", "origin",
            f"https://x-access-token:{token}@github.com/{repo}.git"
        ], check=True)

def make_daily_snapshots():
    commit_count = random.randint(1, 5)
    print(f"Generating {commit_count} market snapshots...")

    file_path = os.path.join(REPO_PATH, FILENAME)
    today = datetime.now().strftime("%Y-%m-%d")
    with open(file_path, "a") as file:
        file.write(f"\n=== Market Log: {today} ===\n")

    subprocess.run(["git", "add", FILENAME], check=True)
    subprocess.run(["git", "commit", "-m", f"Start market log for {today}"], check=True)

    for i in range(1, commit_count + 1):
        try:
            append_market_data(i)
            git_commit(i)
            print(f"📊 Snapshot {i} committed.")
        except subprocess.CalledProcessError as e:
            print(f"⚠️ Git error at snapshot {i}: {e}")

def main():
    ensure_log_file()
    make_daily_snapshots()
    set_git_credentials()
    try:
        subprocess.run(["git", "push", "origin", "main"], check=True)
        print("✅ All market snapshots pushed.")
    except subprocess.CalledProcessError as e:
        print(f"❌ Push failed: {e}")

if __name__ == "__main__":
    main()

