#!/bin/bash
#
python triangle_integrals_test.py > triangle_integrals_test_output.txt
if [ $? -ne 0 ]; then
  echo "Errors running triangle_integrals_test.py"
  exit
fi
#
rm *.pyc
#
echo "Test program output written to triangle_integrals_test_output.txt."
