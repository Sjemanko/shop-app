#!/bin/bash
APP_PORT=${PORT:-8001}
cd /app/
/opt/venv/bin/gunicorn --worker-tmp-dir /dev/shm shopApp.wsgi:application
--bind "localhost:${APP_PORT}"