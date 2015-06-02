#!/usr/bin/env python

def i4mat_max ( m, n, a ):

#*****************************************************************************80
#
## I4MAT_MAX returns the largest value in an I4MAT.
#
#  Discussion:
#
#    An I4MAT is an M by N array of I4's.
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
#    Input, integer M, N, the number of rows and columns.
#
#    Input, integer A(M,N), the matrix.
#
#    Output, integer VALUE, the largest of the entries.
#
  i4_huge = 2147483647
  value = - i4_huge

  for j in range ( 0, n ):
    for i in range ( 0, m ):
      value = max ( value, a[i,j] )

  return value

def i4mat_max_test ( ):

#*****************************************************************************80
#
## I4MAT_MAX_TEST tests I4MAT_MAX.
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
  from i4mat_print import i4mat_print
  from i4mat_uniform_ab import i4mat_uniform_ab

  print ''
  print 'I4MAT_MAX_TEST'
  print '  For an I4MAT:'
  print '  I4MAT_MAX returns the maximum entry.'

  m = 5
  n = 7
  a = 0
  b = 10
  seed = 123456789
  x, seed = i4mat_uniform_ab ( m, n, a, b, seed )

  i4mat_print ( m, n, x, '  The matrix:' )
  
  x_max = i4mat_max ( m, n, x )

  print ''
  print '  Maximum entry = %d' % ( x_max )
#
#  Terminate.
#
  print ''
  print 'I4MAT_MAX_TEST'
  print '  Normal_end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  i4mat_max_test ( )
  timestamp ( )
