#!/bin/bash

# Very simple test. It formats the "$1_unformatted.py" file into "$1_reformatted.py"
# and checks if it looks the same as "$1_expected.py"

set -e

PYTHON_VERSION=$1

err_report() {
  echo "ERROR: Test failed. Unexpected formatting, have a look at the diff"
}

trap 'err_report' ERR

if tty --quiet; then
  # enable debugging with [PuDB](https://youtu.be/bJYkCWPs_UU)
  export PUDB_TTY
  PUDB_TTY="$(tty)"
fi

PYTHON_VERSION2="$(python3 -c 'if True:
    import sys
    major, minor = sys.version_info[:2]
    print(major, minor, sep=".")
')"

if [[ $PYTHON_VERSION != $PYTHON_VERSION2 ]]; then
  echo >&2 \
    "wrong python version! (found $PYTHON_VERSION2 expected $PYTHON_VERSION)" \
  exit 1
fi

cat "test/${PYTHON_VERSION}_unformatted.py" | python3 cblack.py -q - > test/${PYTHON_VERSION}_reformatted.py

diff -u --color=always test/${PYTHON_VERSION}_expected.py test/${PYTHON_VERSION}_reformatted.py

echo "Test ${PYTHON_VERSION} Succeeded!"
exit 0
