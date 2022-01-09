#!/bin/bash
# Get all methods allowed
curl -s -i -X OPTIONS -L "$1"
