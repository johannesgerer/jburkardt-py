#!/bin/bash
#
python bellman_ford.py > bellman_ford_test_output.txt
if [ $? -ne 0 ]; then
  echo "Errors running bellman_ford_test.py"
  exit
fi
#
rm *.pyc
#
echo "Test program output written to bellman_ford_test_output.txt."
