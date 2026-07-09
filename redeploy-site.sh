#!/bin/bash

# cd into project folder
cd ~/MLH-Fellowship-Portfolio-site

# Pull latest changes from GitHub
git fetch && git reset origin/main --hard

# Enter virtual environment and install dependencies
source python3-virtualenv/bin/activate
pip install -r requirements.txt

# Restart myportfolio service
sudo systemctl restart myportfolio
