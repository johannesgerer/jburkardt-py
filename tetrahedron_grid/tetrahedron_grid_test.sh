#!/bin/bash
#
python tetrahedron_grid_test.py > tetrahedron_grid_test_output.txt
if [ $? -ne 0 ]; then
  echo "Errors running tetrahedron_grid_test.py"
  exit
fi
#
rm *.pyc
#
echo "Test program output written to tetrahedron_grid_test_output.txt."
