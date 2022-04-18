#!/usr/bin/env bash
set -euo pipefail


## Define paths
DIRNAME="$(dirname "$0")"
APP_DIR="$DIRNAME/.."
ENV_FILE="$APP_DIR/.env"

DIRNAME="$(realpath --relative-to=. "$DIRNAME")"
APP_DIR="$(realpath --relative-to=. "$APP_DIR")"
ENV_FILE="$(realpath --relative-to=. "$ENV_FILE")"

readonly DIRNAME
readonly APP_DIR
readonly ENV_FILE


## Enter into Python virtual environment
virtualenv -p py38 .venv
# shellcheck disable=SC1091
. .venv/bin/activate


## Install Python app's requirements
pip install --upgrade pip
pip install -r app/requirements-dev.txt


## Copy environment variables from `.env.default` to `.env` file
# TODO: add method that merge `.env.default` into `.env`
if [ ! -f "$ENV_FILE" ]; then
    cp "$ENV_FILE.default" "$ENV_FILE"
fi
