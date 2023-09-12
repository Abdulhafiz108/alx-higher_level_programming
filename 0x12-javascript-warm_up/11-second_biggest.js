#!/usr/bin/node
if (process.argv.length - 2 > 1) {
	let mylist = process.argv.slice(2).map(arg => parseInt(arg));
	let max1 = mylist[1];
	let max2 = mylist[0];
	if (max2 > max1) {
		max2 = mylist[1];
		max1 = mylist[0];
	} for (let i = 2; i < mylist.length; i++) {
		if (mylist[i] > max1) {
			max2 = max1;
			max1 = mylist[i];
		} else if (mylist[i] < max1 && mylist[i] > max2) {
			max2 = mylist[i];
		}
	}
	console.log(max2);
} else {
	console.log(0);
}
