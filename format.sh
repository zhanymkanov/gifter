#!/bin/sh -e
set -x

autoflake --remove-all-unused-imports --recursive --remove-unused-variables --in-place config apps tests --exclude=__init__.py
isort --recursive --apply config apps tests
black config apps tests
