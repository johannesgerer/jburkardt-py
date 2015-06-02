#!/bin/bash
#
python bvec_test.py > bvec_test_output.txt
if [ $? -ne 0 ]; then
  echo "Errors running bvec_test.py"
  exit
fi
#
rm *.pyc
#
echo "Test program output written to bvec_test_output.txt."
