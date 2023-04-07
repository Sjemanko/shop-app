#!/bin/bash
#APP_PORT=${PORT:-8000}
cd /app/
/opt/venv/bin/python manage.py runserver 0.0.0.0:8000
#/opt/venv/bin/gunicorn --worker-tmp-dir /dev/shm shopApp.wsgi:application
# --bind "localhost:${APP_PORT}"