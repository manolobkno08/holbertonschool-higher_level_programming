#!/usr/bin/node
const request = require('request');

const args = process.argv.slice(2);
const episode = args[0];

async function movieTitle () {
  const url = 'https://swapi-api.hbtn.io/api/films/';
  request(url + episode, function (err, response, body) {
    if (err) {
      console.log(err);
    }
    const obj = JSON.parse(body);
    console.log(obj.title);
  });
}

movieTitle();
