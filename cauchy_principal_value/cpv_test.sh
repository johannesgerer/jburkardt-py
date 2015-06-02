#!/bin/bash
#
python cpv_test.py > cpv_test_output.txt
if [ $? -ne 0 ]; then
  echo "Errors running cpv_test.py"
  exit
fi
#
rm *.pyc
#
echo "Test program output written to cpv_test_output.txt."
