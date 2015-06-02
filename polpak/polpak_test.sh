#!/bin/bash
#
python polpak_test.py > polpak_test_output.txt
if [ $? -ne 0 ]; then
  echo "Errors running polpak_test.py"
  exit
fi
#
rm *.pyc
#
echo "Test program output written to polpak_test_output.txt."
