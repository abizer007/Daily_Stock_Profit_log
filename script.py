import os
import time
import random
from datetime import datetime
import subprocess

# Config
REPO_PATH = os.path.expanduser("~/Desktop/git-autocommit-script")  # Update this if needed
FILENAME = "commits.txt"

def append_line(commit_no):
    file_path = os.path.join(REPO_PATH, FILENAME)
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S IST")
    line = f"Commit {commit_no} made automatically on {now}\n"
    with open(file_path, "a") as file:
        file.write(line)

def git_commit_push():
    os.chdir(REPO_PATH)
    subprocess.run(["git", "add", "."], check=True)
    commit_msg = f"Auto commit on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} IST"
    subprocess.run(["git", "commit", "-m", commit_msg], check=True)
    subprocess.run(["git", "push", "origin", "main"], check=True)

def make_daily_commits():
    commit_count = random.randint(2, 20)
    print(f"Making {commit_count} commits today...")
    
    for i in range(1, commit_count + 1):
        try:
            append_line(i)
            git_commit_push()
            print(f"Commit {i} successful!")
        except Exception as e:
            print(f"An error occurred during commit {i}: {e}")
        time.sleep(random.randint(60, 300))  # Wait between 1-5 minutes between commits to look natural

def wait_until_midnight():
    while True:
        now = datetime.now()
        if now.hour == 0 and now.minute == 0:
            return
        time.sleep(30)

def main():
    print("Starting Git auto-commit script... Waiting for 12 AM IST each day.")
    while True:
        wait_until_midnight()
        make_daily_commits()
        time.sleep(61)  # Sleep after finishing today's commits

if __name__ == "__main__":
    main()
