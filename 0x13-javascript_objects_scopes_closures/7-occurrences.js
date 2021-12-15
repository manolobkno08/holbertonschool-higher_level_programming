#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  const rep = [];
  list.forEach(function (element) {
    if (element === searchElement) {
      rep.push(element);
    }
  });
  return rep.length;
};
