#!/bin/bash
# SUPERUSER_EMAIL=${DJANGO_SUPERUSER_EMAIL}
# SUPERUSER_USERNAME=${DJANGO_SUPERUSER_USERNAME}
# SUPERUSER_USERNAME=${DJANGO_SUPERUSER_USERNAME}

cd /app/ &&
/opt/venv/bin/python manage.py makemigrations --noinput &&
/opt/venv/bin/python manage.py migrate --noinput &&
/opt/venv/bin/python manage.py createsuperuser --noinput || true