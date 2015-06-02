#!/bin/bash
#
python polynomial_test.py > polynomial_test_output.txt
if [ $? -ne 0 ]; then
  echo "Errors running polynomial_test.py"
  exit
fi
#
rm *.pyc
#
echo "Test program output written to polynomial_test_output.txt."
