#!/usr/bin/node

const process = require('process');

const args = process.argv;
// console.log(args[2])

const x = parseInt(args[2]);

try {
  const res = factorial(x);
  console.log(res);
} catch (error) {
  console.log(1);
}

function factorial (x) {
  if (x === 0) {
    return 1;
  }
  return x * factorial(x - 1);
}
