#!/usr/bin/env python
#
def r8vec_nint ( n, a ):

#*****************************************************************************80
#
## R8VEC_NINT rounds entries of an R8VEC.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of entries in the vector.
#
#    Input, real A(N), the vector to be rounded.
#
#    Output, real A(N), the rounded vector.
#
  for i in range ( 0, n ):
    a[i] = round ( a[i] )

  return a

def r8vec_nint_test ( ):

#*****************************************************************************80
#
## R8VEC_NINT_TEST tests R8VEC_NINT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 December 2014
#
#  Author:
#
#    John Burkardt
#
  from r8vec_print import r8vec_print
  from r8vec_uniform_ab import r8vec_uniform_ab

  print ''
  print 'R8VEC_NINT_TEST'
  print '  R8VEC_NINT rounds an R8VEC.'

  n = 5
  x1 = -5.0
  x2 = +5.0
  seed = 123456789
  a, seed = r8vec_uniform_ab ( n, x1, x2, seed )
  r8vec_print ( n, a, '  Vector A:' )
  a = r8vec_nint ( n, a )
  r8vec_print ( n, a, '  Rounded vector A:' )
#
#  Terminate.
#
  print ''
  print 'R8VEC_NINT_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp

  timestamp ( )
  r8vec_nint_test ( )
  timestamp ( )
