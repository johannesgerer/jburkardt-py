#!/usr/bin/env python

def c8vec_nint ( n, c ):

#*****************************************************************************80
#
## C8VEC_NINT rounds the entries of a C8VEC.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    28 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of values to compute.
#
#    Input, complex C(N), the vector.
#
#    Output, complex C(N), the rounded vector.
#
  from c8_nint import c8_nint

  for i in range ( 0, n ):
    c[i] = c8_nint ( c[i] )

  return c

def c8vec_nint_test ( ):

#*****************************************************************************80
#
## C8VEC_NINT_TEST tests C8VEC_NINT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    28 February 2015
#
#  Author:
#
#    John Burkardt
#
  from c8vec_print import c8vec_print
  from c8vec_uniform_01 import c8vec_uniform_01

  print ''
  print 'C8VEC_NINT_TEST'
  print '  C8VEC_NINT rounds a C8VEC.'

  n = 5
  seed = 123456789
  [ c, seed ] = c8vec_uniform_01 ( n, seed )

  s = 5.0 + 3.0j
  for i in range ( 0, n ):
    c[i] = s * c[i]

  c8vec_print ( n, c, '  The initial vector:' )

  a = c8vec_nint ( n, c )

  c8vec_print ( n, c, '  The rounded vector:' )

  print ''
  print 'C8VEC_NINT_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  c8vec_nint_test ( )
  timestamp ( )


