#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi
python manage.py flush --no-input
# python manage.py migrate

gunicorn api.wsgi:application --bind "0.0.0.0:8000" --workers 1 --threads 8 --timeout 0

# nginx -g 'daemon off;'

exec "$@"