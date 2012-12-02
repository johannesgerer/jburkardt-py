#!/bin/bash
#
mpirun -np 4 python quad_mpi.py >& quad_mpi_output.txt
#
echo " "
echo "The quad_mpi example has been run."

