#! /usr/bin/env python
#
def jacobi ( m, n ):

#*****************************************************************************80
#
## JACOBI returns the JACOBI matrix.
#
#  Formula:
#
#    if ( J = I - 1 )
#      A(I,J) = 0.5 * sqrt ( ( 4 * J^2 ) / ( 4 * J^2 - 1 ) )
#    else if ( J = I + 1 )
#      A(I,J) = 0.5 * sqrt ( ( 4 * (J-1)^2 ) / ( 4 * (J-1)^2 - 1 ) )
#    else
#      A(I,J) = 0
#
#  Example:
#
#    M = 4, N = 4
#
#    0            0.577350269  0            0
#    0.577350269  0            0.516397779  0
#    0            0.516397779  0            0.507092553
#    0            0            0.507092553  0
#
#  Properties:
#
#    A is symmetric: A' = A.
#
#    Because A is symmetric, it is normal.
#
#    Because A is normal, it is diagonalizable.
#
#    A has a zero diagonal.
#
#    The eigenvalues of A are the zeros of the Legendre polynomial
#    of degree N.  They lie symmetrically in [-1,1], and are also
#    the nodes of Gauss-Legendre quadrature.  For the case of N = 4,
#    these eigenvalues are
#
#      [ -0.861136312, -0.339981044, +0.339981044, +0.861136312 ].
#
#    It follows that A is singular when N is odd.
#
#    The J-th Gauss-Legendre weight is twice the square of the first
#    component of the J-th eigenvector of A.  For the case of N = 4,
#    the eigenvector matrix is:
#
#      -0.417046     -0.571028     -0.571028    0.417046
#       0.622037      0.336258     -0.336258    0.622038
#      -0.571028      0.417046      0.417046    0.571028
#       0.336258     -0.622037      0.622038    0.336258
#
#    and the corresponding weights are
#
#      [ 0.347854845, 0.652145155, 0.652145155, 0.347854845 ]
#
#    The family of matrices is nested as a function of N.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    16 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Lloyd Trefethen, David Bau,
#    Numerical Linear Algebra,
#    SIAM, 1997, pages 287-292.
#
#  Parameters:
#
#    Input, integer M, N, the number of rows and columns of A.
#
#    Output, real A(M,N), the matrix.
#
  import numpy as np

  a = np.zeros ( ( m, n ) )

  for i in range ( 0, m ):
    for j in range ( 0, n ):

      if ( j == i - 1 ):
        a[i,j] = 0.5 * np.sqrt ( float ( 4 * ( j + 1 ) ** 2 ) \
                               / float ( 4 * ( j + 1 ) ** 2 - 1 ) )
      elif ( j == i + 1 ):
        a[i,j] = 0.5 * np.sqrt ( float ( 4 * j ** 2 ) \
                               / float ( 4 * j ** 2 - 1 ) )

  return a

def jacobi_determinant ( n ):

#*****************************************************************************80
#
## JACOBI_DETERMINANT returns the determinant of the JACOBI matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    16 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the order of the matrix.
#
#    Output, real VALUE, the determinant.
#
  import numpy as np
  from legendre_zeros import legendre_zeros

  if ( ( n % 2 ) == 1 ):
  
    value = 0.0;
    
  else:
  
    lam = legendre_zeros ( n )
  
    value = np.prod ( lam )

  return value

def jacobi_determinant_test ( ):

#*****************************************************************************80
#
## JACOBI_DETERMINANT_TEST tests JACOBI_DETERMINANT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    16 February 2015
#
#  Author:
#
#    John Burkardt
#
  from jacobi import jacobi
  from r8mat_print import r8mat_print
 
  print ''
  print 'JACOBI_DETERMINANT_TEST'
  print '  JACOBI_DETERMINANT computes the determinant of the JACOBI matrix.'
  print ''

  m = 4
  n = m

  a = jacobi ( m, n )
  r8mat_print ( m, n, a, '  JACOBI matrix:' )

  value = jacobi_determinant ( n )

  print ''
  print '  Value =  %g' % ( value )

  print ''
  print 'JACOBI_DETERMINANT_TEST'
  print '  Normal end of execution.'

  return

def jacobi_inverse ( n ):

#*****************************************************************************80
#
## JACOBI_INVERSE returns the inverse of the JACOBI matrix.
#
#  Discussion:
#
#    This inverse is related to that of the CLEMENT2 matrix.
#
#  Example:
#
#    N = 6
#
#         0    1.7321         0   -1.7638         0    1.7689
#    1.7321         0         0         0         0         0
#         0         0         0    1.9720         0   -1.9777
#   -1.7638         0    1.9720         0         0         0
#         0         0         0         0         0    1.9900
#    1.7689         0   -1.9777         0    1.9900         0
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    12 April 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the order of the matrix.
#    N must be even.
#
#    Output, real A(N,N), the matrix.
#
  import numpy as np
  from sys import exit

  if ( ( n % 2 ) == 1 ):
    print ''
    print 'JACOBI_INVERSE - Fatal error!'
    print '  The Jacobi matrix is singular for odd N.'
    exit ( 'JACOBI_INVERSE - Fatal error!' )

  a = np.zeros ( ( n, n ) )

  for i in range ( 0, n ):

    if ( ( i % 2 ) == 0 ):

      p = 1.0

      for j in range ( i, n - 1, 2 ):

        a1 = 0.5 * np.sqrt ( float ( 4 * ( j + 1 ) * ( j + 1 ) ) \
          / float ( 4 * ( j + 1 ) * ( j + 1 ) - 1 ) )
        a2 = 0.5 * np.sqrt ( float ( 4 * j * j ) \
          / float ( 4 * j * j - 1 ) )

        if ( j == i ):
          p = p / a1
        else:
          p = - p * a2 / a1
 
        a[i,j+1] = p
        a[j+1,i] = p

  return a

def jacobi_test ( ):

#*****************************************************************************80
#
## JACOBI_TEST tests JACOBI.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    16 February 2015
#
#  Author:
#
#    John Burkardt
#
  from r8mat_print import r8mat_print

  print ''
  print 'JACOBI_TEST'
  print '  JACOBI computes the JACOBI matrix.'

  m = 4
  n = m

  a = jacobi ( m, n )
  r8mat_print ( m, n, a, '  JACOBI matrix:' )

  print ''
  print 'JACOBI_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  jacobi_test ( )
  timestamp ( )
