#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
	let num = 0;
	let i = 0;
	while (list[i]) {
		if (list[i] === searchElement) {
			num++;
		}
		i++;
	}
	return num;
}
