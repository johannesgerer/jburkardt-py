#!/bin/bash
#
mpirun -np 4 python prime_mpi.py >& prime_mpi_output.txt
#
echo " "
echo "The prime_mpi example has been run."

