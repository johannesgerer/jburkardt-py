#!/usr/bin/env python

def r8mat_transpose ( m, n, a ):

#*****************************************************************************80
#
## R8MAT_TRANSPOSE transposes an R8MAT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    02 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, N, the number of rows and columns of A.
#
#    Input, real A(M,N), the matrix to be transposed.
#
#    Output, real AT(N,M), the transposed matrix.
#
  import numpy as np

  at = np.zeros ( ( n, m ) )

  for j in range ( 0, n ):
    for i in range ( 0, m ):
      at[j,i] = a[i,j]

  return at

def r8mat_transpose_test ( ):

#*****************************************************************************80
#
## R8MAT_TRANSPOSE_TEST tests R8MAT_TRANSPOSE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    02 March 2015
#
#  Author:
#
#    John Burkardt
#
  from r8mat_indicator import r8mat_indicator
  from r8mat_print import r8mat_print

  m = 5
  n = 4

  print ''
  print 'R8MAT_TRANSPOSE_TEST'
  print '  R8MAT_TRANSPOSE transposes an R8MAT.'

  a = r8mat_indicator ( m, n )
  r8mat_print ( m, n, a, '  Matrix A:' )

  at = r8mat_transpose ( m, n, a )
  r8mat_print ( n, m, at, '  Transposed matrix At:' )

  print ''
  print 'R8MAT_TRANSPOSE_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8mat_transpose_test ( )
  timestamp ( )
