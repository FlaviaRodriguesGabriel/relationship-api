#!/usr/bin/env bash
# shellcheck disable=SC2034
set -euo pipefail


## Define paths
DIRNAME="$(dirname "$0")"
APP_DIR="$DIRNAME/.."
MAIN_MODULE="src"
SOURCE_DIR="$APP_DIR/$MAIN_MODULE"
CONFIG_FILE_BANDIT="$APP_DIR/setup-bandit.yml"
CONFIG_FILE_GENERAL="$APP_DIR/setup.cfg"

DIRNAME="$(realpath --relative-to=. "$DIRNAME")"
APP_DIR="$(realpath --relative-to=. "$APP_DIR")"
SOURCE_DIR="$(realpath "$SOURCE_DIR")"
CONFIG_FILE_BANDIT="$(realpath "$CONFIG_FILE_BANDIT")"
CONFIG_FILE_GENERAL="$(realpath "$CONFIG_FILE_GENERAL")"

readonly DIRNAME
readonly APP_DIR
readonly MAIN_MODULE
readonly SOURCE_DIR
readonly CONFIG_FILE_BANDIT
readonly CONFIG_FILE_GENERAL


## Custom print function
BLACK="\033[0;30m"
RED="\033[0;31m"
GREEN="\033[0;32m"
BROWN_ORANGE="\033[0;33m"
BLUE="\033[0;34m"
PURPLE="\033[0;35m"
CYAN="\033[0;36m"
LIGHT_GRAY="\033[0;37m"
DARK_GRAY="\033[1;30m"
LIGHT_RED="\033[1;31m"
LIGHT_GREEN="\033[1;32m"
YELLOW="\033[1;33m"
LIGHT_BLUE="\033[1;34m"
LIGHT_PURPLE="\033[1;35m"
LIGHT_CYAN="\033[1;36m"
WHITE="\033[1;37m"
NO_COLOR='\033[0m'

readonly BLACK
readonly RED
readonly GREEN
readonly BROWN_ORANGE
readonly BLUE
readonly PURPLE
readonly CYAN
readonly LIGHT_GRAY
readonly DARK
readonly LIGHT_RED
readonly LIGHT_GREEN
readonly YELLOW
readonly LIGHT_BLUE
readonly LIGHT_PURPLE
readonly LIGHT_CYAN
readonly WHITE
readonly NO_COLOR

echoc() (
 COLOR="$1"
  # shellcheck disable=SC2124
  MSG="${@:2}"
  echo -e "$COLOR$MSG$NO_COLOR"
)

print_header() (
  MSG="$*"
  printf "\n\n"
  echoc "$YELLOW" "$MSG"
)


## Enter into Python virtual environment
virtualenv -p py38 .venv > /dev/null
# shellcheck disable=SC1091
. .venv/bin/activate


## Lint the code
print_header Running bandit...
python -m bandit --configfile "$CONFIG_FILE_BANDIT" "$SOURCE_DIR"

print_header Running black...
# python -m black --config "$CONFIG_FILE_GENERAL" "$SOURCE_DIR"
python -m black "$SOURCE_DIR"

print_header Running flake8...
python -m flake8 --config "$CONFIG_FILE_GENERAL" "$SOURCE_DIR"

print_header Running isort...
python -m isort --settings-path "$CONFIG_FILE_GENERAL" "$SOURCE_DIR"

print_header Running mypy...
python -m mypy  --config-file  "$CONFIG_FILE_GENERAL" "$SOURCE_DIR"
