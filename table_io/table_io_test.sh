#!/bin/bash
#
python table_io_test.py > table_io_test_output.txt
if [ $? -ne 0 ]; then
  echo "Errors running table_io_test.py"
  exit
fi
#
rm *.pyc
#
echo "Output written to table_io_test_output.txt."
