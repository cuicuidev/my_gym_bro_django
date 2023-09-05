#!/bin/sh

set -e

python manage.py collectstatic --noinput

gunicorn root.wsgi:application --bind 0.0.0.0:8000