#!/bin/bash
#
python uniform_test.py > uniform_test_output.txt
if [ $? -ne 0 ]; then
  echo "Errors running uniform_test.py"
  exit
fi
#
rm *.pyc
#
echo "Test program output written to uniform_test_output.txt."
