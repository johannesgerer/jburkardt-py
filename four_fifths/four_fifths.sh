#!/bin/bash
#
python four_fifths.py > four_fifths_output.txt
if [ $? -ne 0 ]; then
  echo "Errors running four_fifths.py"
  exit
fi
#
rm *.pyc
#
echo "Test program output written to four_fifths_output.txt."
