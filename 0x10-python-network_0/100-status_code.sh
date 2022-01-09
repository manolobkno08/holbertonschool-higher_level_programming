#!/bin/bash
# Header variables - POST
curl -s -o /dev/null -s -w "%{http_code}" "$1"
