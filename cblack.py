#!/usr/bin/python3
# -*- coding: utf-8 -*-
import re
import sys

import black

__version__ = '0.9.1'

_orgLineStr = black.Line.__str__
_orgFixDocString = black.fix_docstring

def lineStrIndentTwoSpaces(self) -> str:
  """ Intended to replace Line.__str__ to produce 2-space indentation blocks
  instead of the 4 by default.
  """
  original = _orgLineStr(self)
  if not original.startswith(' '):
    return original

  noLeftSpaces   = original.lstrip(' ')
  nLeadingSpaces = len(original) - len(noLeftSpaces)

  # reindent by generating half the spaces (from 4-space blocks to 2-space blocks)
  reindented = '%s%s' % (' ' * (nLeadingSpaces >> 1), noLeftSpaces)
  return reindented

def fixDocString(docstring, prefix):
  """ Indent doc strings by 2 spaces instead of 4
  """
  return _orgFixDocString(docstring, ' ' * (len(prefix) >> 1))

black.Line.__str__ = lineStrIndentTwoSpaces
black.fix_docstring = fixDocString

def main ():
  # behabe like normal black code
  sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
  sys.exit(black.main())

if __name__ == '__main__':
  sys.exit(main())
