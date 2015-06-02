#!/usr/bin/env python
#
def r8vec_norm_l0 ( n, a ):

#*****************************************************************************80
#
## R8VEC_NORM_L0 returns the l0 "norm" of an R8VEC.
#
#  Discussion:
#
#    An R8VEC is a vector of R8's.
#
#    The l0 "norm" simply counts the number of nonzero entries in the vector.
#    It is not a true norm, but has some similarities to one.  It is useful
#    in the study of compressive sensing.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 January 2015
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
#    Output, real VALUE, the value of the norm.
#
  value = 0.0
  for i in range ( 0, n ):
    if ( a[i] != 0.0 ):
      value = value + 1.0

  return value

def r8vec_norm_l0_test ( ):

#*****************************************************************************80
#
## R8VEC_NORM_L0_TEST tests R8VEC_NORM_L0.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 January 2015
#
#  Author:
#
#    John Burkardt
#
  from r8vec_nint import r8vec_nint
  from r8vec_print import r8vec_print
  from r8vec_uniform_ab import r8vec_uniform_ab

  print ''
  print 'R8VEC_NORM_L0_TEST'
  print '  R8VEC_NORM_L0 computes the L0 "norm" of an R8VEC.'

  n = 10
  a_lo = - 2.0
  a_hi = + 2.0
  seed = 123456789

  a, seed = r8vec_uniform_ab ( n, a_lo, a_hi, seed )
  a = r8vec_nint ( n, a )

  r8vec_print ( n, a, '  Input vector:' )

  value = r8vec_norm_l0 ( n, a )
  print ''
  print '  L0 norm = %g' % ( value )
#
#  Terminate.
#
  print ''
  print 'R8VEC_NORM_L0_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8vec_norm_l0_test ( )
  timestamp ( )

