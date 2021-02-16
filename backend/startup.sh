#!/usr/bin/env bash
python manage.py collectstatic --noinput &&
python manage.py migrate &&
gunicorn pichess.wsgi:application -w 2 -b :80
