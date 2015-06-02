#!/bin/bash
#
python rnglib_test.py > rnglib_test_output.txt
if [ $? -ne 0 ]; then
  echo "Errors running rnglib_test.py"
  exit
fi
#
rm *.pyc
#
echo "Test program output written to rnglib_test_output.txt."
