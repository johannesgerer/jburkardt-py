#!/usr/bin/env python

def c8vec_norm_l1 ( n, c ):

#*****************************************************************************80
#
## C8VEC_NORM_L1 returns the L1 norm of a C8VEC.
#
#  Discussion:
#
#    The vector L1 norm is defined as:
#
#      C8VEC_NORM_L1 =  sum ( 1 <= I <= N ) abs ( A(I) ).
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    01 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of entries.
#
#    Input, complex C(N), the vector.
#
#    Output, real VALUE, the number.
#
  value = 0.0

  for i in range ( 0, n ):
    value = value + abs ( c[i] )

  return value

def c8vec_norm_l1_test ( ):

#*****************************************************************************80
#
## C8VEC_NORM_L1_TEST tests C8VEC_NORM_L1.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    01 March 2015
#
#  Author:
#
#    John Burkardt
#
  from c8vec_indicator import c8vec_indicator
  from c8vec_print import c8vec_print

  print ''
  print 'C8VEC_NORM_L1_TEST'
  print '  C8VEC_NORM_L1 computes the L1 norm of a C8VEC.'

  n = 5
  c = c8vec_indicator ( n )

  c8vec_print ( n, c, '  The indicator vector:' )

  value = c8vec_norm_l1 ( n, c )

  print ''
  print '  L1 norm = %g' % ( value )

  print ''
  print 'C8VEC_NORM_L1_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  c8vec_norm_l1_test ( )
  timestamp ( )


