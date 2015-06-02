#!/bin/bash
#
python timer_test.py > timer_test_output.txt
if [ $? -ne 0 ]; then
  echo "Errors running timer_test.py"
  exit
fi
#
rm *.pyc
#
echo "Test program output written to timer_test_output.txt."
