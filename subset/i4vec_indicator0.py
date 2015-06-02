#!/usr/bin/env python

def i4vec_indicator0 ( n ):

#*****************************************************************************80
#
## I4VEC_INDICATOR0 sets an I4VEC to the indicator vector ( 0, 1, 2, ... ).
#
#  Discussion:
#
#    An I4VEC is a vector of I4's.
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
#    Output, integer A(N), the indicator array.
#
  import numpy

  a = numpy.zeros ( n );

  for i in range ( 0, n ):
    a[i] = i

  return a

def i4vec_indicator0_test ( ):

#*****************************************************************************80
#
## I4VEC_INDICATOR0_TEST tests I4VEC_INDICATOR0.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 November 2014
#
#  Author:
#
#    John Burkardt
#
  from i4vec_print import i4vec_print

  print ''
  print 'I4VEC_INDICATOR0_TEST'
  print '  I4VEC_INDICATOR0 returns an indicator vector.'

  n = 10
  a = i4vec_indicator0 ( n )
  i4vec_print ( n, a, '  The indicator0 vector:' )
#
#  Terminate.
#
  print ''
  print 'I4VEC_INDICATOR0_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  i4vec_indicator0_test ( )
  timestamp ( )
