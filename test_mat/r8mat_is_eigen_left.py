#!/usr/bin/env python

def r8mat_is_eigen_left ( n, k, a, x, lam ):

#*****************************************************************************80
#
## R8MAT_IS_EIGEN_LEFT determines the error in a left eigensystem.
#
#  Discussion:
#
#    An R8MAT is a matrix of real values.
#
#    This routine computes the Frobenius norm of
#
#      X * A - LAMBDA * X
#
#    where
#
#      A is an N by N matrix,
#      X is an K by N matrix (each of K columns is an eigenvector)
#      LAMBDA is a K by K diagonal matrix of eigenvalues.
#
#    This routine assumes that A, X and LAMBDA are all real.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    17 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the order of the matrix.
#
#    Input, integer K, the number of eigenvectors.
#    K is usually 1 or N.
#
#    Input, real A(N,N), the matrix.
#
#    Input, real X(K,N), the K eigenvectors.
#
#    Input, real LAM(K), the K eigenvalues.
#
#    Output, real VALUE, the Frobenius norm of X * A - LAM * X.
#
  from r8mat_mm import r8mat_mm
  from r8mat_norm_fro import r8mat_norm_fro

  c = r8mat_mm ( k, n, n, x, a )

  for i in range ( 0, k ):
    for j in range ( 0, n ):
      c[i,j] = c[i,j] - lam[i] * x[i,j]

  value = r8mat_norm_fro ( k, n, c )

  return value

def r8mat_is_eigen_left_test ( ):

#*****************************************************************************80
#
## R8MAT_IS_EIGEN_LEFT_TEST tests R8MAT_IS_EIGEN_LEFT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    11 March 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  from r8mat_print import r8mat_print
  from r8vec_print import r8vec_print
#
#  This is the CARRY ( 4.0, 4 ) matrix.
#
  m = 4
  n = m
  a = np.array ( [ \
   [ 0.13671875,   0.60546875,   0.25390625,   0.00390625 ], \
   [ 0.05859375,   0.52734375,   0.39453125,   0.01953125 ], \
   [ 0.01953125,   0.39453125,   0.52734375,   0.05859375 ], \
   [ 0.00390625,   0.25390625,   0.60546875,   0.13671875 ] ] )

  k = 4
  x = np.array ( [ \
    [  1.0,     1.0,     1.0,     1.0 ], \
    [ 11.0,     3.0,    -1.0,    -3.0 ], \
    [ 11.0,    -3.0,    -1.0,     3.0 ], \
    [  1.0,    -1.0,     1.0,    -1.0 ] ] )

  lam = np.array ( [ \
     1.000000000000000, \
     0.250000000000000, \
     0.062500000000000, \
     0.015625000000000 ] )

  print ''
  print 'R8MAT_IS_EIGEN_LEFT_TEST:'
  print '  R8MAT_IS_EIGEN_LEFT tests the error in the left eigensystem'
  print '    A\' * X - X * LAMBDA = 0'

  r8mat_print ( n, n, a, '  Matrix A:' )
  r8mat_print ( n, k, x, '  Eigenmatrix X:' )
  r8vec_print ( n, lam, '  Eigenvalues LAM:' )

  value = r8mat_is_eigen_left ( n, k, a, x, lam )

  print ''
  print '  Frobenius norm of A\'*X-X*LAMBDA is %g' % ( value )

  print ''
  print 'R8MAT_IS_EIGEN_LEFT_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8mat_is_eigen_left_test ( )
  timestamp ( )
