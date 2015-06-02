#!/bin/bash
#
python c4lib_test.py > c4lib_test_output.txt
if [ $? -ne 0 ]; then
  echo "Errors running c4lib_test.py"
  exit
fi
#
rm *.pyc
#
echo "Test program output written to c4lib_test_output.txt."
