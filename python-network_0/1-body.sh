#!/bin/bash
curl -s -w "%{http_code}" "$1" | {
    read -N -3 body
    read -N 3 status
    if [ "$status" = "200" ]; then
        print "%s" "$body"
    fi
}
