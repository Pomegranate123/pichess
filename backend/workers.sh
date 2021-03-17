#/bin/sh
python manage.py runworker --only-channels=http.* --only-channels=websocket.* -v2
