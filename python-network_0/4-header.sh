#!/bin/bash
#Sending a get request with the required custom header
curl -s -H "X=HolbertonSchool-User-Id: 98" "$1"
