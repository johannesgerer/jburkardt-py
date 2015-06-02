#!/bin/bash
#
python ball_grid_test.py > ball_grid_test_output.txt
if [ $? -ne 0 ]; then
  echo "Errors running ball_grid_test.py"
  exit
fi
#
rm *.pyc
#
echo "Test program output written to ball_grid_test_output.txt."
