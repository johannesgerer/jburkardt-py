#!/usr/bin/env python

def i4vec_amax ( n, a ):

#*****************************************************************************80
#
## I4VEC_AMAX returns the largest magnitude in an I4VEC.
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
#    Output, integer VALUE, the largest of the magnitudes of the entries.
#
  i4_huge = 2147483647
  value = - i4_huge

  for i in range ( 0, n ):
    value = max ( value, abs ( a[i] ) )

  return value

def i4vec_amax_test ( ):

#*****************************************************************************80
#
## I4VEC_AMAX_TEST tests I4VEC_AMAX.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    29 September 2014
#
#  Author:
#
#    John Burkardt
#
  from i4vec_print import i4vec_print
  from i4vec_uniform_ab import i4vec_uniform_ab

  print ''
  print 'I4VEC_AMAX_TEST'
  print '  I4VEC_AMAX computes the largest of the magnitudes of the'
  print '  entries of an I4VEC.'

  n = 10
  lo = - 10
  hi = 5
  seed = 123456789

  a, seed = i4vec_uniform_ab ( n, lo, hi, seed )
  i4vec_print ( n, a, '  Vector A:' )
  a_amax = i4vec_amax ( n, a )
  print ''
  print '  Largest magnitude of entries of A = %d' % ( a_amax )
#
#  Terminate.
#
  print ''
  print 'I4VEC_AMAX_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  i4vec_amax_test ( )
  timestamp ( )
