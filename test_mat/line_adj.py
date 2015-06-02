#! /usr/bin/env python
#
def line_adj ( n ):

#*****************************************************************************80
#
## LINE_ADJ returns the LINE_ADJ matrix, for line adjacency matrix.
#
#  Example:
#
#    N = 5
#
#    0  1  0  0  0
#    1  0  1  0  0
#    0  1  0  1  0
#    0  0  1  0  1
#    0  0  0  1  0
#
#  Properties:
#
#    A is symmetric: A' = A.
#
#    Because A is symmetric, it is normal.
#
#    Because A is normal, it is diagonalizable.
#
#    A is tridiagonal.
#
#    Because A is tridiagonal, it has property A (bipartite).
#
#    A is banded, with bandwidth 3.
#
#    A is an adjacency matrix for a set of points arranged in a line.
#
#    A has a zero diagonal.
#
#    A is a zero/one matrix.
#
#    The row and column sums are all 2, except for the first and last
#    rows and columns which have a sum of 1.
#
#    The family of matrices is nested as a function of N.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    18 February 2015
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
      if ( j == i - 1 ):
        a[i,j] = 1.0
      elif ( j == i + 1 ):
        a[i,j] = 1.0

  return a

def line_adj_determinant ( n ):

#*****************************************************************************80
#
## LINE_ADJ_DETERMINANT computes the determinant of the LINE_ADJ matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    18 February 2015
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
  if ( ( n % 4 ) == 1 ):
    value =   0.0
  elif ( ( n % 4 ) == 2 ):
    value = - 1.0
  elif ( ( n % 4 ) == 3 ):
    value =   0.0
  elif ( ( n % 4 ) == 0 ):
    value = + 1.0

  return value

def line_adj_determinant_test ( ):

#*****************************************************************************80
#
## LINE_ADJ_DETERMINANT_TEST tests LINE_ADJ_DETERMINANT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    18 February 2015
#
#  Author:
#
#    John Burkardt
#
  from line_adj import line_adj
  from r8mat_print import r8mat_print

  print ''
  print 'LINE_ADJ_DETERMINANT_TEST'
  print '  LINE_ADJ_DETERMINANT computes the LINE_ADJ determinant.'

  m = 5
  n = m
 
  a = line_adj ( n )

  r8mat_print ( m, n, a, '  LINE_ADJ matrix:' )

  value = line_adj_determinant ( n )

  print '  Value =  %g' % ( value )

  print ''
  print 'LINE_ADJ_DETERMINANT_TEST'
  print '  Normal end of execution.'

  return

def line_adj_eigen_right ( n ):

#*****************************************************************************80
#
## LINE_ADJ_EIGEN_RIGHT returns the right eigenvectors of the LINE_ADJ matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 April 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the order of A.
#
#    Output, real A(N,N), the right eigenvector matrix.
#
  import numpy as np

  a = np.zeros ( ( n, n ) )

  for i in range ( 0, n ):
    for j in range ( 0, n ):
      angle = float ( ( i + 1 ) *  ( j + 1 ) ) * np.pi / float ( n + 1 )
      a[i,j] = np.sqrt ( 2.0 / float ( n + 1 ) ) * np.sin ( angle )

  return a

def line_adj_eigenvalues ( n ):

#*****************************************************************************80
#
## LINE_ADJ_EIGENVALUES returns the eigenvalues of the LINE_ADJ matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 April 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the order of the matrix.
#
#    Output, real LAM(N), the eigenvalues.
#
  import numpy as np

  lam = np.zeros ( n )

  for i in range ( 0, n ):
    angle = float ( i + 1 ) * np.pi / float ( n + 1 )
    lam[i] = 2.0 * np.cos ( angle )

  return lam

def line_adj_inverse ( n ):

#*****************************************************************************80
#
## LINE_ADJ_INVERSE returns the inverse of the LINE_ADJ matrix.
#
#  Example:
#
#    N = 6:
#
#     0     1     0    -1     0     1
#     1     0     0     0     0     0
#     0     0     0     1     0    -1
#    -1     0     1     0     0     0
#     0     0     0     0     0     1
#     1     0    -1     0     1     0
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    17 April 2015
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
  from sys import exit

  if ( ( n % 2 ) == 1 ):
    print ''
    print 'LINE_ADJ_INVERSE - Fatal error!'
    print '  The matrix is singular for odd N.'
    exit ( 'LINE_ADJ_INVERSE - Fatal error!' )

  a = np.zeros ( ( n, n ) )

  for i in range ( 0, n ):

    if ( ( i % 2 ) == 0 ):

      for j in range ( i, n - 1, 2 ):

        if ( j == i ):
          p = 1.0
        else:
          p = - p

        a[i,j+1] = p
        a[j+1,i] = p

  return a

def line_adj_null_left ( m, n ):

#*****************************************************************************80
#
## LINE_ADJ_NULL_LEFT returns a left null vector of the LINE_ADJ matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    15 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, N, the order of the matrix.
#
#    Output, real X(M), the vector
#
  import numpy as np

  if ( ( m % 2 ) == 0 ):
    print ''
    print 'LINE_ADJ_NULL_LEFT - Fatal error!'
    print '  For M even, there is no null vector.'
    error ( 'LINE_ADJ_NULL_LEFT - Fatal error!' )

  x = np.zeros ( m )
  s = 1.0

  for i in range ( 0, m, 2 ):
    x[i] = s
    s = -s

  return x

def line_adj_null_right ( m, n ):

#*****************************************************************************80
#
## LINE_ADJ_NULL_RIGHT returns a right null vector of the LINE_ADJ matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    12 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, N, the order of the matrix.
#
#    Output, real X(N), the vector
#
  import numpy as np

  if ( ( n % 2 ) == 0 ):
    print ''
    print 'LINE_ADJ_NULL_RIGHT - Fatal error!'
    print '  For N even, there is no null vector.'
    error ( 'LINE_ADJ_NULL_RIGHT - Fatal error!' )

  x = np.zeros ( n )
  s = 1.0

  for i in range ( 0, n, 2 ):
    x[i] = s
    s = -s

  return x

def line_adj_test ( ):

#*****************************************************************************80
#
## LINE_ADJ_TEST tests LINE_ADJ.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    18 February 2015
#
#  Author:
#
#    John Burkardt
#
  from r8mat_print import r8mat_print

  print ''
  print 'LINE_ADJ_TEST'
  print '  LINE_ADJ computes the LINE_ADJ matrix.'

  m = 5
  n = m

  a = line_adj ( n )
 
  r8mat_print ( m, n, a, '  LINE_ADJ matrix:' )

  print ''
  print 'LINE_ADJ_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  line_adj_test ( )
  line_adj_determinant_test ( )
  timestamp ( )
