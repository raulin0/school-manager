#!/bin/bash

set -e

python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser --noinput

if [ "$DJANGO_ENV" = "production" ]; then
    gunicorn school_manager.wsgi:application
else
    python manage.py runserver 0.0.0.0:8000
fi
