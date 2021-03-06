"use strict";

var argv = process.argv

var usage = function() {
  console.log("usage:"
              + argv[0]
              + argv[1]
              + "<solution> [case]");
  process.exit(-1);
}

if (argv.length < 3 || argv.length > 4) {
  usage();
};

var solution_file = "./implementations/" + argv[2] + ".js";

console.log('requiring ' + solution_file);
var solution = require(solution_file).solution;

var cases = require('./cases.json');

var try_case = function(i) {

  var thiscase = cases[i];
  var pirates = thiscase.pirates;
  var answer = thiscase.answer;

  console.log();
  console.log("trying testcase " + i + ":", pirates);

  var myanswer = solution(pirates);

  console.log("my answer: " + myanswer + ". correct answer: " + answer);

};

if (argv.length == 4) {
  try_case(argv[3]);
} else {
  for (var i=0; i<cases.length; i++) {
    try_case(i);
}};
