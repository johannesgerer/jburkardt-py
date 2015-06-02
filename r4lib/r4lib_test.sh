#!/bin/bash
#
python r4lib_test.py > r4lib_test_output.txt
if [ $? -ne 0 ]; then
  echo "Errors running r4lib_test.py"
  exit
fi
#
rm *.pyc
#
echo "Test program output written to r4lib_test_output.txt."
