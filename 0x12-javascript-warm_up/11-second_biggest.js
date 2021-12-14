#!/usr/bin/node

const process = require('process');

const args = process.argv;

myArray = [];

if (args.length <= 3) {
	console.log(0)
} else if (args.length > 3){
	args.forEach(function (element) {
		const x = parseInt(element);
		if (isNaN(x)) {
			myArray.push('');
		}
		myArray.push(element);
	});
	console.log(myArray);
}
