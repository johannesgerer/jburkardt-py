#!/bin/bash
#
python i4lib_test.py > i4lib_test_output.txt
if [ $? -ne 0 ]; then
  echo "Errors running i4lib_test.py"
  exit
fi
#
rm *.pyc
#
echo "Test program output written to i4lib_test_output.txt."
