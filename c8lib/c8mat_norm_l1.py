#!/usr/bin/env python

def c8mat_norm_l1 ( m, n, a ):

#*****************************************************************************80
#
## C8MAT_NORM_L1 returns the L1 norm of a C8MAT.
#
#  Discussion:
#
#    The L1 norm is defined as
#
#      C8MAT_NORM_L1 = max ( 1 <= J <= N )
#        sum ( 1 <= I <= M ) abs ( A(I,J) )
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    15 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, the number of rows in A.
#
#    Input, integer N, the number of columns in A.
#
#    Input, complex A(M,N), the matrix whose norm is desired.
#
#    Output, real VALUE, the norm of A.
#
  import numpy as np

  value = 0.0

  for j in range ( 0, n ):
    col_sum = 0.0
    for i in range ( 0, m ):
      col_sum = col_sum + abs ( a[i,j] )
    value = max ( value, col_sum )

  return value

def c8mat_norm_l1_test ( ):

#*****************************************************************************80
#
## C8MAT_NORM_L1_TEST tests C8MAT_NORM_L1.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    15 February 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  from c8mat_indicator import c8mat_indicator
  from c8mat_print import c8mat_print

  print ''
  print 'C8MAT_NORM_L1_TEST'
  print '  C8MAT_NORM_L1 computes the L1 norm of a C8MAT.'

  m = 5
  n = 4
  c = c8mat_indicator ( m, n )

  c8mat_print ( m, n, c, '  The Indicator matrix:' )

  value = c8mat_norm_l1 ( m, n, c )

  print ''
  print '  L1 norm = %g' % ( value )

  print ''
  print 'C8MAT_NORM_L1_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  c8mat_norm_l1_test ( )
  timestamp ( )

