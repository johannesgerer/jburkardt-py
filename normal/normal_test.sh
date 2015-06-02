#!/bin/bash
#
python normal_test.py > normal_test_output.txt
if [ $? -ne 0 ]; then
  echo "Errors running normal_test.py"
  exit
fi
#
rm *.pyc
#
echo "Test program output written to normal_test_output.txt."
