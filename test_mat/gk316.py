#! /usr/bin/env python
#
def gk316 ( n ):

#*****************************************************************************80
#
## GK316  returns the GK316 matrix.
#
#  Discussion:
#
#    GK316 is a Gregory and Karney test matrix.
#
#  Formula:
#
#    if ( I == N )
#      A(I,J) = J
#    elseif ( J == N )
#      A(I,J) = I
#    elseif ( I == J )
#      A(I,J) = 1.0
#    else
#      A(I,J) = 0.0
#
#  Example:
#
#    N = 5
#
#     1  0  0  0  1
#     0  1  0  0  2
#     0  0  1  0  3
#     0  0  0  1  4
#     1  2  3  4  5
#
#  Properties:
#
#    A is symmetric: A' = A.
#
#    Because A is symmetric, it is normal.
#
#    Because A is normal, it is diagonalizable.
#
#    A has property A (the first set is 1:N-1, the second is just N).
#
#    A is integral: int ( A ) = A.
#
#    det ( A ) = - N * ( N + 1 ) * ( 2 * N - 5 ) / 6.
#
#    N-2 eigenvalues are equal to 1, while the remaining eigenvalues
#    are the roots of X^2 - (N+1)*X - N*(N+1)*(2*N-5)/6 = 0.
#
#    A is border-banded.
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
#  Reference:
#
#    Aegerter,
#    Construction of a Set of Test Matrices,
#    Communications of the ACM,
#    Volume 2, Number 8, 1959, pages 10-12.
#
#    Robert Gregory, David Karney,
#    Example 3.16, Example 4.15,
#    A Collection of Matrices for Testing Computational Algorithms,
#    Wiley, New York, 1969, page 44, page 74,
#    LC: QA263.G68.
#
#  Parameters:
#
#    Input, integer N, the order of A.
#
#    Output, real A(N,N), the matrix.
#
  import numpy as np

  a = np.zeros ( ( n, n ) )

  for i in range ( 0, n ):
    for j in range ( 0, n ):
      if ( i == n - 1 ):
        a[i,j] = float ( j + 1 )
      elif ( j == n - 1 ):
        a[i,j] = float ( i + 1 )
      elif ( i == j ):
        a[i,j] = 1.0

  return a

def gk316_determinant ( n ):

#*****************************************************************************80
#
## GK316_DETERMINANT computes the determinant of the GK316 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 February 2015
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
  value = - float ( n * ( n + 1 ) * ( 2 * n - 5 ) ) / 6.0

  return value

def gk316_determinant_test ( ):

#*****************************************************************************80
#
## GK316_DETERMINANT_TEST tests GK316_DETERMINANT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 February 2015
#
#  Author:
#
#    John Burkardt
#
  from gk316 import gk316
  from r8mat_print import r8mat_print

  print ''
  print 'GK316_DETERMINANT_TEST'
  print '  GK316_DETERMINANT computes the GK316 determinant.'

  m = 5
  n = m
 
  a = gk316 ( n )

  r8mat_print ( m, n, a, '  GK316 matrix:' )

  value = gk316_determinant ( n )

  print '  Value =  %g' % ( value )

  print ''
  print 'GK316_DETERMINANT_TEST'
  print '  Normal end of execution.'

  return

def gk316_inverse ( n ):

#*****************************************************************************80
#
## GK316_INVERSE returns the inverse of the GK316 matrix.
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
#    Input, integer N, the order of A.
#
#    Output, real A(N,N), the matrix.
#
  import numpy as np

  a = np.zeros ( ( n, n ) )

  t = 6.0 / float ( n * ( n + 1 ) * ( 2 * n - 5 ) )

  for i in range ( 0, n ):
    for j in range ( 0, n ):
 
      if ( i == j and i < n - 1 ):
        a[i,j] = 1.0 - t * float ( ( i + 1 ) * ( i + 1 ) )
      elif ( i == j and i == n - 1 ):
        a[i,j] = - t
      elif ( i < n - 1 and j < n - 1 ):
        a[i,j] = - t * float ( ( i + 1 ) * ( j + 1 ) )
      elif ( i == n - 1 ):
        a[i,j] = t * float ( j + 1 )
      elif ( j == n - 1 ):
        a[i,j] = t * float ( i + 1 )

  return a

def gk316_test ( ):

#*****************************************************************************80
#
## GK316_TEST tests GK316.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 February 2015
#
#  Author:
#
#    John Burkardt
#
  from r8mat_print import r8mat_print

  print ''
  print 'GK316_TEST'
  print '  GK316 computes the GK316 matrix.'

  m = 5
  n = m

  a = gk316 ( n )
 
  r8mat_print ( m, n, a, '  GK316 matrix:' )

  print ''
  print 'GK316_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  gk316_test ( )
  timestamp ( )
