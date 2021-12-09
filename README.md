# DID_DJANGO_SCHEDULE_JOBS_V2

Hi there.
This repo has a few tutorial videos that will you get up and running quickly
1) https://youtu.be/_9MbgyUvDGs - This will walk you through how to set up the project without Docker

### Local Development Setup

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


