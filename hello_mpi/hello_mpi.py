#!/usr/bin/env python

import sys
from mpi4py import MPI

comm = MPI.COMM_WORLD

id = comm.Get_rank()

p = comm.Get_size()

if id == 0:
  print ""
  print "HELLO_MPI:"
  print "  There are ", p, " MPI processes running."

print "Hello, world, from process ", id, "!"

