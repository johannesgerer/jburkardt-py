#! /usr/bin/env python
#
def wilk21 ( n ):

#*****************************************************************************80
#
## WILK21 returns the WILK21 matrix.
#
#  Discussion:
#
#    By using values of N not equal to 21, WILK21 can return a variety
#    of related matrices.
#
#  Formula:
#
#    if ( I = J )
#      A(I,J) = nint ( abs ( i -  ( n+1 ) / 2 ) )
#    elseif ( I = J - 1 or I = J + 1 )
#      A(I,J) = 1
#    else
#      A(I,J) = 0
#
#  Example:
#
#    N = 21
#
#    10  1  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .
#     1  9  1  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .
#     .  1  8  1  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .
#     .  .  1  7  1  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .
#     .  .  .  1  6  1  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .
#     .  .  .  .  1  5  1  .  .  .  .  .  .  .  .  .  .  .  .  .  .
#     .  .  .  .  .  1  4  1  .  .  .  .  .  .  .  .  .  .  .  .  .
#     .  .  .  .  .  .  1  3  1  .  .  .  .  .  .  .  .  .  .  .  .
#     .  .  .  .  .  .  .  1  2  1  .  .  .  .  .  .  .  .  .  .  .
#     .  .  .  .  .  .  .  .  1  1  1  .  .  .  .  .  .  .  .  .  .
#     .  .  .  .  .  .  .  .  .  1  0  1  .  .  .  .  .  .  .  .  .
#     .  .  .  .  .  .  .  .  .  .  1  1  1  .  .  .  .  .  .  .  .
#     .  .  .  .  .  .  .  .  .  .  .  1  2  1  .  .  .  .  .  .  .
#     .  .  .  .  .  .  .  .  .  .  .  .  1  3  1  .  .  .  .  .  .
#     .  .  .  .  .  .  .  .  .  .  .  .  .  1  4  1  .  .  .  .  .
#     .  .  .  .  .  .  .  .  .  .  .  .  .  .  1  5  1  .  .  .  .
#     .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  1  6  1  .  .  .
#     .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  1  7  1  .  .
#     .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  1  8  1  .
#     .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  1  9  1
#     .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  1 10
#
#  Properties:
#
#    A is tridiagonal.
#
#    Because A is tridiagonal, it has property A (bipartite).
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
#    A is persymmetric: A(I,J) = A(N+1-J,N+1-I).
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    James Wilkinson,
#    The Algebraic Eigenvalue Problem,
#    Oxford University Press, 1965,
#    page 308.
#
#  Parameters:
#
#    Input, integer N, the order of the desired matrix.
#
#    Output, real A(N,N), the matrix.
#
  import numpy as np

  a = np.zeros ( ( n, n ) )

  for i in range ( 0, n ):
    for j in range ( 0, n ):

      if ( i == j ):
        a[i,j] = float ( abs ( i + 1 - ( n + 1 ) // 2 ) )
      elif ( j == i + 1 ):
        a[i,j] = 1.0
      elif ( j == i - 1 ):
        a[i,j] = 1.0

  return a

def wilk21_determinant ( n ):

#*****************************************************************************80
#
## WILK21_DETERMINANT computes the determinant of the WILK21 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 February 2015
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

  d = np.zeros ( n )

  for i in range ( 0, n ):
    d[i] = abs ( float ( i + 1 - ( n + 1 ) // 2 ) )

  determ_nm1 = d[n-1]

  if ( n == 1 ):
    value = determ_nm1;
    return value

  determ_nm2 = determ_nm1
  determ_nm1 = d[n-2] * d[n-1] - 1.0

  if ( n == 2 ):
    value = determ_nm1
    return value

  for i in range ( n - 3, -1, -1 ):
 
    value = d[i] * determ_nm1 - determ_nm2

    determ_nm2 = determ_nm1
    determ_nm1 = value

  return value

def wilk21_determinant_test ( ):

#*****************************************************************************80
#
## WILK21_DETERMINANT_TEST tests WILK21_DETERMINANT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 February 2015
#
#  Author:
#
#    John Burkardt
#
  from wilk21 import wilk21
  from r8mat_print import r8mat_print

  print ''
  print 'WILK21_DETERMINANT_TEST'
  print '  WILK21_DETERMINANT computes the WILK21 determinant.'

  m = 5
  n = m
 
  a = wilk21 ( n )

  r8mat_print ( m, n, a, '  WILK21 matrix:' )

  value = wilk21_determinant ( n )

  print ''
  print '  Value =  %g' % ( value )

  print ''
  print 'WILK21_DETERMINANT_TEST'
  print '  Normal end of execution.'

  return

def wilk21_inverse ( n ):

#*****************************************************************************80
#
## WILK21_INVERSE returns the inverse of the WILK21 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    CM daFonseca, J Petronilho,
#    Explicit Inverses of Some Tridiagonal Matrices,
#    Linear Algebra and Its Applications,
#    Volume 325, 2001, pages 7-21.
#
#  Parameters:
#
#    Input, integer N, the order of the matrix.
#
#    Output, real A(N,N), the inverse of the matrix.
#
  import numpy as np
  from r8_mop import r8_mop

  y = np.zeros ( n )
  for i in range ( 0, n ):
    y[i] = float ( abs ( i + 1 - ( n + 1 ) // 2 ) )

  d = np.zeros ( n )
  d[n-1] = y[n-1]
  for i in range ( n - 2, -1, -1 ):
    d[i] = y[i] - 1.0 / d[i+1]

  e = np.zeros ( n )
  e[0] = y[0]
  for i in range ( 1, n ):
    e[i] = y[i] - 1.0 / e[i-1]

  a = np.zeros ( ( n, n ) )

  for i in range ( 0, n ):
    for j in range ( 0, i + 1 ):
      p1 = 1.0
      for k in range ( i + 1, n ):
        p1 = p1 * d[k]
      p2 = 1.0
      for k in range ( j, n ):
        p2 = p2 * e[k]
      a[i,j] = r8_mop ( i + j ) * p1 / p2
    for j in range ( i + 1, n ):
      p1 = 1.0
      for k in range ( j + 1, n ):
        p1 = p1 * d[k]
      p2 = 1.0
      for k in range ( i, n ):
        p2 = p2 * e[k]
      a[i,j] = r8_mop ( i + j ) * p1 / p2

  return a

def wilk21_test ( ):

#*****************************************************************************80
#
## WILK21_TEST tests WILK21.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 February 2015
#
#  Author:
#
#    John Burkardt
#
  from r8mat_print import r8mat_print

  print ''
  print 'WILK21_TEST'
  print '  WILK21 computes the WILK21 matrix.'

  m = 5
  n = m

  a = wilk21 ( n )
 
  r8mat_print ( m, n, a, '  WILK21 matrix:' )

  print ''
  print 'WILK21_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  wilk21_test ( )
  timestamp ( )
