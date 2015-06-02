#! /usr/bin/env python
#
def clement2 ( n, x, y ):

#*****************************************************************************80
#
## CLEMENT2 returns the CLEMENT2 matrix.
#
#  Formula:
#
#    if ( J = I + 1 ) then
#      A(I,J) = X(I)
#    else if ( I = J + 1 ) then
#      A(I,J) = Y(J)
#    else
#      A(I,J) = 0
#
#  Example:
#
#    N = 5, X and Y arbitrary:
#
#       .   X(1)    .     .     .
#     Y(1)   .    X(2)    .     .
#       .   Y(2)    .   X(3)    .
#       .     .   Y(3)    .   X(4)
#       .     .     .   Y(4)    .
#
#    N = 5, X=(1,2,3,4), Y=(5,6,7,8):
#
#       .     1     .     .     .
#       5     .     2     .     .
#       .     6     .     3     .
#       .     .     7     .     4
#       .     .     .     8     .
#
#  Properties:
#
#    A is generally not symmetric: A' /= A.
#
#    A is tridiagonal.
#
#    Because A is tridiagonal, it has property A (bipartite).
#
#    A is banded, with bandwidth 3.
#
#    The diagonal of A is zero.
#
#    A is singular if N is odd.
#
#    About 64 percent of the entries of the inverse of A are zero.
#
#    If N is even,
#
#      det ( A ) = (-1)^(N/2) * product ( 1 <= I <= N/2 )
#        ( X(2*I-1) * Y(2*I-1) )
#
#    and if N is odd,
#
#      det ( A ) = 0.
#
#    The family of matrices is nested as a function of N.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 December 2014
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
#    Alan Edelman, Eric Kostlan,
#    The road from Kac's matrix to Kac's random polynomials.
#    In Proceedings of the Fifth SIAM Conference on Applied Linear Algebra,
#    edited by John Lewis,
#    SIAM, 1994,
#    pages 503-507.
#
#    Robert Gregory, David Karney,
#    Example 3.19,
#    A Collection of Matrices for Testing Computational Algorithms,
#    Wiley, New York, 1969, page 46, 
#    LC: QA263.G68.
#
#    Olga Taussky, John Todd,
#    Another look at a matrix of Mark Kac,
#    Linear Algebra and Applications,
#    Volume 150, 1991, pages 341-360.
#
#  Parameters:
#
#    Input, integer N, the order of A.
#
#    Input, real X(N-1), Y(N-1), the first super and
#    subdiagonals of the matrix A.
#
#    Output, real A(N,N), the matrix.
#
  import numpy as np

  a = np.zeros ( [ n, n ] )

  for i in range ( 0, n ):
    for j in range ( 0, n ):

      if ( j == i + 1 ):
        a[i,j] = x[i]
      elif ( i == j + 1 ):
        a[i,j] = y[j]
      else:
        a[i,j] = 0.0

  return a

def clement2_determinant ( n, x, y ):

