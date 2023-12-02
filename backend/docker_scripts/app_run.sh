#!/bin/bash

sh -c './wait-for db:5432 -- npm start'  # doesnt work nc command is missing!

sleep 20  # wait for bd

gunicorn app.__main__:app --workers 2 --worker-class uvicorn.workers.UvicornWorker --bind=0.0.0.0:8000