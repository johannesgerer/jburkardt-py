#!/bin/bash
#
python r8lib_test.py > r8lib_test_output.txt
if [ $? -ne 0 ]; then
  echo "Errors running r8lib_test.py"
  exit
fi
#
rm *.pyc
#
echo "Test program output written to r8lib_test_output.txt."
