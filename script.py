import os
import random
from datetime import datetime
import subprocess

# Config
REPO_PATH = os.path.expanduser(".")  # GitHub Actions runs in repo root
FILENAME = "commits.txt"

def append_line(commit_no):
    file_path = os.path.join(REPO_PATH, FILENAME)
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S IST")
    line = f"Commit {commit_no} made automatically on {now}\n"
    with open(file_path, "a") as file:
        file.write(line)
    # Stage the file after writing
    subprocess.run(["git", "add", FILENAME], check=True)

def git_commit(commit_no):
    commit_msg = f"Auto commit #{commit_no} on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} IST"
    subprocess.run(["git", "commit", "-m", commit_msg], check=True)

def make_daily_commits():
    commit_count = random.randint(2, 20)
    print(f"Making {commit_count} commits...")

    # Add daily header once
    file_path = os.path.join(REPO_PATH, FILENAME)
    today = datetime.now().strftime("%Y-%m-%d")
    with open(file_path, "a") as file:
        file.write(f"\n=== {today} ===\n")

    subprocess.run(["git", "add", FILENAME], check=True)
    subprocess.run(["git", "commit", "-m", f"Log header for {today}"], check=True)

    for i in range(1, commit_count + 1):
        try:
            append_line(i)
            git_commit(i)
            print(f"Commit {i} successful!")
        except subprocess.CalledProcessError as e:
            print(f"Git error during commit {i}: {e}")
            continue

    try:
        subprocess.run(["git", "push", "origin", "main"], check=True)
        print("All commits pushed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Git push failed: {e}")

def main():
    make_daily_commits()

if __name__ == "__main__":
    main()
