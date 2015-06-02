#!/bin/bash
#
python circle_arc_grid_test.py > circle_arc_grid_test_output.txt
if [ $? -ne 0 ]; then
  echo "Errors running circle_arc_grid_test.py"
  exit
fi
#
rm *.pyc
#
echo "Test program output written to circle_arc_grid_test_output.txt."
