#!/bin/bash
#
python cube_grid_test.py > cube_grid_test_output.txt
if [ $? -ne 0 ]; then
  echo "Errors running cube_grid_test.py"
  exit
fi
#
rm *.pyc
#
echo "Test program output written to cube_grid_test_output.txt."
