#!/bin/bash
#
python square_grid_test.py > square_grid_test_output.txt
if [ $? -ne 0 ]; then
  echo "Errors running square_grid_test.py"
  exit
fi
#
rm *.pyc
#
echo "Test program output written to square_grid_test_output.txt."
