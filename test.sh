#!/bin/bash

# Very simple test. It formats the "$1_unformatted.py" file into "$1_reformatted.py"
# and checks if it looks the same as "$1_expected.py"

set -e

PYTHON_VERSION=$1

err_report() {
  echo "ERROR: Test failed. Unexpected formatting, have a look at the diff"
}

trap 'err_report' ERR

cat "test/${PYTHON_VERSION}_unformatted.py" | python3 cblack.py -q - > test/${PYTHON_VERSION}_reformatted.py

diff -u --color=auto test/${PYTHON_VERSION}_expected.py test/${PYTHON_VERSION}_reformatted.py

echo "Test ${PYTHON_VERSION} Succeeded!"
exit 0
