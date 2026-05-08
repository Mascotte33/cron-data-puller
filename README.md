# Poland Weather Dashboard

An automated weather dashboard that fetches live data for 5 Polish cities every hour using GitHub Actions and displays it via GitHub Pages

## What it does

- Dynamic Content Display
- Checks weather for a couple of different Polish cities using the weatherapi.com api
- Html file which updates the existing one using a template.html 
- Updates the temperature, condition, and "last updated" timestamp in a readable format
- GitHub Actions workflow which runs automatically every hour using cron schedule

## Live Site
https://mascotte33.github.io/cron-data-puller/

## Tech Stack
- Language: Python, html
- API: weatherapi.com
- Automation: GitHub Actions
- Hosting: GitHub Pages

## Setup (local)
1. Clone the repo
2. Get a free API key from weatherapi.com
3. Create an .env file with WEATHER_API_KEY=your key
4. pip install requests python-dotenv
5. python3 main.py

## GitHub Actions
The GitHub Actions automatically reruns every 1 hour. It also supports manual triggering via workflow_dispatch, and it commits and pushes index.html automatically.