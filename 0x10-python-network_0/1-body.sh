#!/bin/bash
# body of the response by GET method
curl -s -w "%{http_code}" -X GET "$1"
