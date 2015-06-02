#!/bin/bash
#
python sphere_llq_grid_test.py > sphere_llq_grid_test_output.txt
if [ $? -ne 0 ]; then
  echo "Errors running sphere_llq_grid_test.py"
  exit
fi
#
rm *.pyc
#
echo "Test program output written to sphere_llq_grid_test_output.txt."
