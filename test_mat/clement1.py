#! /usr/bin/env python
#
def clement1 ( n ):

#*****************************************************************************80
#
## CLEMENT1 returns the CLEMENT1 matrix.
#
#  Formula:
#
#    if ( J = I+1 )
#      A(I,J) = sqrt(I*(N-I))
#    else if ( I = J+1 )
#      A(I,J) = sqrt(J*(N-J))
#    else
#      A(I,J) = 0
#
#  Example:
#
#    N = 5
#
#       .    sqrt(4)    .       .       .
#    sqrt(4)    .    sqrt(6)    .       .
#       .    sqrt(6)    .    sqrt(6)    .
#       .       .    sqrt(6)    .    sqrt(4)
#       .       .       .    sqrt(4)    .
#
#  Properties:
#
#    A is tridiagonal.
#
#    A is banded, with bandwidth 3.
#
#    Because A is tridiagonal, it has property A (bipartite).
#
#    A is symmetric: A' = A.
#
#    Because A is symmetric, it is normal.
#
#    Because A is normal, it is diagonalizable.
#
#    A is persymmetric: A(I,J) = A(N+1-J,N+1-I).
#
#    The diagonal of A is zero.
#
#    A is singular if N is odd.
#
#    About 64 percent of the entries of the inverse of A are zero.
#
#    The eigenvalues are plus and minus the numbers
#
#      N-1, N-3, N-5, ..., (1 or 0).
#
#    If N is even,
#
#      det ( A ) = (-1)**(N/2) * (N-1) * (N+1)**(N/2)
#
#    and if N is odd,
#
#      det ( A ) = 0
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Paul Clement,
#    A class of triple-diagonal matrices for test purposes,
#    SIAM Review,
#    Volume 1, 1959, pages 50-52.
#
#  Parameters:
#
#    Input, integer N, the order of A.
#
#    Output, real A(N,N), the matrix.
#
  from math import sqrt
  import numpy as np

  a = np.zeros ( [ n, n ] )

  for i in range ( 0, n ):
    for j in range ( 0, n ):

      if ( j == i + 1 ):
        a[i,j] = sqrt ( ( i + 1 ) * ( n - i - 1 ) )
      elif ( i == j + 1 ):
        a[i,j] = sqrt ( ( j + 1 ) * ( n - j - 1 ) )
      else:
        a[i,j] = 0.0

  return a

def clement1_determinant ( n ):

#*****************************************************************************80
#
## CLEMENT1_DETERMINANT computes the determinant of the CLEMENT1 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 December 2014
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
    determ = 0.0
  else:
    determ = 1.0
    for i in range ( 1, n, 2 ):
      determ = determ * ( i ) * ( n - i )

    if ( ( n // 2 ) % 2 == 1 ):
      determ = - determ

  return determ

def clement1_inverse ( n ):

#*****************************************************************************80
#
## CLEMENT1_INVERSE returns the inverse of the CLEMENT1 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    24 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the order of A.  N must not be odd%
#
#    Output, real A(N,N), the matrix.
#
  import numpy as np
  from sys import exit

  if ( ( n % 2 ) == 1 ):
    print ''
    print 'CLEMENT1_INVERSE - Fatal error!'
    print '  The Clement matrix is singular for odd N.'
    exit ( 'CLEMENT1_INVERSE - Fatal error!' )

  a = np.zeros ( ( n, n ) )

  for i in range ( 0, n ):

    if ( ( i % 2 ) == 0 ):

      for j in range ( i, n - 1, 2 ):

        if ( j == i ):
          prod = 1.0 / np.sqrt ( float ( ( j + 1 ) * ( n - j - 1 ) ) )
        else:
          prod = - prod \
            * np.sqrt ( float ( ( j ) * ( n - j ) ) ) \
            / np.sqrt ( float ( ( j + 1 ) * ( n - j - 1 ) ) )
 
        a[i,j+1] = prod
        a[j+1,i] = prod

  return a

def clement1_determinant_test ( ):

#*****************************************************************************80
#
## CLEMENT1_DETERMINANT_TEST tests CLEMENT1_DETERMINANT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 December 2014
#
#  Author:
#
#    John Burkardt
#
  from r8mat_print import r8mat_print

  print ''
  print 'CLEMENT1_DETERMINANT_TEST'
  print '  CLEMENT1_DETERMINANT computes the CLEMENT1 determinant.'

  m = 4
  n = 4
  a = clement1 ( n )
  r8mat_print ( m, n, a, '  CLEMENT1 matrix:' )

  value = clement1_determinant ( n )
  print '  Value =  %g' % ( value )

  print ''
  print 'CLEMENT1_DETERMINANT_TEST'
  print '  Normal end of execution.'

  return

def clement1_test ( ):

#*****************************************************************************80
#
## CLEMENT1_TEST tests CLEMENT1.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 December 2014
#
#  Author:
#
#    John Burkardt
#
  from r8mat_print import r8mat_print

  print ''
  print 'CLEMENT1_TEST'
  print '  CLEMENT1 computes the CLEMENT1 matrix.'

  m = 4
  n = m
  a = clement1 ( n )
  r8mat_print ( n, n, a, '  CLEMENT1 matrix:' )

  print ''
  print 'CLEMENT1_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  clement1_test ( )
  timestamp ( )
