#!/bin/bash
# The Comment
curl -s -I -X OPTIONS "$1" | grep "Allow:" | cut -f2- -d" "
