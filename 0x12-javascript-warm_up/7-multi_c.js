#!/usr/bin/node

const process = require('process');

const args = process.argv;
// console.log(args[2])

const x = parseInt(args[2]);
if (isNaN(x)) {
  console.log('Missing number of occurrences');
}
let i = 0;
while (i < x) {
  console.log('C is fun');
  i++;
}
