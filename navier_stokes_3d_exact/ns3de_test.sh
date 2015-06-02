#!/bin/bash
#
python ns3de_test.py > ns3de_test_output.txt
if [ $? -ne 0 ]; then
  echo "Errors running ns3de_test.py"
  exit
fi
#
rm *.pyc
#
echo "Test program output written to ns3de_test_output.txt."
