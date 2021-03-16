#/bin/sh
redis-server &
python manage.py runserver 0:8000
