#! /usr/bin/env python

from os.path import dirname, realpath, abspath, join
from os import chdir, getcwd
from glob import glob
from re import search
from subprocess import check_output

ROOT_PATH = abspath(join(dirname(realpath(__file__)), '../..'))
SLIDES_PATH = join(ROOT_PATH, 'slidedeck')
SRC_PATH = join(SLIDES_PATH, 'src')
CODE_PATH = abspath(join(ROOT_PATH, 'code'))

def copy(infn):
  print 'copying ' + infn
  with open(infn) as infile:
    inlines = infile.readlines()
    outfile.writelines([do_macro(line) for line in inlines])
    outfile.write('\n')

def do_macro(line):

  m = search('\$LIST\((.+)\)', line)
  if m:
    return do_list(m.groups()[0])

  m = search('\$EXEC\((.+)\)', line)
  if m:
    return do_exec(m.groups()[0])

  return line

def get_div(precode):
  cssclass = 'terminal' if precode.count('\n') < 31 else 'terminal-scroll'
  return '''
      <div class="{}">
        <pre><code>{}</code></pre>
      </div>
  '''.format(
      cssclass,
      precode
      )


def do_list(arg):
  fn = join(CODE_PATH, arg)
  print 'inserting listing of {}'.format(fn)
  with open(fn) as listing:
    return get_div(listing.read())

def do_exec(arg):

  path, cmd = arg.split(',')
  cmd = cmd.strip()

  chdir(join(ROOT_PATH, path))

  print 'inserting results of "{}" executed in {}'.format(
      cmd,
      getcwd()
      )

  cmdargs = cmd.split(' ')

  return get_div('{}/ > {}\n\n{}'.format(
    path,
    cmd,
    check_output(cmdargs)
  ))

def fncmp(a, b):
  """
  cmp-return-compatible function that behaves such that
  'slide-1.html < <slide-2.html' < 'slide-10.html' < 'slide-10-1.html' etc.
  """

  def listify(fn):
    """
    given fn='slide-1-3-5.html', returns [1, 3, 5]
    """
    l = fn.split('-')
    if not l[-1].endswith('.html'): raise ValueError
    # strip 'slide-' and '.html'
    l[-1] = l[-1][:-5]
    return [int(i) for i in l[1:]]

  # builtin cmp does what we want with lists of ints
  return cmp(listify(a),
             listify(b))

with open(join(SLIDES_PATH, 'index.html'), 'w') as outfile:

  copy(join(SRC_PATH, 'head.html'))

  for slidefile in sorted(glob(join(SRC_PATH, "slide*.html")), fncmp):
    copy(slidefile)

  copy(join(SRC_PATH, 'tail.html'))

