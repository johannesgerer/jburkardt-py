#!/bin/bash
#
python test_values_test.py > test_values_test_output.txt
if [ $? -ne 0 ]; then
  echo "Errors running test_values_test.py"
  exit
fi
#
rm *.pyc
#
echo "Test program output written to test_values_test_output.txt."
