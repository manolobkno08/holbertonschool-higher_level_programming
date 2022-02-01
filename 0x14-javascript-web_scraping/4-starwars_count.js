#!/usr/bin/node
const request = require('request');

const args = process.argv.slice(2);
const url = args[0];

async function wedgeAntilles () {
  await request(url, function (err, response, body) {
    if (err) {
      console.log(err);
    }
    const user = 'https://swapi-api.hbtn.io/api/people/18/';
    const obj = JSON.parse(body);
    let count = 0;
    const data = obj.results;
    for (const item of data) {
      for (const char of item.characters) {
        if (char === user) {
          count++;
        }
      }
    }
    console.log(count);
  });
}

wedgeAntilles();
