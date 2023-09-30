#!/bin/bash
# Sends a Post request with a variable and value
curl -sd "email=test@gmail.com&subject=I will always be here for PLD" -X POST "$1"
