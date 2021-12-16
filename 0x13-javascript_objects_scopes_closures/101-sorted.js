#!/usr/bin/node

const obj = require('./101-data').dict;

const newDict = {};

for (let key in obj) {
	if (newDict[obj[key]] === undefined) {
		newDict[obj[key]] = [];
	}
	newDict[obj[key]].push(key);
}
console.log(newDict);
