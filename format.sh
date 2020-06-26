#!/bin/sh -e
set -x

autoflake --remove-all-unused-imports --recursive --remove-unused-variables --in-place config --exclude=__init__.py
isort --recursive --apply config
black config
