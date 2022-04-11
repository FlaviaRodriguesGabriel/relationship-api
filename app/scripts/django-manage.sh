#! /usr/bin/env bash

DIRNAME="$(dirname "$0")"
ENV_FILE="$DIRNAME/../.env"
SOURCE_DIR="$DIRNAME/../src"

# shellcheck disable=SC2046
export $(grep -o '^[^#]*' "$ENV_FILE" | xargs)
export PYTHONPATH="$SOURCE_DIR:$PYTHONPATH"

if [ "$*" = "" ]; then
    ARGS="shell"
else
    ARGS="$*"
fi

set -x
# shellcheck disable=SC2048,SC2086
"$DIRNAME/../src/inputs/http_server/manage.py" $ARGS
