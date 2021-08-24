#!/usr/bin/env bash


gunicorn trello.src.config.wsgi -b 0.0.0.0:8000 || { echo 'runserver failed' ; exit 1; }
