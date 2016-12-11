#!/bin/bash

# Get absolute path of the script.
PARENT_PATH=$( cd "$(dirname "${BASH_SOURCE}")" ; pwd -P )
ROOT_PATH=$( cd "$(dirname "${PARENT_PATH}")" ; pwd -P )

cd "$ROOT_PATH"

# Make log directory.
mkdir -p "$ROOT_PATH/log"

# Remove '.pyc' files.
find . -name '*.pyc' -print0|xargs -0 rm

echo 'Starting gunicorn...'
gunicorn main --bind 0.0.0.0:7000 --access-logfile log/access.log --error-logfile log/error.log
