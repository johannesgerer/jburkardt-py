#!/bin/bash
#
python simplex_grid_test.py > simplex_grid_test_output.txt
if [ $? -ne 0 ]; then
  echo "Errors running simplex_grid_test.py"
  exit
fi
#
rm *.pyc
#
echo "Test program output written to simplex_grid_test_output.txt."
