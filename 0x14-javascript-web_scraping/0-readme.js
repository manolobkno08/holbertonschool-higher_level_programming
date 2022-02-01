#!/usr/bin/node
const fs = require('fs');
const args = process.argv.slice(2);
const file = args[0];

fs.readFile(file, 'utf-8', (err, data) => {
	if (err) {
		console.error(err);
		return;
	}
	console.log(data);
})

// Write a script that reads and prints the content of a file.

// The first argument is the file path
// If an error occurred during the reading, print the error object
