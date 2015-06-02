#!/bin/bash
#
python machine_test.py > machine_test_output.txt
if [ $? -ne 0 ]; then
  echo "Errors running machine_test.py"
  exit
fi
#
rm *.pyc
#
echo "Test program output written to machine_test_output.txt."
