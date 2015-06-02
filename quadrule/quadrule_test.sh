#!/bin/bash
#
python quadrule_test.py > quadrule_test_output.txt
if [ $? -ne 0 ]; then
  echo "Errors running quadrule_test.py"
  exit
fi
#
rm *.pyc
#
echo "Test program output written to quadrule_test_output.txt."
