#!/bin/bash
#
python cycle_floyd_test.py > cycle_floyd_test_output.txt
if [ $? -ne 0 ]; then
  echo "Errors running cycle_floyd_test.py"
  exit
fi
#
rm *.pyc
#
echo "Test program output written to cycle_floyd_test_output.txt."
