#!/bin/bash
#
python function_args.py > function_args_test_output.txt
if [ $? -ne 0 ]; then
  echo "Errors running function_args_test.py"
  exit
fi
#
rm *.pyc
#
echo "Test program output written to function_args_test_output.txt."
