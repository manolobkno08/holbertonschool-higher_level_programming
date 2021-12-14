#!/usr/bin/node

const process = require('process');

const args = process.argv;
// console.log(args[2])

if (args.length <= 2) {
  console.log('Not a number');
} else if (args[2]) {
  const x = parseInt(args[2]);
  if (isNaN(x)) {
    console.log('Not a number');
  } else {
    console.log('My number: ' + x);
  }
}
