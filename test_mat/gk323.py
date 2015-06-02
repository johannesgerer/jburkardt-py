#! /usr/bin/env python
#
def gk323 ( m, n ):

#*****************************************************************************80
#
## GK323 returns the GK323 matrix, a Gregory and Karney test matrix.
#
#  Discussion:
#
#    This matrix is occasionally known as the "Todd" matrix.
#
#  Formula:
#
#    A(I,J) = abs ( I - J )
#
#  Example:
#
#    N = 5
#
#     0  1  2  3  4
#     1  0  1  2  3
#     2  1  0  1  2
#     3  2  1  0  1
#     4  3  2  1  0
#
#  Rectangular Properties:
#
#    A is integral: int ( A ) = A.
#
#    A is a special case of the Fiedler matrix.
#
#  Square Properties:
#
#    A is symmetric: A' = A.
#
#    Because A is symmetric, it is normal.
#
#    Because A is normal, it is diagonalizable.
#
#    det ( A ) = (-1)^(N-1) * 2^(N-2) * ( N - 1 ).
#
#    A has a dominant positive eigenvalue, and N-1 real negative eigenvalues.
#
#    If N = 2 mod 4, then -1 is an eigenvalue, with an eigenvector
#    of the form ( 1, -1, -1, 1, 1, -1, -1, 1, ... ).
#
#    The family of matrices is nested as a function of N.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#   08 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Robert Gregory, David Karney,
#    Example 3.23,
#    A Collection of Matrices for Testing Computational Algorithms,
#    Wiley, New York, 1969, page 51, 
#    LC: QA263.G68.
#
#  Parameters:
#
#    Input, integer M, N, the number of rows and columns 
#    of the matrix.
#
#    Output, real A(M,N), the matrix.
#
  import numpy as np

  a = np.zeros ( ( m, n ) )

  for i  in range ( 0, m ):
    for j in range ( 0, n ):
      a[i,j] = abs ( i - j )

  return a

def gk323_determinant ( n ):

#*****************************************************************************80
#
## GK323_DETERMINANT computes the determinant of the GK323 matrix.
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
  from r8_mop import r8_mop

  value = r8_mop ( n - 1 ) * 2.0 ** ( n - 2 ) * ( n - 1 )

  return value

def gk323_determinant_test ( ):

#*****************************************************************************80
#
## GK323_DETERMINANT_TEST tests GK323_DETERMINANT.
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
  from gk323 import gk323
  from r8mat_print import r8mat_print

  print ''
  print 'GK323_DETERMINANT_TEST'
  print '  GK323_DETERMINANT computes the GK323 determinant.'

  m = 5
  n = m
 
  a = gk323 ( m, n )

  r8mat_print ( m, n, a, '  GK323 matrix:' )

  value = gk323_determinant ( n )

  print '  Value =  %g' % ( value )

  print ''
  print 'GK323_DETERMINANT_TEST'
  print '  Normal end of execution.'

  return

def gk323_inverse ( n ):

#*****************************************************************************80
#
## GK323_INVERSE returns the inverse of the GK323 matrix.
#
#  Properties:
#
#    A is symmetric: A' = A.
#
#    Because A is symmetric, it is normal.
#
#    Because A is normal, it is diagonalizable.
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

  for i in range ( 0, n ):
    for j in range ( 0, n ):

      if ( i == j ):
        if ( i == 0 or i == n - 1 ):
          a[i,j] = - 0.5 * float ( n - 2 ) / float ( n - 1 )
        else:
          a[i,j] = - 1.0
      elif ( i == j + 1 or i == j - 1 ):
        a[i,j] = 0.5
      elif ( i == 0 and j == n - 1 ):
        a[i,j] = 0.5 / float ( n - 1 )
      elif ( i == n - 1 and j == 0 ):
        a[i,j] = 0.5 / float ( n - 1 )

  return a

def gk323_test ( ):

#*****************************************************************************80
#
## GK323_TEST tests GK323.
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
  print 'GK323_TEST'
  print '  GK323 computes the GK323 matrix.'

  m = 5
  n = m

  a = gk323 ( m, n )
 
  r8mat_print ( m, n, a, '  GK323 matrix:' )

  print ''
  print 'GK323_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  gk323_test ( )
  timestamp ( )
