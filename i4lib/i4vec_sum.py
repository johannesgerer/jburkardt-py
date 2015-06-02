#!/usr/bin/env python

def i4vec_sum ( n, a ):

#*****************************************************************************80
#
## I4VEC_SUM sums the entries of an I4VEC.
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
#    29 September 2014
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
#    Output, integer VALUE, the sum of the entries.
#
  value = 0

  for i in range ( 0, n ):
    value = value + a[i]

  return value

def i4vec_sum_test ( ):

#*****************************************************************************80
#
## I4VEC_SUM_TEST tests I4VEC_SUM.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 October 2014
#
#  Author:
#
#    John Burkardt
#
  from i4vec_print import i4vec_print
  from i4vec_uniform_ab import i4vec_uniform_ab

  print ''
  print 'I4VEC_SUM_TEST'
  print '  I4VEC_SUM sums the entries of an I4VEC.'

  n = 5
  lo = 0
  hi = 10
  seed = 123456789
  a, seed = i4vec_uniform_ab ( n, lo, hi, seed )
  i4vec_print ( n, a, '  The vector:' )

  s = i4vec_sum ( n, a )
  print ''
  print '  The vector entries sum to %d' % ( s )
#
#  Terminate.
#
  print ''
  print 'I4VEC_SUM_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  i4vec_sum_test ( )
  timestamp ( )

