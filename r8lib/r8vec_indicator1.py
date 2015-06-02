#!/usr/bin/env python
#
def r8vec_indicator1 ( n ):

#*****************************************************************************80
#
## R8VEC_INDICATOR1 sets an R8VEC to the indicator vector (1,2,3,...).
#
#  Discussion:
#
#    An R8VEC is a vector of R8's.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 September 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of elements of the vector.
#
#    Output, real A(N), the indicator array.
#
  import numpy

  a = numpy.zeros ( n );

  for i in range ( 0, n ):
    a[i] = i + 1

  return a

def r8vec_indicator1_test ( ):

#*****************************************************************************80
#
## R8VEC_INDICATOR1_TEST tests R8VEC_INDICATOR1.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    19 February 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  from r8vec_print import r8vec_print

  print ''
  print 'R8VEC_INDICATOR1_TEST'
  print '  R8VEC_INDICATOR1 returns the 1-based indicator matrix.'

  n = 10
  a = r8vec_indicator1 ( n )

  r8vec_print ( n, a, '  The 1-based indicator vector:' )
#
#  Terminate.
#
  print ''
  print 'R8VEC_INDICATOR1_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( ) 
  r8vec_indicator1_test ( )
  timestamp ( )

