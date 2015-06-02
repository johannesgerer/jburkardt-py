#!/usr/bin/env python

def r8mat_norm_l1 ( m, n, a ):

#*****************************************************************************80
#
## R8MAT_NORM_L1 returns the matrix L1 norm of an R8MAT.
#
#  Discussion:
#
#    The matrix L1 norm is defined as:
#
#      value = max ( 1 <= J <= N ) sum ( 1 <= I <= M ) abs ( A(I,J) ).
#
#    The matrix L1 norm is derived from the vector L1 norm, and
#    satisifies:
#
#      vec_norm_l1 ( A * x ) <= mat_norm_l1 ( A ) * vec_norm_l1 ( x ).
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    05 December 2014
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
#    Input, real A(M,N), the matrix whose norm is desired.
#
#    Output, real VALUE, the norm of A.
#
  value = 0.0

  for j in range ( 0, n ):
    row_sum = 0.0
    for i in range ( 0, m ):
      row_sum = row_sum + abs ( a[i,j] )
    value = max ( value, row_sum )

  return value

def r8mat_norm_l1_test ( ):

#*****************************************************************************80
#
## R8MAT_NORM_L1_TEST tests R8MAT_NORM_L1.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    04 December 2014
#
#  Author:
#
#    John Burkardt
#
  from r8mat_print import r8mat_print
  from r8mat_uniform_ab import r8mat_uniform_ab

  m = 5
  n = 4
  x1 = -5.0
  x2 = +5.0
  seed = 123456789

  a, seed = r8mat_uniform_ab ( m, n, x1, x2, seed )
  
  for j in range ( 0, n ):
    for i in range ( 0, m ):
      a[i,j] = round ( a[i,j] )

  print ''
  print 'R8MAT_NORM_L1_TEST'
  print '  R8MAT_NORM_L1 computes the L1 norm of an R8MAT;'

  t = r8mat_norm_l1 ( m, n, a )

  r8mat_print ( m, n, a, '  A:' )
  print ''
  print '  Computed L1 norm = %g' % ( t )

  print ''
  print 'R8MAT_NORM_L1_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8mat_norm_l1_test ( )
  timestamp ( )
