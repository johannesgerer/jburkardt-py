#!/bin/bash
#
python fem1d_heat_explicit_test.py > fem1d_heat_explicit_test_output.txt
if [ $? -ne 0 ]; then
  echo "Errors running fem1d_heat_explicit_test.py"
  exit
fi
#
rm *.pyc
#
echo "Test program output written to fem1d_heat_explicit_test_output.txt."
