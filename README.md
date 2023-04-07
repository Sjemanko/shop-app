# Prototype of e-commerce Cloth shop

## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)

## General info
My first project in web development. Project created to practice programming web applications.

## Technologies

Project is mainly created with:

* Django 4.1.3
* gunicorn
* python-dotenv
* psycopg2-binary
* whitenoise
* django-widget-tweaks
* Pillow
* django-crispy-forms

* Bootstrap 5.0

## Docker requirements
1) Run docker compose up in docker-compose.yaml directory
2) If there's a problem with finding .sh scripts while docker's setting up containers, try to change "End of line sequence" from CRLF To LF in both files.


//TODO
* postgresql scripts for populating data
* fix bugs (with creating object after register user "Cart", "Profile")
* fix associations with models
