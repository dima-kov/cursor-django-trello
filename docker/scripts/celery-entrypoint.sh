#!/usr/bin/env bash

cd trello && celery -A src.common.celery worker -l info --concurrency=2