#!/bin/bash

# Get absolute path of the script.
PARENT_PATH=$( cd "$(dirname "${BASH_SOURCE}")" ; pwd -P )

cd "$PARENT_PATH"
mkdir -p log

echo 'Starting gunicorn...'
gunicorn main --bind 0.0.0.0:80 --access-logfile log/access.log --error-logfile log/error.log
