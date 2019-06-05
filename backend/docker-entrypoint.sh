#!/bin/sh
sleep 3
pipenv run python manage.py makemigrations
pipenv run python manage.py migrate
# pipenv run python manage.py loaddata users.json
pipenv run python manage.py collectstatic --noinput
#echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('unai', 'unaipg@gmail.com', '1234')" | pipenv run python manage.py shell
pipenv run gunicorn -b :8000 -w 4 backend.wsgi
