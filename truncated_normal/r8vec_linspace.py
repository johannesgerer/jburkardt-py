#!/usr/bin/env python
#
def r8vec_linspace ( n, a, b ):

#*****************************************************************************80
#
## R8VEC_LINSPACE creates a column vector of linearly spaced values.
#
#  Discussion:
#
#    An R8VEC is a vector of R8's.
#
#    While MATLAB has the built in command 
#
#      x = linspace ( a, b, n )
#
#    that command has the distinct disadvantage of returning a ROW vector.
#
#    4 points evenly spaced between 0 and 12 will yield 0, 4, 8, 12.
#
#    In other words, the interval is divided into N-1 even subintervals,
#    and the endpoints of intervals are used as the points.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    02 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of entries in the vector.
#
#    Input, real A, B, the first and last entries.
#
#    Output, real X(N), a vector of linearly spaced data.
#
  import numpy as np

  x = np.zeros ( n )

  if ( n == 1 ):
    x[0] = ( a + b ) / 2.0
  else:
    for i in range ( 0, n ):
     x[i] = ( ( n - 1 - i ) * a \
            + (         i ) * b ) \
            / ( n - 1     )
 
  return x

def r8vec_linspace_test ( ):

#*****************************************************************************80
#
## R8VEC_LINSPACE_TEST tests R8VEC_LINSPACE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    02 January 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  from r8vec_print import r8vec_print

  print ''
  print 'R8VEC_LINSPACE_TEST'
  print '  R8VEC_LINSPACE returns evenly spaced values between A and B.'

  n = 5
  x_lo = 10.0
  x_hi = 20.0
  x = r8vec_linspace ( n, x_lo, x_hi )

  r8vec_print ( n, x, '  The linspace vector:' )

  print ''
  print 'R8VEC_LINSPACE_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( ) 
  r8vec_linspace_test ( )
  timestamp ( )
