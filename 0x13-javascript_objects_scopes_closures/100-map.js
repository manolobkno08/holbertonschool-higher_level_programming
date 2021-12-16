#!/usr/bin/node

const array1 = require('./100-data').list;

let idx = 0;
const newArray = array1.map(x => x * idx++);

console.log(array1);
console.log(newArray);
