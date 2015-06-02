#! /usr/bin/env python
#
def maxij ( m, n ):

#*****************************************************************************80
#
## MAXIJ returns the MAXIJ matrix.
#
#  Discussion:
#
#    This matrix is occasionally known as the "Boothroyd MAX" matrix.
#
#  Formula:
#
#    A(I,J) = max(I,J)
#
#  Example:
#
#    N = 5
#
#    1 2 3 4 5
#    2 2 3 4 5
#    3 3 3 4 5
#    4 4 4 4 5
#    5 5 5 5 5
#
#  Properties:
#
#    A is integral, therefore det ( A ) is integral, and 
#    det ( A ) * inverse ( A ) is integral.
#
#    A is symmetric: A' = A.
#
#    Because A is symmetric, it is normal.
#
#    Because A is normal, it is diagonalizable.
#
#    The inverse of A is tridiagonal.
#
#    The family of matrices is nested as a function of N.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Robert Gregory, David Karney,
#    Example 3.13,
#    A Collection of Matrices for Testing Computational Algorithms,
#    Wiley, 1969, page 42,
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

  a = np.zeros ( [ m, n ] )

  for j in range ( 0, n ):
    for i in range ( 0, m ):

      a[i,j] = max ( i, j ) + 1

  return a

def maxij_condition ( n ):

#*****************************************************************************80
#
## MAXIJ_CONDITION returns the L1 condition of the MAXIJ matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the order of the matrix.
#
#    Output, real VALUE, the L1 condition.
#
  a_norm = n * n

  if ( n == 1 ):
    b_norm = 1.0
  elif ( n == 2 ):
    b_norm = 2.0
  else:
    b_norm = 4.0

  value = a_norm * b_norm

  return value

def maxij_condition_test ( ):

#*****************************************************************************80
#
## MAXIJ_CONDITION_TEST tests MAXIJ_CONDITION.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    17 December 2014
#
#  Author:
#
#    John Burkardt
#
  from maxij import maxij
  from r8mat_print import r8mat_print

  print ''
  print 'MAXIJ_CONDITION_TEST'
  print '  MAXIJ_CONDITION computes the condition of the MAXIJ matrix.'
  print ''

  n = 4
  a = maxij ( n, n )
  r8mat_print ( n, n, a, '  MAXIJ matrix:' )

  value = maxij_condition ( n )

  print ''
  print '  Value =  %g' % ( value )

  print ''
  print 'MAXIJ_CONDITION_TEST'
  print '  Normal end of execution.'

  return

def maxij_determinant ( n ):

#*****************************************************************************80
#
## MAXIJ_DETERMINANT returns the determinant of the MAXIJ matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 January 2015
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
  value = float ( n )

  return value

def maxij_determinant_test ( ):

#*****************************************************************************80
#
## MAXIJ_DETERMINANT_TEST tests MAXIJ_DETERMINANT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 January 2015
#
#  Author:
#
#    John Burkardt
#
  from maxij import maxij
  from r8mat_print import r8mat_print

  print ''
  print 'MAXIJ_DETERMINANT_TEST'
  print '  MAXIJ_DETERMINANT computes the determinant of the MAXIJ matrix.'
  print ''

  n = 4
  a = maxij ( n, n )
  r8mat_print ( n, n, a, '  MAXIJ matrix:' )

  value = maxij_determinant ( n )

  print ''
  print '  Value =  %g' % ( value )

  print ''
  print 'MAXIJ_DETERMINANT_TEST'
  print '  Normal end of execution.'

  return

def maxij_inverse ( n ):

#*****************************************************************************80
#
## MAXIJ_INVERSE returns the inverse of the MAXIJ matrix.
#
#  Formula:
#
#    if ( I = 1 and J = 1 )
#      A(I,J) = -1
#    else if ( I = N and J = N )
#      A(I,J) = -(N-1)/N
#    else if ( I = J )
#      A(I,J) = -2
#    else if ( J = I-1 or J = I + 1 )
#      A(I,J) =  1
#    else
#      A(I,J) =  0
#
#  Example:
#
#    N = 5
#
#    -1  1  0  0   0
#     1 -2  1  0   0
#     0  1 -2  1   0
#     0  0  1 -2   1
#     0  0  0  1 -4/5
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
#    A is "almost" equal to the second difference matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    18 March 2015
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
 
      if ( j == i ):

        if ( i == 0 ):
          a[i,j] = - 1.0
        elif ( i < n - 1 ):
          a[i,j] = - 2.0
        else:
          a[i,j] = - float ( n - 1 ) / float ( n )

      elif ( j == i - 1 or j == i + 1 ):

        a[i,j] = 1.0;

  return a

def maxij_plu ( n ):

#*****************************************************************************80
#
## MAXIJ_PLU returns the PLU factors of the MAXIJ matrix.
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
#  Parameters:
#
#    Input, integer N, the order of the matrix.
#
#    Output, real P(N,N), L(N,N), U(N,N), the PLU factors.
#
  import numpy as np
  from i4_wrap import i4_wrap

  p = np.zeros ( ( n, n ) )

  for j in range ( 0, n ):
    for i in range ( 0, n ):
      if ( i4_wrap ( j - i, 1, n ) == 1 ):
        p[i,j] = 1.0

  l = np.zeros ( ( n, n ) )

  l[0,0] = 1.0

  j = 0
  for i in range ( 1, n ):
    l[i,j] = float ( i ) / float ( n )

  for j in range ( 1, n ):
    l[j,j] = 1.0

  u = np.zeros ( ( n, n ) )

  for j in range ( 0, n ):
    u[0,j] = float ( n )

  for i in range ( 1, n ):
    for j in range ( i, n ):
      u[i,j] = float ( j + 1 - i )

  return p, l, u

def maxij_test ( ):

#*****************************************************************************80
#
## MAXIJ_TEST tests MAXIJ.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 January 2015
#
#  Author:
#
#    John Burkardt
#
  from r8mat_print import r8mat_print

  print ''
  print 'MAXIJ_TEST'
  print '  MAXIJ computes the MAXIJ matrix.'

  m = 5
  n = 5
  a = maxij ( m, n )
  r8mat_print ( m, n, a, '  MAXIJ matrix:' )

  print ''
  print 'MAXIJ_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  maxij_test ( )
  timestamp ( )
