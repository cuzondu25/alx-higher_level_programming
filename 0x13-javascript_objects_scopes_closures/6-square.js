#!/usr/bin/node
const SquareP = require('./5-square');

class Square extends SquareP {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let m = 0; m < this.height; m++) {
      let s = '';
      for (let n = 0; n < this.width; n++) {
        s += c;
      }
      console.log(s);
    }
  }
}

module.exports = Square;
