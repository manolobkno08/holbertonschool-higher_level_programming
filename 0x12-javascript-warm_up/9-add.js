#!/usr/bin/node

const process = require('process');

const args = process.argv;
// console.log(args[2])

const a = parseInt(args[2]);
const b = parseInt(args[3]);

try {
  const x = add(a, b);
  console.log(x);
} catch (error) {
  console.error('NaN');
}

function add (a, b) {
  return (a + b);
}
