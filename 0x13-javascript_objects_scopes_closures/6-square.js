#!/usr/bin/node

const Square1 = require('./5-square');

module.exports = class Square extends Square1 {
  constructor (size) {
    super(size, size);
    this.size = size;
  }

  charPrint (c) {
    if (c === undefined) {
      for (let i = 0; i < this.size; i++) {
        for (let j = 0; j < this.size; j++) {
          process.stdout.write('X');
        }
        console.log('');
      }
    } else {
      for (let i = 0; i < this.size; i++) {
        for (let j = 0; j < this.size; j++) {
          process.stdout.write(c);
        }
        console.log('');
      }
    }
  }
};
