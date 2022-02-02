#!/usr/bin/node
const request = require('request');

const args = process.argv.slice(2);
const url = args[0];

async function taskCompleted () {
  await request(url, function (err, response, body) {
    if (err) {
      console.log(err);
    }
    const obj = JSON.parse(body);
    const data = obj;
    const dict = {};

    for (const user of data) {
      if (user.completed) {
        if (dict[user.userId] === undefined) {
          dict[user.userId] = 1;
        } else {
          dict[user.userId] += 1;
        }
      }
    }
    console.log(dict);
  });
}

taskCompleted();
