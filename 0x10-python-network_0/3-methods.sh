#!/bin/bash
# Displays all HTTP methods a server will accept.
curl -sX OPTIONS "$1"
