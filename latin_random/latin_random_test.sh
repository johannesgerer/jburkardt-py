#!/bin/bash
#
python latin_random.py > latin_random_test_output.txt
if [ $? -ne 0 ]; then
  echo "Errors running latin_random.py"
  exit
fi
#
rm *.pyc
#
echo "Test program output written to latin_random_test_output.txt."
