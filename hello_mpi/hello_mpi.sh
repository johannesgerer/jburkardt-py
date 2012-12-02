#!/bin/bash
#
mpirun -np 4 python hello_mpi.py >& hello_mpi_output.txt
#
echo " "
echo "The hello_mpi example has been run."

