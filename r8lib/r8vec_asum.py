#!/usr/bin/env python
#
def r8vec_asum ( n, a ):

#*****************************************************************************80
#
## R8VEC_ASUM sums the absolute values of the entries of an R8VEC.
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
#    24 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of entries in the vector.
#
#    Input, real A(N), the vector.
#
#    Output, real VALUE, the sum of the absolute values of the entries.
#
  value = 0.0
  for i in range ( 0, n ):
    value = value + abs ( a[i] )

  return value

def r8vec_asum_test ( ):

#*****************************************************************************80
#
## R8VEC_ASUM_TEST tests R8VEC_ASUM.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    24 January 2015
#
#  Author:
#
#    John Burkardt
#
  from r8vec_print import r8vec_print
  from r8vec_uniform_ab import r8vec_uniform_ab

  print ''
  print 'R8VEC_ASUM_TEST'
  print '  R8VEC_ASUM sums the absolute values of the entries in an R8VEC.'

  n = 10
  a_lo = - 10.0
  a_hi = + 10.0
  seed = 123456789

  a, seed = r8vec_uniform_ab ( n, a_lo, a_hi, seed )

  r8vec_print ( n, a, '  Input vector:' )

  value = r8vec_asum ( n, a )
  print ''
  print '  Sum of absolute values of entries = %g' % ( value )
#
#  Terminate.
#
  print ''
  print 'R8VEC_ASUM_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8vec_asum_test ( )
  timestamp ( )

