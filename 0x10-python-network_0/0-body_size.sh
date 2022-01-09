#!/bin/bash
# displays the size of the body of the response

params=$1
port=5000
curl -sI "$params":$port | grep -i content-length | awk '{print $2}'
