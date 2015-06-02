#!/usr/bin/env python
#
def r8vec_indicator0 ( n ):

#*****************************************************************************80
#
## R8VEC_INDICATOR0 sets an R8VEC to the indicator vector (0,1,2,...).
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
    a[i] = i

  return a

def r8vec_indicator0_test ( ):

#*****************************************************************************80
#
## R8VEC_INDICATOR0_TEST tests R8VEC_INDICATOR0.
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
  import numpy as np
  from r8vec_print import r8vec_print

  print ''
  print 'R8VEC_INDICATOR0_TEST'
  print '  R8VEC_INDICATOR0 returns an indicator matrix.'

  n = 10
  a = r8vec_indicator0 ( n )

  r8vec_print ( n, a, '  The indicator0 vector:' )
#
#  Terminate.
#
  print ''
  print 'R8VEC_INDICATOR0_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( ) 
  r8vec_indicator0_test ( )
  timestamp ( )
