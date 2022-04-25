#! /usr/bin/env bash
set -euo pipefail


## Define paths
DIRNAME="$(dirname "$0")"
APP_DIR="$DIRNAME/.."
MAIN_MODULE="src"
SOURCE_DIR="$APP_DIR/$MAIN_MODULE"
ENV_FILE="$APP_DIR/.env"

DIRNAME="$(realpath --relative-to=. "$DIRNAME")"
APP_DIR="$(realpath --relative-to=. "$APP_DIR")"
SOURCE_DIR="$(realpath "$SOURCE_DIR")"
ENV_FILE="$(realpath --relative-to=. "$ENV_FILE")"

readonly DIRNAME
readonly APP_DIR
readonly MAIN_MODULE
readonly SOURCE_DIR
readonly ENV_FILE


## Export environment variables from `.env` file
if [ ! -f "$ENV_FILE" ]; then
    echo "ERROR: '$ENV_FILE' not found!"
    exit 1
fi
# shellcheck disable=SC2046
export $(grep -o '^[^#]*' "$ENV_FILE" | xargs)


## Enter into Python virtual environment
echo "Entering Python virtual environment..."
virtualenv -p py38 .venv > /dev/null
# shellcheck disable=SC1091
. .venv/bin/activate


## Run tests
ARGS="$*"
set -x
(
    cd "$SOURCE_DIR/.."

    ## Define main module path
    export PYTHONPATH="$SOURCE_DIR:${PYTHONPATH:-}"

    # shellcheck disable=SC2048,SC2086
    python -m pytest "./tests" $ARGS
)
