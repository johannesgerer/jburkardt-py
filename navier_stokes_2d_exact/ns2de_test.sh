#!/bin/bash
#
python ns2de_test.py > ns2de_test_output.txt
if [ $? -ne 0 ]; then
  echo "Errors running ns2de_test.py"
  exit
fi
#
rm *.pyc
#
echo "Test program output written to ns2de_test_output.txt."
