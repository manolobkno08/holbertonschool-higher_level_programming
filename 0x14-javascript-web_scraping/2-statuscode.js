#!/usr/bin/node
const request = require('request');
const args = process.argv.slice(2);
const url = args[0];

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  }
  console.log('code: ' + response.statusCode);
});
