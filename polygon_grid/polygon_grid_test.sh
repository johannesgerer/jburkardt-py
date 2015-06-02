#!/bin/bash
#
python polygon_grid_test.py > polygon_grid_test_output.txt
if [ $? -ne 0 ]; then
  echo "Errors running polygon_grid_test.py"
  exit
fi
#
rm *.pyc
#
echo "Test program output written to polygon_grid_test_output.txt."
