#!/usr/bin/node
const fs = require('fs');
const args = process.argv.slice(2);
const file_path = args[0];
const content = args[1];

fs.writeFile(file_path, content, 'utf8', err => {
  if (err) {
    console.error(err);
  }
});
