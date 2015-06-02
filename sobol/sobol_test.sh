#!/bin/bash
#
python sobol_test.py > sobol_test_output.txt
if [ $? -ne 0 ]; then
  echo "Errors running sobol_test.py"
  exit
fi
#
rm *.pyc
#
echo "Test program output written to sobol_test_output.txt."
