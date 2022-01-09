#!/bin/bash
# Get all methods allowed
curl -s OPTIONS * "$1"
