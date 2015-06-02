#!/bin/bash
#
python wtime_test.py > wtime_test_output.txt
if [ $? -ne 0 ]; then
  echo "Errors running wtime_test.py"
  exit
fi
#
rm *.pyc
#
echo "Test program output written to wtime_test_output.txt."
