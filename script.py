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

def git_commit_push(commit_no):
    subprocess.run(["git", "add", "."], check=True)
    commit_msg = f"Auto commit #{commit_no} on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} IST"
    subprocess.run(["git", "commit", "-m", commit_msg], check=True)

def make_daily_commits():
    commit_count = random.randint(2, 20)
    print(f"Making {commit_count} commits...")

    for i in range(1, commit_count + 1):
        try:
            append_line(i)
            git_commit_push(i)
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
