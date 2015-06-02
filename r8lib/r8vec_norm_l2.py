#!/usr/bin/env python
#
def r8vec_norm_l2 ( n, a ):

#*****************************************************************************80
#
## R8VEC_NORM_L2 returns the L2 norm of an R8VEC.
#
#  Discussion:
#
#    The vector L2 norm is defined as:
#
#      value = sqrt ( sum ( 1 <= I <= N ) A(I)^2 ).
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
#    Input, integer N, the number of entries in A.
#
#    Input, real A(N), the vector whose L2 norm is desired.
#
#    Output, real VALUE, the L2 norm of A.
#
  from math import sqrt

  value = 0.0
  for i in range ( 0, n ):
    value = value + a[i] * a[i]
  value = sqrt ( value )

  return value

def r8vec_norm_l2_test ( ):

#*****************************************************************************80
#
## R8VEC_NORM_L2_TEST tests R8VEC_NORM_L2.
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
  from r8vec_print import r8vec_print
  from r8vec_uniform_ab import r8vec_uniform_ab

  print ''
  print 'R8VEC_NORM_L2_TEST'
  print '  R8VEC_NORM_L2 computes the L2 norm of an R8VEC.'

  n = 10
  a_lo = - n
  a_hi = + n
  seed = 123456789
  a, seed = r8vec_uniform_ab ( n, a_lo, a_hi, seed )
  r8vec_print ( n, a, '  Input vector:' )
  a_norm = r8vec_norm_l2 ( n, a )

  print ''
  print '  L2 norm = %g' % ( a_norm )
#
#  Terminate.
#
  print ''
  print 'R8VEC_NORM_L2_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8vec_norm_l2_test ( )
  timestamp ( )
