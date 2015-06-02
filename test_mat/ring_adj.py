#! /usr/bin/env python
#
def ring_adj ( m, n ):

#*****************************************************************************80
#
## RING_ADJ returns the RING_ADJ matrix.
#
#  Discussion:
#
#    This is the adjacency matrix for a set of points on a circle.
#
#  Example:
#
#    N = 5
#
#    0  1  0  0  1
#    1  0  1  0  0
#    0  1  0  1  0
#    0  0  1  0  1
#    1  0  0  1  0
#
#  Properties:
#
#    A is symmetric: A' = A.
#
#    Because A is symmetric, it is normal.
#
#    Because A is normal, it is diagonalizable.
#
#    The determinant for N = 1 is 1, for N = 2 is -1, and for 2 < N,
#      mod ( N, 4 ) = 1 ==> det ( A ) =  2
#      mod ( N, 4 ) = 2 ==> det ( A ) = -4
#      mod ( N, 4 ) = 3 ==> det ( A ) =  2
#      mod ( N, 4 ) = 0 ==> det ( A ) =  0
#
#    A is a zero/one matrix.
#
#    A is an adjacency matrix.
#
#    A has a zero diagonal.
#
#    A is cyclic tridiagonal.
#
#    A is a circulant matrix: each row is shifted once to get the next row.
#
#    A has a constant row sum of 2.
#
#    Because it has a constant row sum of 2,
#    A has an eigenvalue of 2, and
#    a (right) eigenvector of ( 1, 1, 1, ..., 1 ).
#
#    A has a constant column sum of 2.
#
#    Because it has a constant column sum of 2,
#    A has an eigenvalue of 2, and
#    a (left) eigenvector of ( 1, 1, 1, ..., 1 ).
#
#    A is persymmetric: A(I,J) = A(N+1-J,N+1-I).
#
#    A is centrosymmetric: A(I,J) = A(N+1-I,N+1-J).
#
#    A has an eigenvector of ( 1, 1, 1, ..., 1 ) with eigenvalue of 2.
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
#    Input, integer N, the order of A.
#
#    Output, real A(N,N), the matrix.
#
  import numpy as np

  a = np.zeros ( ( n, n ) )

  for i in range ( 0, n ):
    for j in range ( 0, n ):
      if ( j == i + 1 or j == i - 1 or j == i + 1 - n or j == i - 1 + n ):
        a[i,j] = 1.0

  return a

def ring_adj_determinant ( n ):

#*****************************************************************************80
#
## RING_ADJ_DETERMINANT returns the determinant of the RING_ADJ matrix.
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
#    Input, integer N, the order of the matrix.
#
#    Output, real VALUE, the determinant.
#
  if ( n == 1 ):
    value = 1.0
  elif ( n == 2 ):
    value = -1.0
  elif ( ( n % 4 ) == 0 ):
    value = 0.0
  elif ( ( n % 4 ) == 1 ):
    value = 2.0
  elif ( ( n % 4 ) == 2 ):
    value = -4.0
  elif ( ( n % 4 ) == 3 ):
    value = 2.0

  return value

def ring_adj_null_left ( m, n ):

#*****************************************************************************80
#
## RING_ADJ_NULL_LEFT returns a left null vector of the RING_ADJ matrix.
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
#    Output, real X(N), the null vector.
#
  import numpy as np
  from sys import exit

  if ( ( m % 4 ) != 0 ):
    print  ''
    print 'RING_ADJ_NULL_LEFT - Fatal error!'
    print '  M must be a multiple of 4.'
    exit ( 'RING_ADJ_NULL_LEFT - Fatal error!' )

  x = np.zeros ( m )

  for i in range ( 0, m, 4 ):
    x[i]   = + 1.0
    x[i+1] = + 1.0
    x[i+2] = - 1.0
    x[i+3] = - 1.0

  return x

def ring_adj_null_right ( m, n ):

#*****************************************************************************80
#
## RING_ADJ_NULL_RIGHT returns a right null vector of the RING_ADJ matrix.
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
#    Output, real X(N), the null vector.
#
  import numpy as np
  from sys import exit

  if ( ( n % 4 ) != 0 ):
    print  ''
    print 'RING_ADJ_NULL_RIGHT - Fatal error!'
    print '  N must be a multiple of 4.'
    exit ( 'RING_ADJ_NULL_RIGHT - Fatal error!' )

  x = np.zeros ( n )

  for i in range ( 0, n, 4 ):
    x[i]   = + 1.0
    x[i+1] = + 1.0
    x[i+2] = - 1.0
    x[i+3] = - 1.0

  return x

def ring_adj_test ( ):

#*****************************************************************************80
#
## RING_ADJ_TEST tests RING_ADJ.
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
  from r8mat_print import r8mat_print

  print ''
  print 'RING_ADJ_TEST'
  print '  RING_ADJ computes the RING_ADJ matrix.'

  m = 6
  n = m

  a = ring_adj ( m, n )
  r8mat_print ( m, n, a, '  RING_ADJ matrix:' )

  print ''
  print 'RING_ADJ_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  ring_adj_test ( )
  timestamp ( )
