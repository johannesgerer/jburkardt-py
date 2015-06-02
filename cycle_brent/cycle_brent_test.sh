#!/bin/bash
#
python cycle_brent_test.py > cycle_brent_test_output.txt
if [ $? -ne 0 ]; then
  echo "Errors running cycle_brent_test.py"
  exit
fi
#
rm *.pyc
#
echo "Test program output written to cycle_brent_test_output.txt."
