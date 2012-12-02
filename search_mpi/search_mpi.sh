#!/bin/sh
#
mpirun -np 4 python search_mpi.py >& search_mpi_output.txt
#
echo "The search_mpi script has been executed."
