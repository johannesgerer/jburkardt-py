#!/bin/bash
#
python pyramid_grid_test.py > pyramid_grid_test_output.txt
if [ $? -ne 0 ]; then
  echo "Errors running pyramid_grid_test.py"
  exit
fi
#
rm *.pyc
#
echo "Test program output written to pyramid_grid_test_output.txt."
