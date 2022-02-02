#!/usr/bin/node
const request = require('request');

const args = process.argv.slice(2);
const url = args[0];

async function taskCompleted() {
	await request(url, function (err, response, body) {
		if (err) {
			console.log(err);
		}
		const obj = JSON.parse(body);
		let data = obj;
		let dict = {};
		let count = 0;

		for (let user of data) {
			if (user.completed === true) {
				if (dict[user.userId] === undefined) {
					count = 1;
				}
				else {
					count += 1;
				}
				dict[user.userId] = count;
			}
		}
		console.log(dict);
	});
}

taskCompleted();
