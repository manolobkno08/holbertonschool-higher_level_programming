#!/usr/bin/node

const Square1 = require('./5-square');

module.exports = class Square extends Square1 {
  charPrint (c) {
    if (c === undefined) {
      for (let i = 0; i < this.height; i++) {
        for (let j = 0; j < this.width; j++) {
          process.stdout.write('X');
        }
        console.log('');
      }
    } else {
      for (let i = 0; i < this.height; i++) {
        for (let j = 0; j < this.width; j++) {
          process.stdout.write(c);
        }
        console.log('');
      }
    }
  }
};
