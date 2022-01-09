#!/bin/bash
# Get all methods allowed
curl -s -X OPTIONS "$1" -i
