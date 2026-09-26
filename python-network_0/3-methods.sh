#!/bin/bash
#Displaying all http methods accepted by the server
curl -s -X OPTIONS -i "$1" | grep "Allow:" | cut -d " " -f 2-
