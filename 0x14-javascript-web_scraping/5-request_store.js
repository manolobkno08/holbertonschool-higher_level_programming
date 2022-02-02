#!/usr/bin/node
const request = require('request');
const fs = require('fs');

const args = process.argv.slice(2);
const url = args[0];
const filename = args[1];

async function Loripsum () {
  await request(url, function (err, response, body) {
    if (err) {
      console.log(err);
    }
    fs.writeFile(filename, body, 'utf8', err => {
      if (err) {
        console.error(err);
      }
    });
  });
}

Loripsum();
