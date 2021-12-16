#!/usr/bin/node

const obj = require('./101-data').dict;

const newDict = {};

for (const key in obj) {
  if (newDict[obj[key]] === undefined) {
    newDict[obj[key]] = [];
  }
  newDict[obj[key]].push(key);
}
console.log(newDict);
