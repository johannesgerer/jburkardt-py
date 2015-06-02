#!/bin/bash
#
python hypercube_grid_test.py > hypercube_grid_test_output.txt
if [ $? -ne 0 ]; then
  echo "Errors running hypercube_grid_test.py"
  exit
fi
#
rm *.pyc
#
echo "Test program output written to hypercube_grid_test_output.txt."
