#!/bin/sh
sleep 3
pipenv run python manage.py makemigrations
pipenv run python manage.py migrate
# pipenv run python manage.py loaddata users.json
pipenv run python manage.py collectstatic --noinput
pipenv run gunicorn -b :8000 -w 4 backend.wsgi
