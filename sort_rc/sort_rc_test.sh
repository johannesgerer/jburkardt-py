#!/bin/bash
#
python sort_rc_test.py > sort_rc_test_output.txt
if [ $? -ne 0 ]; then
  echo "Errors running sort_rc_test.py"
  exit
fi
#
rm *.pyc
#
echo "Test program output written to sort_rc_test_output.txt."
