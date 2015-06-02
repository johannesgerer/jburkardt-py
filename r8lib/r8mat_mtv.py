#!/usr/bin/env python

def r8mat_mtv ( m, n, a, x ):

#*****************************************************************************80
#
## R8MAT_MTV multiplies a tranposed matrix times a vector.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    07 March 2015
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
#    Input, real X(M), the vector to be multiplied by A'.
#
#    Output, real Y(N), the product A'*X.
#
  import numpy as np

  y = np.zeros ( n )

  for j in range ( 0, n ):
    for i in range ( 0, m ):
      y[j] = y[j] + x[i] * a[i,j]

  return y

def r8mat_mtv_test ( ):

#*****************************************************************************80
#
## R8MAT_MTV_TEST tests R8MAT_MTV.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    07 March 2015
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
 
  x = np.array ( ( 1.0, 2.0, 3.0, 4.0 ) )

  print ''
  print 'R8MAT_MTV_TEST'
  print '  R8MAT_MTV computes a matrix-vector product b = A\' * x;'

  b = r8mat_mtv ( m, n, a, x )

  r8mat_print ( m, n, a, '  A:' )
  r8vec_print ( m, x, '  X:' )
  r8vec_print ( n, b, '  B = A\'*X:' )

  print ''
  print 'R8MAT_MTV_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8mat_mtv_test ( )
  timestamp ( )
