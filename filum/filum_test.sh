#!/bin/bash
#
python filum_test.py > filum_test_output.txt
if [ $? -ne 0 ]; then
  echo "Errors running filum_test.py"
  exit
fi
#
rm *.pyc
#
echo "Output written to filum_test_output.txt."
