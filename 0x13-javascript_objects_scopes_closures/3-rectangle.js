#!/usr/bin/node

module.exports = class Rectangle {
	constructor(w, h) {
		if (w > 0 && h > 0) {
			this.width = w;
			this.height = h;
		}
	}

	print() {
		let shape = '';
		for (let i = this.width; i > 0; i--) {
			shape += 'X';
		}
		for (let i = this.height; i > 0; i--) {
			console.log(shape);
		}
	}
};
