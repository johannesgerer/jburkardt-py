#!/bin/bash
#
python fd1d_advection_lax_wendroff.py > fd1d_advection_lax_wendroff_output.txt
if [ $? -ne 0 ]; then
  echo "Errors running fd1d_advection_lax_wendroff.py"
  exit
fi
#
rm *.pyc
#
echo "Output written to fd1d_advection_lax_wendroff_output.txt."
