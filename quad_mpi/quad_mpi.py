#!/usr/bin/env python
#
#*****************************************************************************80

def quad_serial ( ):

#*****************************************************************************80
#
## QUAD_SERIAL estimates an integral using a quadrature rule.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 October 2011
#
#  Author:
#
#    John Burkardt
#
  import numpy
  import sys
  from mpi4py import MPI
  from time import time, ctime
  from math import fabs

  comm = MPI.COMM_WORLD

  id = comm.Get_rank()

  p = comm.Get_size()

  a =  0.0
  b = 10.0
  exact = 0.49936338107645674464
#
#  Assume process 0 decides on the value of N, and 
#  must compute NP = N/P and send it to others.
#
  if id == 0:
    n = numpy.array ( 10000, dtype = 'i' )
    wtime = MPI.Wtime ( )
    print ( ctime ( time ( ) ) )
    print ""
    print "QUAD_MPI"
    print "  Python/MPI version"
    print "  Estimate an integral of f(x) from A to B."
    print "  f(x) = 50 / (pi * ( 2500 * x * x + 1 ) )"
    print ""
    print "  A        = ", a
    print "  B        = ", b
    print "  N        = ", n
    print "  Exact    = ", exact
    print ""
    print "  Use MPI to divide the computation among"
    print "  multiple processes."
  else:
    n = numpy.array ( 0, dtype = 'i' )

  comm.Bcast ( [ n, MPI.INT ], root = 0 )

  t = numpy.array ( 0.0, dtype = 'd' )
  for i in range ( id, n, p ):
    x = ( ( n - i - 1 ) * a + ( i ) * b ) / ( n - 1 )
    t = t + f ( x )

  print "  Sum for process ", id, " is ", t

  total = numpy.array ( 0.0, 'd' )

  comm.Reduce ( [ t, MPI.DOUBLE ], [ total, MPI.DOUBLE ], op = MPI.SUM, root = 0 )

  if id == 0:
    wtime = MPI.Wtime ( ) - wtime

    total = ( b - a ) * total / n
    error = fabs ( total - exact )
 
    print ""
    print "  Estimate = ", total
    print "  Error    = ", error
    print "  Time     = ", wtime
#
#  Terminate.
#
    print ""
    print "QUAD_SERIAL:"
    print "  Normal end of execution."
    print ""
    print ( ctime ( time ( ) ) )

#*****************************************************************************80

def f ( x ):

#*****************************************************************************80
#
## F evaluates the function.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 October 2012
#
#  Author:
#
#    John Burkardt
#
  pi = 3.141592653589793;
  value = 50.0 / ( pi * ( 2500.0 * x * x + 1.0 ) );

  return value

#*****************************************************************************80

quad_serial ( )

