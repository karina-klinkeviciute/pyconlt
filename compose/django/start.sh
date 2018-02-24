#!/bin/sh

set -o errexit
set -o pipefail
set -o nounset
set -o xtrace

python manage.py migrate
gunicorn pyconlt.wsgi -b 0.0.0.0:8999
