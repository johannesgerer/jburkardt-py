#!/bin/bash
#
python disk_grid_test.py > disk_grid_test_output.txt
if [ $? -ne 0 ]; then
  echo "Errors running disk_grid_test.py"
  exit
fi
#
rm *.pyc
#
echo "Test program output written to disk_grid_test_output.txt."
