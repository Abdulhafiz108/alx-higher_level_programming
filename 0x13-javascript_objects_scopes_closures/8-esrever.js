#!/usr/bin/node

exports.esrever = function (list) {
	let tmp = [];
	let i = list.length - 1;
	while (i >= 0) {
		tmp.push(list[i]);
		i--;
	}
	return tmp;
}
