#! /usr/bin/env python
#
def line_loop_adj ( n ):

#*****************************************************************************80
#
## LINE_LOOP_ADJ returns the LINE_LOOP_ADJ matrix.
#
#  Discussion:
#
#    LINE_LOOP_ADJ is the line loop adjacency matrix.
#
#  Example:
#
#    N = 5
#
#    1  1  0  0  0
#    1  1  1  0  0
#    0  1  1  1  0
#    0  0  1  1  1
#    0  0  0  1  1
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
#    A is a zero/one matrix.
#
#    The row and column sums are all 3, except for the first and last
#    rows and columns which have a sum of 2.
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
      elif ( j == i ):
        a[i,j] = 1.0
      elif ( j == i + 1 ):
        a[i,j] = 1.0

  return a

def line_loop_adj_determinant ( n ):

#*****************************************************************************80
#
## LINE_LOOP_ADJ_DETERMINANT computes the determinant of the LINE_ADJ matrix.
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
  import numpy as np

  if ( ( n % 2 ) == 1 ):

    value = 0.0

  else:

    value = 1.0

    for i in range ( 1, n + 1 ):
      angle = float ( i ) * np.pi / float ( n + 1 )
      value = value * ( 1.0 + 2.0 * np.cos ( angle ) )

  return value

def line_loop_adj_determinant_test ( ):

#*****************************************************************************80
#
## LINE_LOOP_ADJ_DETERMINANT_TEST tests LINE_LOOP_ADJ_DETERMINANT.
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
  print 'LINE_LOOP_ADJ_DETERMINANT_TEST'
  print '  LINE_LOOP_ADJ_DETERMINANT computes the LINE_ADJ determinant.'

  m = 5
  n = m
 
  a = line_loop_adj ( n )

  r8mat_print ( m, n, a, '  LINE_ADJ matrix:' )

  value = line_loop_adj_determinant ( n )

  print '  Value =  %g' % ( value )

  print ''
  print 'LINE_LOOP_ADJ_DETERMINANT_TEST'
  print '  Normal end of execution.'

  return

def line_loop_adj_eigen_right ( n ):

#*****************************************************************************80
#
## LINE_LOOP_ADJ_EIGEN_RIGHT: right eigenvectors of the LINE_LOOP_ADJ matrix.
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

def line_loop_adj_eigenvalues ( n ):

#*****************************************************************************80
#
## LINE_LOOP_ADJ_EIGENVALUES: the eigenvalues of the LINE_LOOP_ADJ matrix.
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
    lam[i] = 1.0 + 2.0 * np.cos ( angle )

  return lam

def line_loop_adj_test ( ):

#*****************************************************************************80
#
## LINE_LOOP_ADJ_TEST tests LINE_LOOP_ADJ.
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
  print 'LINE_LOOP_ADJ_TEST'
  print '  LINE_LOOP_ADJ computes the LINE_LOOP_ADJ matrix.'

  m = 5
  n = m

  a = line_loop_adj ( n )
 
  r8mat_print ( m, n, a, '  LINE_LOOP_ADJ matrix:' )

  print ''
  print 'LINE_LOOP_ADJ_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  line_loop_adj_test ( )
  timestamp ( )
