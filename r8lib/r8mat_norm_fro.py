#!/usr/bin/env python

def r8mat_norm_fro ( m, n, a ):

#*****************************************************************************80
#
## R8MAT_NORM_FRO returns the Frobenius norm of an R8MAT.
#
#  Discussion:
#
#    The Frobenius norm is defined as
#
#      value = sqrt ( sum ( 1 <= I <= M ) sum ( 1 <= j <= N ) A(I,J)^2 )
#
#    The matrix Frobenius norm is not derived from a vector norm, but
#    is compatible with the vector L2 norm, so that:
#
#      vec_norm_l2 ( A * x ) <= mat_norm_fro ( A ) * vec_norm_l2 ( x ).
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
#  Parameters:
#
#    Input, integer M, the number of rows in A.
#
#    Input, integer N, the number of columns in A.
#
#    Input, real A(M,N), the matrix whose Frobenius
#    norm is desired.
#
#    Output, real VALUE, the Frobenius norm of A.
#
  from math import sqrt

  value = sqrt ( sum ( sum ( a ** 2 ) ) )

  return value

def r8mat_norm_fro_test ( ):

#*****************************************************************************80
#
## R8MAT_NORM_FRO_TEST tests R8MAT_NORM_FRO.
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
  import numpy as np
  from r8mat_print import r8mat_print
  from math import sqrt

  m = 5
  n = 4

  a = np.zeros ( ( m, n ) )

  k = 0
  t1 = 0.0

  for i in range ( 0, m ):
    for j in range ( 0, n ):
      k = k + 1
      a[i,j] = k
      t1 = t1 + k * k

  t1 = sqrt ( t1 )

  print ''
  print 'R8MAT_NORM_FRO_TEST'
  print '  R8MAT_NORM_FRO computes the Frobenius norm of an R8MAT;'

  t2 = r8mat_norm_fro ( m, n, a )

  r8mat_print ( m, n, a, '  A:' )
  print ''
  print '  Expected Frobenius norm = %g' % ( t1 )
  print '  Computed Frobenius norm = %g' % ( t2 )

  print ''
  print 'R8MAT_NORM_FRO_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8mat_norm_fro_test ( )
  timestamp ( )
