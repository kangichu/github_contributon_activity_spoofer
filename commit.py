import datetime
import subprocess
import random

# Set the start date
start_date = datetime.datetime(2022, 1, 1)

# Set the number of commits per day
commits_per_day = 5

# Set the current date
current_date = datetime.datetime.now()

# Calculate the number of days between the start date and the current date
num_days = (current_date - start_date).days

# Calculate the total number of commits
total_commits = num_days * commits_per_day

# Loop through the days and commit the code
for i in range(total_commits):
  # Generate a commit message
  commit_message = f"Commit message  {i+1}"
  a = random.randint(1,365)

  # Add and commit the code
  subprocess.run(["git", "add", "."])
  subprocess.run(["git", "commit", f"--date= {a} day ago", "--allow-empty", "-m", commit_message])

  # Push the code to the repository
  push_command = ["git", "push", "--force-with-lease"]
  push_result = subprocess.run(push_command, stderr=subprocess.PIPE)

  # If the push fails, try again with a force flag
  if push_result.returncode != 0:
    push_command = ["git", "push", "--force"]
    subprocess.run(push_command)
