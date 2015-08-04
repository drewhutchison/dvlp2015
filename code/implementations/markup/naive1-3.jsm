"use strict";

var solution = function(pirates) {

  console.log('solutioning', pirates)

  var spoken = []; // pirates we've spoken to
  var current_pirate = 0; // pirate we're presently speaking to

  for (var i=0; i<=pirates.length; i++) {

<span id="chighlight">    if (spoken.indexOf(current_pirate) == -1) {
      // we haven't talked to current_pirate yet
      spoken.push(current_pirate);
      current_pirate = pirates[current_pirate];
    }</span> else {
      // otherwise, we're done
      return spoken.length;
    };

  };
};

module.exports.solution = solution;

console.log(solution([1, 2, 0]));
