#!/usr/bin/env python

def i4vec_max ( n, a ):

#*****************************************************************************80
#
## I4VEC_MAX returns the largest value in an I4VEC.
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
#    18 October 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of elements.
#
#    Input, integer A(N), the vector.
#
#    Output, integer VALUE, the largest of the entries.
#
  i4_huge = 2147483647
  value = - i4_huge

  for i in range ( 0, n ):
    value = max ( value, a[i] )

  return value

def i4vec_max_test ( ):

#*****************************************************************************80
#
## I4VEC_MAX_TEST tests I4VEC_MAX.
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
  from i4vec_uniform_ab import i4vec_uniform_ab

  print ''
  print 'I4VEC_MAX_TEST'
  print '  I4VEC_MAX returns the maximum entry in an I4VEC.'

  n = 10
  a = 1
  b = 30
  seed = 123456789
  x, seed = i4vec_uniform_ab ( n, a, b, seed )

  i4vec_print ( n, x, '  The vector:' )
  
  x_max = i4vec_max ( n, x )
 
  print ''
  print '  Maximum entry = %d' % ( x_max )
#
#  Terminate.
#
  print ''
  print 'I4VEC_MAX_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  i4vec_max_test ( )
  timestamp ( )
