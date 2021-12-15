#!/usr/bin/node

const process = require('process');

const args = process.argv;

const myArray = [];

if (args.length <= 3) {
  console.log(0);
} else if (args.length > 3) {
  args.forEach(function (element) {
    const x = parseInt(element);
    if (!isNaN(x)) {
      myArray.push(parseInt(element));
    }
  });
  myArray.sort(function (a, b) { return a - b; });
  myArray.pop();
  const x = myArray[myArray.length - 1];
  console.log(parseInt(x));
}
