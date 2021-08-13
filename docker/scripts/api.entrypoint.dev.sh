#!/usr/bin/env bash

./trello/docker/scripts/wait-for-it.sh postgres:5432 -s -t 30 --

python trello/src/manage.py runserver 0.0.0.0:8000 || { echo 'runserver failed' ; exit 1; }
