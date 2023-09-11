#!/usr/bin/node
let value = process.argv[2];
let convert = parseInt(value);
if (!isNaN(value)) {
	console.log('My number: ' + convert);
} else {
	console.log('Not a number');
}
