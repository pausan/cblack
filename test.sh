#!/bin/bash

# Very simple test. It formats the "unformatted.py" file into "reformatted.py"
# and checks if it looks the same as "expected.py"

set -e

err_report() {
  echo "ERROR: Test failed. Unexpected formatting, have a look at the diff"
}

trap 'err_report' ERR

cat "test/unformatted.py" | python3 cblack.py -q - > test/reformatted.py

diff test/expected.py test/reformatted.py

echo "Test Succeeded!"
exit 0
