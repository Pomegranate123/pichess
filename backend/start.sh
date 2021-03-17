#/bin/sh
python manage.py runserver 0:8000 &
daphne -b 0.0.0.0 -p 8001 pichess.asgi:application
