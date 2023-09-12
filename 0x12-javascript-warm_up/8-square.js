#!/usr/bin/node
let i = parseInt(process.argv[2]);
let shape = '';
if (!isNaN(i)) {
	for (let j = i; j > 0; j--) {
		shape += 'X';
	}
	for (j = i; j > 0; j--) {
		console.log(shape);
	}
} else {
	console.log('Missing size');
}
