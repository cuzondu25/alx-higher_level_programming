#!/usr/bin/node
<<<<<<< HEAD
=======

>>>>>>> ee26083ed2a8f37becc8f4f01300c5d3bbee5426
exports.esrever = function (list) {
  let len = list.length - 1;
  let i = 0;
  while ((len - i) > 0) {
    const aux = list[len];
    list[len] = list[i];
    list[i] = aux;
    i++;
    len--;
  }
  return list;
};
