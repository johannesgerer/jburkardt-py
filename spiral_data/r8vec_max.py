#!/usr/bin/env python
#
def r8vec_max ( n, a ):

#*****************************************************************************80
#
## R8VEC_MAX returns the maximum value in an R8VEC.
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
#    09 March 2015
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
#    Output, real VALUE, the maximum value in the vector.
#
  r8_huge = 1.79769313486231571E+308

  value = - r8_huge
  for i in range ( 0, n ):
    if ( value < a[i] ):
      value = a[i]

  return value

def r8vec_max_test ( ):

#*****************************************************************************80
#
## R8VEC_MAX_TEST tests R8VEC_MAX.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    15 January 2015
#
#  Author:
#
#    John Burkardt
#
  from r8vec_print import r8vec_print
  from r8vec_uniform_ab import r8vec_uniform_ab

  print ''
  print 'R8VEC_MAX_TEST'
  print '  R8VEC_MAX computes the maximum entry in an R8VEC.'

  n = 10
  a_lo = - 10.0
  a_hi = + 10.0
  seed = 123456789

  a, seed = r8vec_uniform_ab ( n, a_lo, a_hi, seed )

  r8vec_print ( n, a, '  Input vector:' )

  value = r8vec_max ( n, a )
  print ''
  print '  Max = %g' % ( value )

  print ''
  print 'R8VEC_MAX_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8vec_max_test ( )
  timestamp ( )

