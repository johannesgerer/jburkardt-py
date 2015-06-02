#! /usr/bin/env python
#
def fourier_sine ( n ):

#*****************************************************************************80
#
## FOURIER_SINE returns the FOURIER_SINE matrix.
#
#  Discussion:
#
#    This is the discrete Fourier Sine Transform matrix.
#
#    This matrix is occasionally known as the "Newman" matrix.
#
#  Formula:
#
#    A(I,J) = sqrt ( 2 / (N+1) ) * SIN ( I * J * PI / (N+1) )
#
#  Example:
#
#    N = 5
#
#     0.288675     0.5    0.577350    0.5    0.288675
#     0.5          0.5    0.0        -0.5   -0.5
#     0.577350     0.0   -0.577350    0.0    0.577350
#     0.5         -0.5    0.0         0.5   -0.5
#     0.288675    -0.5    0.577350   -0.5    0.288675
#
#  Properties:
#
#    A is symmetric: A' = A.
#
#    Because A is symmetric, it is normal.
#
#    Because A is normal, it is diagonalizable.
#
#    A is orthogonal: A' * A = A * A' = I.
#
#    A is involutional: A * A = I.
#
#    A is generally not positive definite.
#
#    All eigenvalues of A have absolute value 1.
#
#    A is the eigenvector matrix of the second difference matrix (-1,2,-1).
#
#    A can be used to compute the Discrete Fourier Sine Transform of
#    a set of data X,
#       DFST ( X ) = A * X
#    A second multiplication by A recovers the original data.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    05 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Robert Gregory, David Karney,
#    Example 3.11,
#    A Collection of Matrices for Testing Computational Algorithms,
#    Wiley, New York, 1969, page 41, 
#    LC: QA263.G68.
#
#    Nicholas Higham, Desmond Higham,
#    Large growth factors in Gaussian elimination with pivoting,
#    SIAM Journal on Matrix Analysis and Applications,
#    Volume 10, 1989, pages 155-164.
#
#    Joan Westlake,
#    Test Matrix A7,
#    A Handbook of Numerical Matrix Inversion and Solution of Linear Equations,
#    John Wiley, 1968.
#
#  Parameters:
#
#    Input, integer N, the order of A.
#
#    Output, real A(N,N), the matrix.
#
  import numpy as np

  a = np.zeros ( ( n, n ) )

  s = np.sqrt ( 2.0 / float ( n + 1 ) )

  for i in range ( 0, n ):
    for j in range ( 0, n ):
      angle = float ( ( i + 1 ) * ( j + 1 ) ) * np.pi / float ( n + 1 )
      a[i,j] = np.sin ( angle ) * s

  return a

def fourier_sine_determinant ( n ):

#*****************************************************************************80
#
## FOURIER_SINE_DETERMINANT returns the determinant of the FOURIER_SINE matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    05 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the order of the matrix.
#
#    Output, real DETERM, the determinant.
#
  if ( ( n % 2 ) == 1 ):
    value = + 1.0
  else:
    value = -1.0

  return value

def fourier_sine_determinant_test ( ):

#*****************************************************************************80
#
## FOURIER_SINE_DETERMINANT_TEST tests FOURIER_SINE_DETERMINANT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    05 February 2015
#
#  Author:
#
#    John Burkardt
#
  from fourier_sine import fourier_sine
  from r8mat_print import r8mat_print

  print ''
  print 'FOURIER_SINE_DETERMINANT_TEST'
  print '  FOURIER_SINE_DETERMINANT computes the determinant of the FOURIER_SINE matrix.'
  print ''

  m = 5
  n = m

  a = fourier_sine ( n )
  r8mat_print ( m, n, a, '  FOURIER_SINE matrix:' )

  value = fourier_sine_determinant ( n )

  print ''
  print '  Value =  %g' % ( value )

  print ''
  print 'FOURIER_SINE_DETERMINANT_TEST'
  print '  Normal end of execution.'

  return

def fourier_sine_inverse ( n ):

#*****************************************************************************80
#
## FOURIER_SINE_INVERSE returns the inverse of the FOURIER_SINE matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the order of the matrix.
#
#    Output, real A(N,N), the matrix.
#
  a = fourier_sine ( n )

  return a

def fourier_sine_test ( ):

#*****************************************************************************80
#
## FOURIER_SINE_TEST tests FOURIER_SINE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    04 February 2015
#
#  Author:
#
#    John Burkardt
#
  from r8mat_print import r8mat_print

  print ''
  print 'FOURIER_SINE_TEST'
  print '  FOURIER_SINE computes the FOURIER_SINE matrix.'

  m = 5
  n = m

  a = fourier_sine ( n )
  r8mat_print ( m, n, a, '  FOURIER_SINE matrix:' )

  print ''
  print 'FOURIER_SINE_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  fourier_sine_test ( )
  timestamp ( )
