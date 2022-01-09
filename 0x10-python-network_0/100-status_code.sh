#!/bin/bash
# Header variables - POST
curl -s -o /dev/null -w "%{http_code}" "$1"
