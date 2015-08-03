# Challenge Problems: a worked example

Talk given at [develop denver](https://developdenver.org/), August 7th 2015

## Problemsets

- [99 Prolog 
  Problems](http://www.ic.unicamp.br/~meidanis/courses/mc336/2009s2/prolog/problemas/)
- [99 Lisp 
  Problems](http://www.ic.unicamp.br/~meidanis/courses/mc336/2006s2/funcional/L-99_Ninety-Nine_Lisp_Problems.html)
- [99 Haskell](https://wiki.haskell.org/H-99:_Ninety-Nine_Haskell_Problems)
- [Ponder This](https://www.research.ibm.com/haifa/ponderthis/index.shtml)
- [Python Challenge](http://www.pythonchallenge.com/)
- [/r/programming 
  thread](http://www.reddit.com/r/programming/comments/70y1m/ask_proggit_does_anyone_know_of_an_online)

fd_

## Building slides

### Build Requirements

- python 2.7.x
- node
- sass

To build the slides, `cd slidedeck && make`. Slides are generated as 
`slidedeck/index.html`

## Running testcases

In directory `code/`:

`node fixture.js <implementation> [<case>]` runs
`case/<implementation>.js`. If `<case>` is specified, only the indicated
case from `cases.json` is tried.

`fixture.py <implementation> [<case>]` runs
`case/<implementation>.py`. If `<case>` is specified, only the indicated
case from `cases.json` is tried.

## Manifest:

- `README.md`: this file
- `slidedeck/`: slidedeck root
- `slidedeck/Makefile`: slidedeck Makefile. Interesting targets are 
  `default`, `generate-html`, and `generate-sass`
- `slidedeck/bin/assemble.py`: slidedeck generator, called by Makefile
- `slidedeck/src`: slide source files
- `slidedeck/custom`: custom stylesheets
- `slidedeck/deck.js`: submodule copy of
  [deck.js](http://imakewebthings.com/deck.js/)
- `slidedeck/highlight.js`: stock copy of 
  [highlight.js](https://highlightjs.org/)
- `code/cases.json`: test cases
- `code/fixture.js`: test fixture for js implementations
- `code/fixture.py`: test fixture for python implementations
- `code/implementations/`: solution implementations
