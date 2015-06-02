#!/bin/bash
#
python s2de_test.py > s2de_test_output.txt
if [ $? -ne 0 ]; then
  echo "Errors running s2de_test.py"
  exit
fi
#
rm *.pyc
#
echo "Test program output written to s2de_test_output.txt."
