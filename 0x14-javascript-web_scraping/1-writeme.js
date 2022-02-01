#!/usr/bin/node
const fs = require('fs');
const args = process.argv.slice(2);
const filePath = args[0];
const content = args[1];

fs.writeFile(filePath, content, 'utf8', err => {
  if (err) {
    console.error(err);
  }
});
