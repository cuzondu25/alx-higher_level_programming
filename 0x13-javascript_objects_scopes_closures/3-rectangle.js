#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if ((w > 0) && (h > 0)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let m = 0; m < this.height; m++) {
      let s = '';
      for (let n = 0; n < this.width; n++) {
        s += 'X';
      }
      console.log(s);
    }
  }
}

module.exports = Rectangle;
