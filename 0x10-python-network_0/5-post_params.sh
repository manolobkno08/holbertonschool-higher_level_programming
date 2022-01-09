#!/bin/bash
# Header variables - POST
curl -sI -d "email:test@gmail.com&subject:I will always be here for PLD" -H "Content-Type: application/json" -X POST "$1"
