#!/bin/bash
#
python ellipse_grid_test.py > ellipse_grid_test_output.txt
if [ $? -ne 0 ]; then
  echo "Errors running ellipse_grid_test.py"
  exit
fi
#
rm *.pyc
#
echo "Test program output written to ellipse_grid_test_output.txt."
