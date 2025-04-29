import os
import random
from datetime import datetime
import subprocess

# Config
REPO_PATH = os.path.expanduser(".")  # GitHub Actions runs in repo root
FILENAME = "commits.txt"

# Ensure commits.txt exists
def ensure_commits_file():
    file_path = os.path.join(REPO_PATH, FILENAME)
    if not os.path.exists(file_path):
        with open(file_path, "w") as file:
            file.write("Commit Log Started\n\n")

# Append a commit line
def append_line(commit_no):
    file_path = os.path.join(REPO_PATH, FILENAME)
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S IST")
    line = f"Commit {commit_no} made automatically on {now}\n"
    with open(file_path, "a") as file:
        file.write(line)
    subprocess.run(["git", "add", FILENAME], check=True)

# Make a git commit
def git_commit(commit_no):
    commit_msg = f"Auto commit #{commit_no} on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} IST"
    subprocess.run(["git", "commit", "-m", commit_msg], check=True)

# Set Git credentials for pushing using GITHUB_TOKEN
def set_git_credentials():
    token = os.getenv("GITHUB_TOKEN")
    repo = os.getenv("GITHUB_REPOSITORY")
    if token and repo:
        subprocess.run(["git", "remote", "set-url", "origin", f"https://x-access-token:{token}@github.com/{repo}.git"], check=True)

# Main logic to make commits
def make_daily_commits():
    commit_count = random.randint(2, 20)
    print(f"Making {commit_count} commits...")

    # Add daily header
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

def main():
    ensure_commits_file()
    make_daily_commits()
    set_git_credentials()  # Set credentials after commits but before push
    try:
        subprocess.run(["git", "push", "origin", "main"], check=True)
        print("All commits pushed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Git push failed: {e}")

if __name__ == "__main__":
    main()

