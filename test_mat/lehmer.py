#! /usr/bin/env python
#
def lehmer ( m, n ):

#*****************************************************************************80
#
## LEHMER returns the LEHMER matrix.
#
#  Discussion:
#
#    This matrix is also known as the "Westlake" matrix.
#
#  Formula:
#
#    A(I,J) = min ( I, J ) / max ( I, J )
#
#  Example:
#
#    N = 5
#
#    1/1  1/2  1/3  1/4  1/5
#    1/2  2/2  2/3  2/4  2/5
#    1/3  2/3  3/3  3/4  3/5
#    1/4  2/4  3/4  4/4  4/5
#    1/5  2/5  3/5  4/5  5/5
#
#  Properties:
#
#    A is symmetric: A' = A.
#
#    Because A is symmetric, it is normal.
#
#    Because A is normal, it is diagonalizable.
#
#    A is positive definite.
#
#    A is totally nonnegative.
#
#    The inverse of A is tridiagonal.
#
#    The condition number of A lies between N and 4*N*N.
#
#    The family of matrices is nested as a function of N.
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
#    Morris Newman, John Todd,
#    The evaluation of matrix inversion programs,
#    Journal of the Society for Industrial and Applied Mathematics,
#    Volume 6, Number 4, 1958, pages 466-476.
#
#    Solutions to problem E710, proposed by DH Lehmer: The inverse of
#    a matrix.
#    American Mathematical Monthly,
#    Volume 53, Number 9, November 1946, pages 534-535.
#
#    John Todd,
#    Basic Numerical Mathematics, Volume 2: Numerical Algebra,
#    Academic Press, 1977, page 154.
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
      a[i,j] = float ( min ( i + 1, j + 1 ) ) / float ( max ( i + 1, j + 1 ) )

  return a

def lehmer_determinant ( n ):

#*****************************************************************************80
#
## LEHMER_DETERMINANT returns the determinant of the LEHMER matrix.
#
#  Formula:
#
#    determinant = (2n)! / 2^n / (n!)^3
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
#  Reference:
#
#    Emrah Kilic, Pantelimon Stanica,
#    The Lehmer matrix and its recursive analogue,
#    Journal of Combinatorial Mathematics and Combinatorial Computing,
#    Volume 74, August 2010, pages 193-205.
#
#  Parameters:
#
#    Input, integer N, the order of the matrix.
#
#    Output, real VALUE, the determinant.
#
  value = 1.0
  for i in range ( 0, n ):
    value = value * float ( n + i + 1 ) / float ( 2 * ( i + 1 ) ** 2 )

  return value

def lehmer_inverse ( n ):

#*****************************************************************************80
#
## LEHMER_INVERSE returns the inverse of the LEHMER matrix.
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
#  Parameters:
#
#    Input, integer N, the order of A.
#
#    Output, real A(N,N), the matrix.
#
  import numpy as np

  a = np.zeros ( ( n, n ) )

  for i in range ( 0, n - 1 ):
    ip1 = float ( i + 1 )
    a[i,i] = ( 4.0 * ip1 * ip1 * ip1 ) / ( 4.0 * ip1 * ip1 - 1.0 )

  a[n-1,n-1] = float ( n * n ) / float ( 2 * n - 1 )

  for i in range ( 0, n - 1 ):
    ip1 = float ( i + 1 )
    a[i,i+1] = - ( ip1 * ( ip1 + 1.0 ) ) / ( 2.0 * ip1 + 1.0 )
    a[i+1,i] = - ( ip1 * ( ip1 + 1.0 ) ) / ( 2.0 * ip1 + 1.0 )

  return a

def lehmer_llt ( n ):

#*****************************************************************************80
#
## LEHMER_LLT returns the Cholesky factor of the LEHMER matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    07 April 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Emrah Kilic, Pantelimon Stanica,
#    The Lehmer matrix and its recursive analogue,
#    Journal of Combinatorial Mathematics and Combinatorial Computing,
#    Volume 74, August 2010, pages 193-205.
#
#  Parameters:
#
#    Input, integer N, the order of the matrix.
#
#    Output, real A(N,N), the matrix.
#
  import numpy as np

  a = np.zeros ( ( n, n ) )

  for j in range ( 0, n ):
    for i in range ( j, n ):
      a[i,j] = np.sqrt ( float ( 2 * j + 1 ) ) / float ( i + 1 )

  return a

def lehmer_plu ( n ):

#*****************************************************************************80
#
## LEHMER_PLU returns the PLU factors of the LEHMER matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    07 April 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Emrah Kilic, Pantelimon Stanica,
#    The Lehmer matrix and its recursive analogue,
#    Journal of Combinatorial Mathematics and Combinatorial Computing,
#    Volume 74, August 2010, pages 193-205.
#
#  Parameters:
#
#    Input, integer N, the order of the matrix.
#
#    Output, real P(N,N), L(N,N), U(N,N), the PLU factors.
#
  import numpy as np

  p = np.zeros ( ( n, n ) )
  for j in range ( 0, n ):
    p[j,j] = 1.0

  l = np.zeros ( ( n, n ) )
  for j in range ( 0, n ):
    l[j,j] = 1.0
    for i in range ( j + 1, n ):
      l[i,j] = float ( j + 1 ) / float  ( i + 1 )

  u = np.zeros ( ( n, n ) )
  for j in range ( 0, n ):
    for i in range ( 0, j + 1 ):
      u[i,j] = float ( 2 * i + 1 ) / float  ( ( i + 1 ) * ( j + 1 ) )

  return p, l, u

def lehmer_test ( ):

#*****************************************************************************80
#
## LEHMER_TEST tests LEHMER.
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
  print 'LEHMER_TEST'
  print '  LEHMER computes the LEHMER matrix.'

  m = 5
  n = 5
  a = lehmer ( m, n )
  r8mat_print ( m, n, a, '  LEHMER matrix:' )

  print ''
  print 'LEHMER_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  lehmer_test ( )
  timestamp ( )
