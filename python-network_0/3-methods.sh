#!/bin/bash
# Script that displays all HTTP methods the server will accept
curl -s -X OPTIONS -I "$1" | grep "Allow:" | cut -d' ' -f2-
