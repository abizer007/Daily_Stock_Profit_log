import os
import re
from datetime import datetime, timedelta
import subprocess

REPO_PATH = os.path.expanduser(".")
LOG_FILE = "market_log.txt"
PROFIT_LOG_FILE = "profit_log.txt"

def extract_prices_from_log(date_str):
    """Extract stock prices for a specific date."""
    filepath = os.path.join(REPO_PATH, LOG_FILE)
    if not os.path.exists(filepath):
        return {}

    with open(filepath, "r") as file:
        content = file.read()

    section_pattern = rf"=== Market Log: {date_str} ===\n(.*?)(?=\n===|\Z)"
    match = re.search(section_pattern, content, re.DOTALL)
    if not match:
        return {}

    section = match.group(1)
    price_pattern = r"\s+([A-Z]+): \$([0-9]+\.[0-9]+)"
    return {symbol: float(price) for symbol, price in re.findall(price_pattern, section)}

def write_profit_log(date_str, total_value, total_profit, breakdown):
    filepath = os.path.join(REPO_PATH, PROFIT_LOG_FILE)
    with open(filepath, "a") as file:
        file.write(f"\n=== Profit Log: {date_str} ===\n")
        file.write(f"Total Value: ${total_value:.2f}\n")
        file.write(f"Total Profit/Loss: ${total_profit:+.2f}\n")
        file.write("Breakdown:\n")
        for line in breakdown:
            file.write(f"  {line}\n")
        file.write("\n")

def commit_profit_log(date_str):
    subprocess.run(["git", "add", PROFIT_LOG_FILE], check=True)
    subprocess.run(["git", "commit", "-m", f"Profit log for {date_str}"], check=True)
    subprocess.run(["git", "push", "origin", "main"], check=True)

def main():
    today = datetime.now()
    yest = (today - timedelta(days=1)).strftime("%Y-%m-%d")
    prev = (today - timedelta(days=2)).strftime("%Y-%m-%d")

    yest_prices = extract_prices_from_log(yest)
    prev_prices = extract_prices_from_log(prev)

    total_value = 0
    total_profit = 0
    breakdown = []

    for symbol, y_price in yest_prices.items():
        p_price = prev_prices.get(symbol)
        if p_price is None:
            continue  # Skip if no price for day-before

        change = y_price - p_price
        total_value += y_price
        total_profit += change
        breakdown.append(f"{symbol}: Prev=${p_price:.2f} → Yest=${y_price:.2f} | Δ ${change:+.2f}")

    if breakdown:
        write_profit_log(yest, total_value, total_profit, breakdown)
        commit_profit_log(yest)
        print(f"✅ Profit log for {yest} committed.")
    else:
        print(f"⚠️ No matching stock data found between {prev} and {yest}.")

if __name__ == "__main__":
    main()