#*****************************************************************************80
#
## CLEMENT2_DETERMINANT computes the determinant of the CLEMENT2 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the order of the matrix.
#
#    Input, real X(N-1), Y(N-1), the first super and
#    subdiagonals of the matrix A.
#
#    Output, real DETERM, the determinant.
#
  if ( ( n % 2 ) == 1 ):
    determ = 0.0
  else:
    determ = 1.0
    for i in range ( 0, n - 1, 2 ):
      determ = determ * x[i] * y[i]

    if ( ( n // 2 ) % 2 == 1 ):
      determ = - determ

  return determ

def clement2_determinant_test ( ):

#*****************************************************************************80
#
## CLEMENT2_DETERMINANT_TEST tests CLEMENT2_DETERMINANT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 December 2014
#
#  Author:
#
#    John Burkardt
#
  from clement2 import clement2
  from r8mat_print import r8mat_print
  from r8vec_uniform_ab import r8vec_uniform_ab

  print ''
  print 'CLEMENT2_DETERMINANT_TEST'
  print '  CLEMENT2_DETERMINANT computes the CLEMENT2 determinant.'

  m = 4
  n = m
  seed = 123456789
  x, seed = r8vec_uniform_ab ( n-1, -5.0, +5.0, seed )
  y, seed = r8vec_uniform_ab ( n-1, -5.0, +5.0, seed )

  a = clement2 ( n, x, y )
  r8mat_print ( m, n, a, '  CLEMENT2 matrix:' )

  value = clement2_determinant ( n, x, y )
  print '  Value =  %g' % ( value )

  print ''
  print 'CLEMENT2_DETERMINANT_TEST'
  print '  Normal end of execution.'

  return

def clement2_inverse ( n, x, y ):

#*****************************************************************************80
#
## CLEMENT2_INVERSE returns the inverse of the Clement3 matrix.
#
#  Example:
#
#    N = 6, X and Y arbitrary:
#
#     0                1/Y1 0         -X2/(Y1*Y3) 0   X2*X4/(Y1*Y3*Y5)
#     1/X1             0    0          0          0    0
#     0                0    0          1/Y3       0   -X4/(Y3*Y5)
#    -Y2/(X1*X3)       0    1/X3       0          0    0
#     0                0    0          0          0    1/Y5
#     Y2*Y4/(X1*X3*X5) 0   -Y4/(X3*X5) 0          1/X5 0
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 March 2015
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
#    Input, integer N, the order of A.  N must not be odd%
#
#    Input, real X(N-1), Y(N-1), the first super and
#    subdiagonals of the matrix A.  None of the entries
#    of X or Y may be zero.
#
#    Output, real A(N,N), the matrix.
#
  import numpy as np
  from sys import exit

  if ( ( n % 2 ) == 1 ):
    print ''
    print 'CLEMENT2_INVERSE - Fatal error!'
    print '  The  Clement matrix is singular for odd N.'
    exit ( 'CLEMENT2_INVERSE - Fatal error!' )

  for i in range ( 0, n - 1 ):

    if ( x[i] == 0.0 ):
      print ''
      print 'CLEMENT2_INVERSE - Fatal error!'
      print '  The matrix is singular'
      print '  X(I) = 0 for I = %d' % ( i )
      exit ( 'CLEMENT2_INVERSE - Fatal error!' )
    elif ( y[i] == 0.0 ):
      print ''
      print 'CLEMENT2_INVERSE - Fatal error!'
      print '  The matrix is singular'
      print '  Y(I) = 0 for I = %d' % ( i )
      exit ( 'CLEMENT2_INVERSE - Fatal error!' )

  a = np.zeros ( ( n, n ) )

  for i in range ( 0, n ):

    if ( ( i % 2 ) == 0 ):

      for j in range ( i, n - 1, 2 ):

        if ( j == i ):
          prod1 = 1.0 / y[j]
          prod2 = 1.0 / x[j]
        else:
          prod1 = - prod1 * x[j-1] / y[j]
          prod2 = - prod2 * y[j-1] / x[j]

        a[i,j+1] = prod1
        a[j+1,i] = prod2

  return a

def clement2_test ( ):

#*****************************************************************************80
#
## CLEMENT2_TEST tests CLEMENT2.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 December 2014
#
#  Author:
#
#    John Burkardt
#
  from r8mat_print import r8mat_print
  from r8vec_uniform_ab import r8vec_uniform_ab

  print ''
  print 'CLEMENT2_TEST'
  print '  CLEMENT2 computes the CLEMENT2 matrix.'

  m = 4
  n = m
  seed = 123456789
  x, seed = r8vec_uniform_ab ( n-1, -5.0, +5.0, seed )
  y, seed = r8vec_uniform_ab ( n-1, -5.0, +5.0, seed )

  a = clement2 ( n, x, y )
  r8mat_print ( m, n, a, '  CLEMENT2 matrix:' )

  print ''
  print 'CLEMENT2_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  clement2_test ( )
  timestamp ( )
