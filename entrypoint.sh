#!/bin/bash

set -e

if [ -f /app/prod_db.sqlite3 ]; then
	echo "Database already exists, skipping restore"
else
	echo "No database found, restoring from replica if exists"
	litestream restore -v -if-replica-exists -o prod_db.sqlite3 "${LITESTREAM_REPLICA_URL}"
fi

python manage.py migrate

litestream replicate -exec "gunicorn --bind :8080 --workers 2 project.wsgi"
