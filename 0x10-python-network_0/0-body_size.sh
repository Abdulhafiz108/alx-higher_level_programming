#!/bin/bash
# A bash script that displays the size of the body of a get request
curl -s "$1" | wc -c
