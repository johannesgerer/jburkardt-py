#!/bin/bash
#
python triangle01_integrals_test.py > triangle01_integrals_test_output.txt
if [ $? -ne 0 ]; then
  echo "Errors running triangle01_integrals_test.py"
  exit
fi
#
rm *.pyc
#
echo "Test program output written to triangle01_integrals_test_output.txt."
