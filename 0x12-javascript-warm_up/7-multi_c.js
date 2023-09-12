#!/usr/bin/node
let i = parseInt(process.argv[2]);
if (!isNaN(i)) {
	while (i > 0) {
		console.log('C is fun');
		i--;
	}
} else {
	console.log('Missing number of occurrences');
}
