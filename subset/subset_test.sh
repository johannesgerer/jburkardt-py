#!/bin/bash
#
python subset_test.py > subset_test_output.txt
if [ $? -ne 0 ]; then
  echo "Errors running subset_test.py"
  exit
fi
#
rm *.pyc
#
echo "Test program output written to subset_test_output.txt."
