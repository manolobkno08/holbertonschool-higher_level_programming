#!/usr/bin/node

const process = require('process');

const args = process.argv;

const argsL = args.length;

if (argsL <= 2) {
  console.log('No argument');
} else if (argsL === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
