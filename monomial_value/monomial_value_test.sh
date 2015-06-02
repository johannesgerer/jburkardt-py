#!/bin/bash
#
python monomial_value_test.py > monomial_value_test_output.txt
if [ $? -ne 0 ]; then
  echo "Errors running monomial_value_test.py"
  exit
fi
#
rm *.pyc
#
echo "Test program output written to monomial_value_test_output.txt."
