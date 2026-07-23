#!/bin/bash

# cd into project folder
cd ~/MLH-Fellowship-Portfolio-site

# Pull latest changes from GitHub
git fetch && git reset origin/main --hard

# Spin containers down first to prevent out of memory issues while building
docker compose -f docker-compose.prod.yml down

# Rebuild and start containers
docker compose -f docker-compose.prod.yml up -d --build
