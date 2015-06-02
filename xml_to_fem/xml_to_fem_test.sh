#!/bin/bash
#
python xml_to_fem.py > xml_to_fem_test_output.txt
if [ $? -ne 0 ]; then
  echo "Errors running xml_to_fem.py"
  exit
fi
#
rm *.pyc
#
echo "Output written to xml_to_fem_test_output.txt."
