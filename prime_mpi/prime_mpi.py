#!/usr/bin/env python
#

#*****************************************************************************80

def prime_mpi ( ):

#*****************************************************************************80
#
## PRIME_MPI counts the primes between N_LO and N_HI.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 October 2011
#
#  Author:
#
#    John Burkardt
#
  import numpy
  import sys
  from mpi4py import MPI
  from time import time, ctime

  comm = MPI.COMM_WORLD

  id = comm.Get_rank()

  p = comm.Get_size()

  n_lo = 1
  n_hi = 131072
  n_factor = 2

  if id == 0:
    wtime = MPI.Wtime ( )
    print ( ctime ( time ( ) ) )
    print ""
    print "PRIME_MPI"
    print "  Python/MPI version"
    print "  Count the primes between ", n_lo, "and", n_hi
    print ""
    print "  Use MPI to divide the computation among"
    print "  multiple processes."

  n = n_lo

  while n <= n_hi:

    primes = numpy.array ( 0, 'i' )
    wtime = MPI.Wtime ( )

    t = 0
    for i in range ( 2 + id, n + 1, id ):
      isprime = 1
      for j in range ( 2, i ):
        if ( i % j ) == 0:
          isprime = 0
          break
      t = t + isprime

    comm.Reduce ( [ t, MPI.DOUBLE ], [ primes, MPI.INT ], op = MPI.SUM, root = 0 )

    wtime = MPI.Wtime ( ) - wtime

    if id == 0:
      print "  ", n, "  ", primes, "  ", wtime

    n = n * n_factor
#
#  Terminate.
#
  print ""
  print "PRIME_MPI:"
  print "  Normal end of execution."
  print ""
  print ( ctime ( time ( ) ) )

#*****************************************************************************80

prime_mpi ( )

