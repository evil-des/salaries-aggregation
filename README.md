# Aggregation Telegram Bot
Aggregate salaries data in Telegram Bot

### Example #1:
**_Input:_**
   `{"dt_from": "2022-09-01T00:00:00", "dt_upto": "2022-12-31T23:59:00", "group_type": "month"}`

**_Output:_**:
   `{"dataset": [5906586, 5515874, 5889803, 6092634], "labels": ["2022-09-01T00:00:00", "2022-10-01T00:00:00", "2022-11-01T00:00:00", "2022-12-01T00:00:00"]}`

### Example #2:
**_Input:_**
   `{"dt_from": "2022-02-01T00:00:00", "dt_upto": "2022-02-02T00:00:00", "group_type": "hour"}`

**_Output:_**:
   `{"dataset": [8177, 8407, 4868, 7706, 8353, 7143, 6062, 11800, 4077, 8820, 4788, 11045, 13048, 2729, 4038, 9888,
            7490, 11644, 11232, 12177, 2741, 5341, 8730, 4718, 0], "labels": ["2022-02-01T00:00:00", "2022-02-01T01:00:00", "2022-02-01T02:00:00", "2022-02-01T03:00:00",
           "2022-02-01T04:00:00", "2022-02-01T05:00:00", "2022-02-01T06:00:00", "2022-02-01T07:00:00",
           "2022-02-01T08:00:00", "2022-02-01T09:00:00", "2022-02-01T10:00:00", "2022-02-01T11:00:00",
           "2022-02-01T12:00:00", "2022-02-01T13:00:00", "2022-02-01T14:00:00", "2022-02-01T15:00:00",
           "2022-02-01T16:00:00", "2022-02-01T17:00:00", "2022-02-01T18:00:00", "2022-02-01T19:00:00",
           "2022-02-01T20:00:00", "2022-02-01T21:00:00", "2022-02-01T22:00:00", "2022-02-01T23:00:00",
           "2022-02-02T00:00:00"]}`

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