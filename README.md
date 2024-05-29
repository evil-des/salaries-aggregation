# Aggregation Telegram Bot
Aggregate data using Telegram bot


### Installation and Running (Manual)
1. Create a new .env file and change all settings:

    `cp .env.example .env`

2. Install all dependencies:

    `poetry install`
3. Restore MongoDB from dump using this command:

    `mongorestore --host localhost --port 27017 dump/`

4. Run Telegram bot:

    `python3 app/bot.py`


### Auto install by Docker
1. Create a new .env file:

    `cp .env.example .env.docker`

2. Change desired options in docker-compose.yml

3. Run this command for the first time build:

    `docker-compose up -d --build`
4. Restore MongoDB from dump:

    `docker exec -it salaries-aggregation-mongodb-1 /usr/bin/mongorestore --host localhost --port 27017 /dump/`