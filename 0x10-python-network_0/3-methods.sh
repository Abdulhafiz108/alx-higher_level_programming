#!/bin/bash
# Displays all HTTP methods a server will accept.
curl -sI "$1" | grep Allow | sed 's/Allow: //'
