#!/usr/bin/python3

# -*- coding: utf-8 -*-
import re
import sys

from black import main as blackMain, Line

__version__ = '0.9'

_orgLineStr = Line.__str__

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

Line.__str__ = lineStrIndentTwoSpaces


def main ():
  # behabe like normal black code
  sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
  sys.exit(blackMain())

if __name__ == '__main__':
  sys.exit(main())
