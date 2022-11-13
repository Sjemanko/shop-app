#!/bin/bash
SUPERUSER_EMAIL=${DJANGO_SUPERUSER_EMAIL}
cd /app/
/opt/venv/bin/python manage.py migrate --noinput
/opt/venv/bin/python manage.py createsuperuser --noinput || true
