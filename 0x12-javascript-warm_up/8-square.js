#!/usr/bin/node

const process = require('process');

const args = process.argv;
// console.log(args[2])

const x = parseInt(args[2]);
if (isNaN(x)) {
  console.log('Missing size');
}
let i = 0;
while (i < x) {
  let con = '';
  for (let j = 0; j < x; j++) {
    con += 'X';
  }
  console.log(con);
  i++;
}
