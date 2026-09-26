#!/bin/bash
#Sending a post request with the required custom header
curl -s -X POST -d "email=test@gmail.com" -d "subject=I will always be here for PLD" "$1"
