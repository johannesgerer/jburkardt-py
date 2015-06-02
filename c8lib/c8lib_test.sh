#!/bin/bash
#
python c8lib_test.py > c8lib_test_output.txt
if [ $? -ne 0 ]; then
  echo "Errors running c8lib_test.py"
  exit
fi
#
rm *.pyc
#
echo "Test program output written to c8lib_test_output.txt."
