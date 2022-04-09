""" This file will be used as a test. We will run cblack on this file and
compare against expected.py file. If they match, we are good. If not, we have
to see if the change is produced by a change in black behaviour and thus, update
expected.py or the difference is due to a bug in our code.

Feel free to grow this file with more use-cases and update expected.py
accordingly.
"""

from x import (
  a,
  b,
  c,
)


A_GLOBAL_SET = {
  # a comment
  # another comment
  "a string",
  "another string",
  # another comment
  "yet another string",
}


def lookAtThisMethod(
  first_parameter,
  second_paramter=None,
  third_parameter=32,
  fourth_parameter="a short string as default argument",
  **kwargs
):
  """The point of this is see how it reformats parameters

  It might be fun to see what goes on

    Here I guess it should respect this spacing, since we are in a comment.

  We are done!
  """
  return kwargs["whatever"](
    first_parameter * third_parameter,
    second_paramter,
    fourth_parameter,
    "extra string because I want to",
  )


def main():
  """Hoo.

  Wat.
  """
  if len(argv) > 1:
    raise app.UsageError("Too many command-line arguments.")

  x = (
    "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa "
    "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb"
  )

  y = [
    1,
    2,
    [
      3,
    ],
  ]

  z = {
    "another": "map",
    "of": 3,
    "values": [
      12345678,
      12345678,
      12345678,
      12345678,
      12345678,
      12345678,
      12345678,
      12345678,
    ],
  }


if __name__ == "__main__":
  exit(main())
