#!/bin/bash

# Get absolute path of the script.
PARENT_PATH=$( cd "$(dirname "${BASH_SOURCE}")" ; pwd -P )

cd "$PARENT_PATH"

# Make log directory.
mkdir -p "$PARENT_PATH/log"

echo 'Starting gunicorn...'
gunicorn main --bind 0.0.0.0:80 --access-logfile log/access.log --error-logfile log/error.log
