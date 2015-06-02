#!/bin/bash
#
python lpp_test.py > lpp_test_output.txt
if [ $? -ne 0 ]; then
  echo "Errors running lpp_test.py"
  exit
fi
#
rm *.pyc
#
echo "Test program output written to lpp_test_output.txt."
