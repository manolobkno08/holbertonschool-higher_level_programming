#!/usr/bin/node
const request = require('request');

const args = process.argv.slice(2);
const idMovie = args[0];
const url = 'https://swapi-api.hbtn.io/api/films/';

async function movieById () {
  await request(url + idMovie, function (err, response, body) {
    if (err) {
      console.log(err);
    }
    const obj = JSON.parse(body).characters;
    for (const item of obj) {
      request(item, function (err, response, body) {
        if (err) {
          console.log(err);
        }
        const r = JSON.parse(body);
        console.log(r.name);
      });
    }
  });
}

movieById();
