#!/bin/bash
#
python monomial_test.py > monomial_test_output.txt
if [ $? -ne 0 ]; then
  echo "Errors running monomial_test.py"
  exit
fi
#
rm *.pyc
#
echo "Test program output written to monomial_test_output.txt."
