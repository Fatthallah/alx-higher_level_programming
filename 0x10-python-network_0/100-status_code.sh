#!/bin/bash 
# THe Comment
curl -s -L -X HEAD -w "%{http_code}" "$1"
