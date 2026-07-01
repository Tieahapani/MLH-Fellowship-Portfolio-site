#!/bin/bash

# Kill all existing tmux sessions
tmux kill-server 2>/dev/null || true

# cd into project folder
cd ~/MLH-Fellowship-Portfolio-site

# Pull latest changes from GitHub
git fetch && git reset origin/main --hard

# Enter virtual environment and install dependencies
source python3-virtualenv/bin/activate
pip install -r requirements.txt

# Start a new detached tmux session that runs Flask
tmux new-session -d -s flask -c ~/MLH-Fellowship-Portfolio-site \; \
  send-keys 'source python3-virtualenv/bin/activate && flask run --host=0.0.0.0 --port=5000' Enter
