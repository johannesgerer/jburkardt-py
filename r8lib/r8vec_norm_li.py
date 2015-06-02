#!/usr/bin/env python
#
def r8vec_norm_li ( n, a ):

#*****************************************************************************80
#
## R8VEC_NORM_LI returns the loo norm of an R8VEC.
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
#    19 February 2015
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
    if ( value < abs ( a[i] ) ):
      value = abs ( a[i] )

  return value

def r8vec_norm_li_test ( ):

#*****************************************************************************80
#
## R8VEC_NORM_LI_TEST tests R8VEC_NORM_LI.
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
  from r8vec_nint import r8vec_nint
  from r8vec_print import r8vec_print
  from r8vec_uniform_ab import r8vec_uniform_ab

  print ''
  print 'R8VEC_NORM_LI_TEST'
  print '  R8VEC_NORM_LI computes the Loo norm of an R8VEC.'

  n = 10
  r8_lo = - 5.0
  r8_hi = + 5.0
  seed = 123456789

  a, seed = r8vec_uniform_ab ( n, r8_lo, r8_hi, seed )

  r8vec_print ( n, a, '  Input vector:' )

  value = r8vec_norm_li ( n, a )
  print ''
  print '  Loo norm = %g' % ( value )
#
#  Terminate.
#
  print ''
  print 'R8VEC_NORM_LI_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8vec_norm_li_test ( )
  timestamp ( )

