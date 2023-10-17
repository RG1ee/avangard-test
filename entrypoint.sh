#!/bin/bash

flask --app src.app db upgrade head

if [ "$DEBUG" = 0 ]; then
  gunicorn src.app:app \
    -w 4 \
    -b 0.0.0.0:5000 \
    --error-logfile '-' \
    --log-level debug
else
  runserver
fi
"$@"
