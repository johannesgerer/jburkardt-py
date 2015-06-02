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
  from time import time, ctime
  from math import fabs

  a =  0.0
  b = 10.0
  n = 10000000
  exact = 0.49936338107645674464

  print ctime ( time ( ) )
  print ""
  print "QUAD_SERIAL:"
  print "  PYTHON version"
  print "  Estimate the integral of f(x) from A to B."
  print "  f(x) = 50 / ( pi * ( 2500 * x * x + 1 ) )."
  print ""
  print "  A        = ", a
  print "  B        = ", b
  print "  N        = ", n
  print "  Exact    = ", exact

  wtime = time ( )

  total = 0.0
  for i in range ( n ):
    x = ( ( n - i - 1 ) * a + ( i ) * b ) / ( n - 1 )
    total = total + f ( x )

  wtime = time ( ) - wtime

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

