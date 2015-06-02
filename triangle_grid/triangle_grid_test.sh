#!/bin/bash
#
python triangle_grid_test.py > triangle_grid_test_output.txt
if [ $? -ne 0 ]; then
  echo "Errors running triangle_grid_test.py"
  exit
fi
#
rm *.pyc
#
echo "Test program output written to triangle_grid_test_output.txt."
