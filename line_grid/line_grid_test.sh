#!/bin/bash
#
python line_grid_test.py > line_grid_test_output.txt
if [ $? -ne 0 ]; then
  echo "Errors running line_grid_test.py"
  exit
fi
#
rm *.pyc
#
echo "Test program output written to line_grid_test_output.txt."
