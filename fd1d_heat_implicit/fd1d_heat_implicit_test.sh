#!/bin/bash
#
python fd1d_heat_implicit_test.py > fd1d_heat_implicit_test_output.txt
if [ $? -ne 0 ]; then
  echo "Errors running fd1d_heat_implicit_test.py"
  exit
fi
#
rm *.pyc
#
echo "Test program output written to fd1d_heat_implicit_test_output.txt."
