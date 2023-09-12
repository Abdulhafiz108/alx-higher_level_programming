#!/usr/bin/node
function fact(a) {
	if (isNaN(a) || a === 0 || a === 1)
		return 1;
	else
		return a * fact(a - 1);
}

let num = parseInt(process.argv[2]);
console.log(fact(num));
