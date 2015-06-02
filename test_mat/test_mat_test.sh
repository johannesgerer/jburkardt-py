#!/bin/bash
#
python test_mat_test.py > test_mat_test_output.txt
if [ $? -ne 0 ]; then
  echo "Errors running test_mat_test.py"
  exit
fi
#
rm *.pyc
#
echo "Test program output written to test_mat_test_output.txt."
