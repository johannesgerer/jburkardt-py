#!/bin/bash
#
python truncated_normal_rule_test.py > truncated_normal_rule_test_output.txt
if [ $? -ne 0 ]; then
  echo "Errors running truncated_normal_rule_test.py"
  exit
fi
#
rm *.pyc
#
echo "Test program output written to truncated_normal_rule_test_output.txt."
