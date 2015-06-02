#!/usr/bin/env python

def r8mat_mv ( m, n, a, x ):

#*****************************************************************************80
#
## R8MAT_MV multiplies a matrix times a vector.
#
#  Discussion:
#
#    In FORTRAN90, this operation can be more efficiently carried
#    out by the command
#
#      Y(1:M) = MATMUL ( A(1:M,1:N), X(1:N) )
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    31 August 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, N, the number of rows and columns of the matrix.
#
#    Input, real A(M,N), the M by N matrix.
#
#    Input, real X(N), the vector to be multiplied by A.
#
#    Output, real Y(M), the product A*X.
#
  import numpy as np

  y = np.zeros ( m )

  for j in range ( 0, n ):
    for i in range ( 0, m ):
      y[i] = y[i] + a[i,j] * x[j]

  return y

def r8mat_mv_test ( ):

#*****************************************************************************80
#
## R8MAT_MV_TEST tests R8MAT_MV.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    31 August 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  from r8mat_print import r8mat_print
  from r8vec_print import r8vec_print

  m = 4
  n = 2

  a = np.array \
  ( \
    ( ( 1.0, 1.0 ), \
    ( 2.0, 1.0 ), \
    ( 3.0, 1.0 ), \
    ( 4.0, 1.0 ) ) \
  )
 
  x = np.array ( ( 1.0, 2.0 ) )

  print ''
  print 'R8MAT_MV_TEST'
  print '  R8MAT_MV computes a matrix-vector product b = A * x;'

  b = r8mat_mv ( m, n, a, x )

  r8mat_print ( m, n, a, '  A:' )
  r8vec_print ( n, x, '  X:' )
  r8vec_print ( m, b, '  B = A*X:' )

  print ''
  print 'R8MAT_MV_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8mat_mv_test ( )
  timestamp ( )
