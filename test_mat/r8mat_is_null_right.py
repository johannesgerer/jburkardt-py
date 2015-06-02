#!/usr/bin/env python

def r8mat_is_null_right ( m, n, a, x ):

#*****************************************************************************80
#
## R8MAT_IS_NULL_RIGHT determines if x is a right null vector of matrix A.
#
#  Discussion:
#
#    The nonzero N vector x is a right null vector of the MxN matrix A if
#
#      A * x = 0
#
#    If A is a square matrix, then this implies that A is singular.
#
#    If A is a square matrix, this implies that 0 is an eigenvalue of A,
#    and that x is an associated eigenvector.
#
#    This routine returns 0 if x is exactly a right null vector of A.
#
#    It returns a "huge" value if x is the zero vector.
#
#    Otherwise, it returns the L2 norm of A * x divided by the L2 norm of x:
#
#      ERROR_L2 = NORM_L2 ( A * x ) / NORM_L2 ( x )
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
#    Input, integer M, N, the row and column dimensions of 
#    the matrix.  M and N must be positive.
#
#    Input, real A(M,N), the matrix.
#
#    Input, real X(N), the vector.
#
#    Output, real VALUE, the result.
#    0.0 indicates that X is exactly a null vector.
#    A "huge" value indicates that ||x|| = 0;
#    Otherwise, the value returned is a relative error ||A*x||/||x||.
#
  from r8mat_mv import r8mat_mv
  from r8vec_norm_l2 import r8vec_norm_l2
#
#  X_NORM
#
  x_norm = r8vec_norm_l2 ( n, x )
#
#  AX = A*X
#
  ax = r8mat_mv ( m, n, a, x )
#
#  AX_NORM
#
  ax_norm = r8vec_norm_l2 ( m, ax )
#
#  Value
#
  value = ax_norm / x_norm

  return value

def r8mat_is_null_right_test ( ):

#*****************************************************************************80
#
## R8MAT_IS_NULL_RIGHT_TEST tests R8MAT_IS_NULL_RIGHT.
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

  m = 3
  n = 3
  a = np.array ( [ \
    [ 1.0, 2.0, 3.0 ], \
    [ 4.0, 5.0, 6.0 ], \
    [ 7.0, 8.0, 9.0 ] ])
  x = np.array ( [ 1.0, -2.0, 1.0 ] )

  print ''
  print 'R8MAT_IS_NULL_RIGHT_TEST:'
  print '  R8MAT_IS_NULL_RIGHT tests whether the N vector X'
  print '  is a right null vector of A, that is, A*x=0.'

  r8mat_print ( m, n, a, '  Matrix A:' )
  r8vec_print ( n, x, '  Vector X:' )

  enorm = r8mat_is_null_right ( m, n, a, x )

  print ''
  print '  Frobenius norm of A*x is %g' % ( enorm )

  print ''
  print 'R8MAT_IS_NULL_RIGHT_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8mat_is_null_right_test ( )
  timestamp ( )
