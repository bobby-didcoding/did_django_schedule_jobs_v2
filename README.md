# DID_DJANGO_SCHEDULE_JOBS_V2

Hi there.
This repo has a few tutorial videos that will you get up and running quickly
1) https://youtu.be/_9MbgyUvDGs - This will walk you through how to set up the project without Docker

### Local Development Setup
1. Clone this repo `git clone git@github.com:bobby-didcoding/did_django_schedule_jobs_v2.git`
2. Create your .env file from the template file `cp .env.template backend/.env`

### Install Redis for Celery
1. Install 'Ubuntu' and set up Redis (https://www.youtube.com/watch?v=_nFwPTHOMIY)
2. Download `Ubunto` from `windows store` and launch app
3. create a username (must be an email) & password
4. Now create redis repository `sudo apt-add-repository ppa:redislabs/redis`
5. Now update and upgrade packages `sudo apt-get update` then `sudo apt-get upgrade`
6. Now install Redis `sudo apt-get install redis-server`
### Config
7. Create a `.env` file from the `.env.template` and fill-in the environment variables specific to your setup (eg. DB
   name, user and password) - Save this into `/backend`
8. Set up a virtual environment `cd backend && python -m venv env`
9. Activate virtual environment `cd env/scripts && activate && cd ../..`
10. Install dependencies for your local environment by running `pip install -r requirements/Local.txt`
11. Run `python manage.py migrate`

### Fire up servers
12. Open Ubuntu terminal and fire up a Redis server `redis-server`
13. Open another Ubuntu and set up a Redis CLI `redis-cli`
14. Open new cmd in root and use this command `celery -A did_django_schedule_jobs_v2.celery beat -l INFO`to fire up celery beat
15. Open new cmd in root and use this command `celery -A did_django_schedule_jobs_v2.celery worker --pool=solo -l info` to fire up a celery worker
16. Run `python manage.py runserver`


### Local Development Setup with Docker
1. Clone from docker branch `git clone --branch docker git@github.com:bobby-didcoding/did_django_schedule_jobs_v2.git`
2. Create an env file `cp .env.template .env`
3. Update the DONOT_REPLY_EMAIL and GOOGLE_APP_PASSOWRD variables in the new .env file
4. `cd backend && mkdir logs && cd logs && echo This is our celery log > celery.log && cd ../..`
5. Install Docker & Docker compose
6. Compose a docker image `docker-compose -f docker-compose.yml up -d --build`

# Note: You may get an issue if your github config is not set up for LF. Add these settings to config
1. git config --global core.autocrlf input
2. git config --global core.eol lf
