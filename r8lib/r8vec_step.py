#!/usr/bin/env python
#
def r8vec_step ( x0, n, x ):

#*****************************************************************************80
#
## R8VEC_STEP evaluates a unit step function.
#
#  Discussion:
#
#    F(X) = 0 if X < X0
#           1 if     X0 <= X
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    30 May 2013
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real X0, the location of the jump.
#
#    Input, integer N, the number of argument values.
#
#    Output, real X(N), the arguments.
#
#    Output, real FX(N), the function values.
#
  import numpy

  fx = numpy.zeros ( n );

  for i in range ( 0, n ):
    if ( x < x0 ):
      fx[i] = 0.0
    else
      fx[i] = 1.0

  return fx

