"use strict";

var solution = function(pirates) {

  var spoken = []; // pirates we've spoken to
  var current_pirate = 0; // pirate we're presently speaking to

  for (var i=0; i<=pirates.length; i++) {

    if (spoken.indexOf(current_pirate) != -1) {
      // if we've talked to current_pirate already
      return spoken.length;
    } else {
      spoken.push(current_pirate);
      current_pirate = pirates[current_pirate];
    };

  };
};

console.log(solution([1, 2, 0]));

module.exports.solution = solution;
