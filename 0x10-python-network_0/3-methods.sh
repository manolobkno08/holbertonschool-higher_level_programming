#!/bin/bash
# Get all methods allowed
curl -si -X OPTIONS "$1" | grep Allow
