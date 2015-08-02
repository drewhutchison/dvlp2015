#! /usr/bin/env python

from os.path import dirname, realpath, abspath, join
from glob import glob

ROOT_PATH = join(dirname(realpath(__file__)), '..')
SRC_PATH = abspath(join(ROOT_PATH, 'src'))

def copy(infn):
  print 'copying ' + infn
  with open(infn) as infile:
    outfile.writelines(infile.readlines())
    outfile.write('\n')

def fncmp(a, b):

  def listify(fn):
    """
    given fn='slide-1-3-5.html', returns [1, 3, 5]
    """
    l = fn.split('-')
    if not l[-1].endswith('.html'): raise ValueError
    l[-1] = l[-1][:-5]
    return [int(i) for i in l[1:]]

  return cmp(listify(a),
             listify(b))

with open(join(ROOT_PATH, 'index.html'), 'w') as outfile:

  copy(join(SRC_PATH, 'head.html'))

  for slidefile in sorted(glob(join(SRC_PATH, "slide*.html")), fncmp):
    copy(slidefile)

  copy(join(SRC_PATH, 'tail.html'))

