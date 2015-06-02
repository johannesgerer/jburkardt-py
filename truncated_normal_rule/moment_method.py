#!/usr/bin/env python
#
def moment_method ( n, moments ):

#*****************************************************************************80
#
## MOMENT_METHOD computes a quadrature rule by the method of moments.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    23 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Gene Golub, John Welsch,
#    Calculation of Gaussian Quadrature Rules,
#    Mathematics of Computation,
#    Volume 23, Number 106, April 1969, pages 221-230.
#
#  Parameters:
#
#    Input, integer N, the order of the quadrature rule.
#
#    Input, real MOMENTS(2*N+1), moments 0 through 2*N.
#
#    Output, real X(N), W(N), the points and weights of the quadrature rule.
#
  import numpy as np

  debug = False

  if ( debug ):
    r8vec_print ( 2 * n + 1, moments, '  Moments:' )
#
#  Define the N+1 by N+1 Hankel matrix H(I,J) = moment(I+J).
#
  h = np.zeros ( ( n + 1, n + 1 ) )

  for i in range ( 0, n + 1 ):
    for j in range ( 0, n + 1 ):
      h[i,j] = moments[i+j]

  if ( debug ):
    r8mat_print ( n + 1, n + 1, h, '  Hankel matrix H:' )
#
#  Compute R, the upper triangular Cholesky factor of H.
#
  r = np.linalg.cholesky ( h )
  r = np.transpose ( r )

  if ( debug ):
    r8mat_print ( n + 1, n + 1, r, '  Upper triangular Cholesky factor R:' )
#
#  Compute ALPHA and BETA from R, using Golub and Welsch's formula.
#
  alpha = np.zeros ( n )

  alpha[0] = r[0,1] / r[0,0]
  for i in range ( 1, n ):
    alpha[i] = r[i,i+1] / r[i,i] - r[i-1,i] / r[i-1,i-1]

  beta = np.zeros ( n - 1 )
  for i in range ( 0, n - 1 ):
    beta[i] = r[i+1,i+1] / r[i,i]
#
#  Set up the tridiagonal Jacobi matrix.
#
  jacobi = np.diag ( alpha, k = 0 ) \
         + np.diag ( beta, k = -1 ) \
         + np.diag ( beta, k = +1 )

  if ( debug ):
    r8mat_print ( n, n, jacobi, '  Jacobi matrix: ' )
#
#  Get the eigendecomposition of the Jacobi matrix.
#
  x, eigvec = np.linalg.eig ( jacobi )

  w = np.zeros ( n )
  for j in range ( 0, n ):
    w[j] = moments[0] * ( float ( eigvec[0,j] ) ) ** 2
#
#  Sort X, and W accordingly.
#
  for j in range ( 0, n ):
    for i in range ( j + 1, n ):
      if ( x[i] < x[j] ):
        t = x[i]
        x[i] = x[j]
        x[j] = t
        t = w[i]
        w[i] = w[j]
        w[j] = t 

  return x, w

def moment_method_test ( ):

#*****************************************************************************80
#
## MOMENT_METHOD_TEST tests MOMENT_METHOD.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    23 March 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  from normal_01_moment import normal_01_moment

  print ''
  print 'MOMENT_METHOD_TEST'
  print '  MOMENT_METHOD uses the method of moments for a quadrature rule.'

  n = 5
  tnp1 = 2 * n + 1
  
  moments = np.zeros ( tnp1 )

  for i in range ( 0, tnp1 ):
    moments[i] = normal_01_moment ( i )

  x, w = moment_method ( n, moments )

  x_correct = np.array ( [ \
    [ -2.85697001387280565416230426401 ], \
    [ -1.35562617997426586583052129087 ], \
    [  0.0 ], \
    [ +1.35562617997426586583052129087 ], \
    [ +2.85697001387280565416230426401 ] ] )

  w_correct = np.array ( [ \
    [ 0.0112574113277206889333702151856 ], \
    [ 0.222075922005612644399963118148 ], \
    [ 0.533333333333333333333333333333 ], \
    [ 0.222075922005612644399963118148 ], \
    [ 0.0112574113277206889333702151856 ] ] )

  print ''
  print '           Computed        Correct'
  print '   I           X              X'
  print ''
  for i in range ( 0, n ):
    print '  %2d  %14.6g  %14.6g' % ( i, x[i], x_correct[i] )

  print ''
  print '           Computed        Correct'
  print '   I           W              W'
  print ''
  for i in range ( 0, n ):
    print '  %2d  %14.6g  %14.6g' % ( i, w[i], w_correct[i] )


#
#  Terminate.
#
  print ''
  print 'MOMENT_METHOD_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  moment_method_test ( )
  timestamp ( )
