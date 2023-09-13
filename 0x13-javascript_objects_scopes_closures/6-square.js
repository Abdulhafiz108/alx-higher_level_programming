#!/usr/bin/node
const oldsquare = require('./5-square');

module.exports = class Square extends oldsquare {
	constructor(size) {
		super(size, size);
	}

	charPrint(c) {
		if (c === undefined) {
			c = 'X';
		}
		let shape = '';
		for (let i = this.width; i > 0; i--) {
			shape += c;
		}
		for (let i = this.height; i > 0; i--) {
			console.log(shape);
		}
	}
};
