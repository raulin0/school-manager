#!/bin/bash

set -e

# Apply database migrations
python manage.py makemigrations
python manage.py migrate

# Check if a superuser already exists
existing_superuser=$(python manage.py shell -c "from django.contrib.auth.models import User; print(User.objects.filter(is_superuser=True).exists())")

# If no superuser exists, create one
if [ "$existing_superuser" != "True" ]; then
    python manage.py createsuperuser --noinput
    echo "Superuser created successfully."
else
    echo "Superuser already exists. Skipping creation."
fi

# Check the environment variable DJANGO_ENV
if [ "$DJANGO_ENV" = "production" ]; then
    # Run Gunicorn in production
    gunicorn school_manager.wsgi:application
else
    # Run the development server
    python manage.py runserver 0.0.0.0:8000
fi
