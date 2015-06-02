#!/bin/bash
#
python ellipsoid_grid_test.py > ellipsoid_grid_test_output.txt
if [ $? -ne 0 ]; then
  echo "Errors running ellipsoid_grid_test.py"
  exit
fi
#
rm *.pyc
#
echo "Test program output written to ellipsoid_grid_test_output.txt."
