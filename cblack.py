#!/usr/bin/python3
# -*- coding: utf-8 -*-
import contextlib
import re
import sys

__version__ = "22.3.0"

import sys
from os.path import isdir

import importlib
import importlib.abc
import importlib.util
import importlib.machinery


@contextlib.contextmanager
def prevent_metapath_recursion(cls):
  orig_meta_path = tuple(sys.meta_path)
  while cls in sys.meta_path:
    sys.meta_path.remove(cls)
  yield
  sys.meta_path[:] = orig_meta_path


class MonkeypatchEnablingBlackModuleFinder(importlib.abc.MetaPathFinder):
  """
  This custom module finder is used in order to prevent black to load a
  binary as the module, and load the pure-python module instead.

  This is done for the later black monkeypatching to work. Otherwise binaries
  cannot be patched.

  Reference:
    https://stupidpythonideas.blogspot.com/2015/06/hacking-python-without-hacking-python.html
  """

  @classmethod
  def find_spec(cls, fullname, path, target=None):
    """ """
    if fullname not in (
        # only need to monkeypatch those two modules
        "black.strings",
        "black.linegen",
        # segfault if we don't also pythonize the parent `black` module
        "black",
    ):
      return None

    # find what the spec "would have been" without this finder
    with prevent_metapath_recursion(cls):
      # I wasn't able to find a public api for this:
      spec = importlib._bootstrap._find_spec(fullname, path)

    if not (spec and spec.origin):
      # we only care if the other finders found a .so
      return spec

    # replace known dynamic loader module extensions by their "py" counterpart
    for ext in importlib.machinery.EXTENSION_SUFFIXES:
      if spec.origin.endswith(ext):

        py_path = spec.origin.replace(ext, ".py")

        # try to load & replace the spec from the .py path
        py_spec = importlib.util.spec_from_file_location(spec.name, py_path)
        if py_spec:
          return py_spec
    else:
      return spec


# override the usual module loaders with our own
sys.meta_path.insert(0, MonkeypatchEnablingBlackModuleFinder)

try:
  import black.strings as black_str
  import black.linegen as black_line
  from black import main as black_main
except ImportError:
  raise ImportError("Cannot import black. Have you installed black v%s?" % __version__)

_orgLineStr = black_line.Line.__str__
_orgFixDocString = black_str.fix_docstring
_orgBracketSplit = black_line.bracket_split_build_line


def lineStrIndentTwoSpaces(self) -> str:
  """Intended to replace Line.__str__ to produce 2-space indentation blocks
  instead of the 4 by default.
  """
  original = _orgLineStr(self)
  if not original.startswith(" "):
    return original

  noLeftSpaces = original.lstrip(" ")
  nLeadingSpaces = len(original) - len(noLeftSpaces)

  # reindent by generating half the spaces (from 4-space blocks to 2-space blocks)
  reindented = "%s%s" % (" " * (nLeadingSpaces >> 1), noLeftSpaces)
  return reindented


def fixDocString(docstring, prefix):
  """Indent doc strings by 2 spaces instead of 4"""
  return _orgFixDocString(docstring, " " * (len(prefix) >> 1))


def bracketSplitBuildLine(*args, is_body: bool = False, **kwargs):
  result = _orgBracketSplit(*args, **kwargs, is_body=is_body)
  if is_body:
    result.depth += 1
  return result


# Patch original black formatter function
black_line.Line.__str__ = lineStrIndentTwoSpaces
black_line.fix_docstring = fixDocString
black_line.bracket_split_build_line = bracketSplitBuildLine
black_str.fix_docstring = fixDocString


def main():
  # behabe like normal black code
  sys.argv[0] = re.sub(r"(-script\.pyw?|\.exe)?$", "", sys.argv[0])
  sys.exit(black_main())


if __name__ == "__main__":
  sys.exit(main())
