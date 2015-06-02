#! /usr/bin/env python
#
def dif2 ( m, n ):

#*****************************************************************************80
#
## DIF2 returns the second difference matrix.
#
#  Example:
#
#    N = 5
#
#    2 -1  .  .  .
#   -1  2 -1  .  .
#    . -1  2 -1  .
#    .  . -1  2 -1
#    .  .  . -1  2
#
#  Rectangular Properties:
#
#    A is banded, with bandwidth 3.
#
#    A is tridiagonal.
#
#    Because A is tridiagonal, it has property A (bipartite).
#
#    A is integral: int ( A ) = A.
#
#    A is Toeplitz: constant along diagonals.
#
#  Square Properties:
#
#    A is symmetric: A' = A.
#
#    Because A is symmetric, it is normal.
#
#    Because A is normal, it is diagonalizable.
#
#    A is persymmetric: A(I,J) = A(N+1-J,N+1-I).
#
#    A is positive definite.
#
#    A is an M matrix.
#
#    A is weakly diagonally dominant, but not strictly diagonally dominant.
#
#    A has an LU factorization A = L * U, without pivoting.
#
#      The matrix L is lower bidiagonal with subdiagonal elements:
#
#        L(I+1,I) = -I/(I+1)
#
#      The matrix U is upper bidiagonal, with diagonal elements
#
#        U(I,I) = (I+1)/I
#
#      and superdiagonal elements which are all -1.
#
#    A has a Cholesky factorization A = L * L', with L lower bidiagonal.
#
#      L(I,I) =    sqrt ( (I+1) / I )
#      L(I,I-1) = -sqrt ( (I-1) / I )
#
#    The eigenvalues are
#
#      LAMBDA(I) = 2 + 2 * COS(I*PI/(N+1))
#                = 4 SIN^2(I*PI/(2*N+2))
#
#    The corresponding eigenvector X(I) has entries
#
#       X(I)(J) = sqrt(2/(N+1)) * sin ( I*J*PI/(N+1) ).
#
#    Simple linear systems:
#
#      x = (1,1,1,...,1,1),   A*x=(1,0,0,...,0,1)
#
#      x = (1,2,3,...,n-1,n), A*x=(0,0,0,...,0,n+1)
#
#    det ( A ) = N + 1.
#
#    The value of the determinant can be seen by induction,
#    and expanding the determinant across the first row:
#
#      det ( A(N) ) = 2 * det ( A(N-1) ) - (-1) * (-1) * det ( A(N-2) )
#                = 2 * N - (N-1)
#                = N + 1
#
#    The family of matrices is nested as a function of N.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    21 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Robert Gregory, David Karney,
#    Example 3.18,
#    A Collection of Matrices for Testing Computational Algorithms,
#    Wiley, New York, 1969, page 45, 
#    LC: QA263.G68.
#
#    Morris Newman, John Todd,
#    Example A8,
#    The evaluation of matrix inversion programs,
#    Journal of the Society for Industrial and Applied Mathematics,
#    Volume 6, Number 4, pages 466-476, 1958.
#
#    John Todd,
#    Example A8,
#    Basic Numerical Mathematics,
#    Volume 2: Numerical Algebra,
#    Academic Press, 1977, page 1.
#
#    Joan Westlake,
#    Test Matrix A15,
#    A Handbook of Numerical Matrix Inversion and Solution of Linear Equations,
#    John Wiley, 1968.
#
#  Parameters:
#
#    Input, integer M, N, the number of rows and columns of A.
#
#    Output, real A(M,N), the matrix.
#
  import numpy as np

  a = np.zeros ( [ m, n ] )

  for i in range ( 0, m ):
    if ( 0 <= i - 1 and i - 1 < n ):
      a[i,i-1] = -1.0
    if ( i < n ):
      a[i,i] = 2.0
    if ( i + 1 < n ):
      a[i,i+1] = -1.0

  return a

def dif2_condition ( n ):

#*****************************************************************************80
#
## DIF2_CONDITION computes the L1 condition of the DIF2 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    07 February 2015
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
  if ( n == 1 ):
    a_norm = 2.0
  elif ( n == 2 ):
    a_norm = 3.0
  else:
    a_norm = 4.0

  b_norm = 0.0
  for j in range ( 1, n + 1 ):
    t = 0.0
    for i in range ( 1, n + 1 ):
      if ( i <= j ):
        t = t + float ( i * ( n - j + 1 ) ) / float ( n + 1 )
      else:
        t = t + float ( j * ( n - i + 1 ) ) / float ( n + 1 )

    b_norm = max ( b_norm, t )

  value = a_norm * b_norm

  return value

def dif2_condition_test ( ):

#*****************************************************************************80
#
## DIF2_CONDITION_TEST tests DIF2_CONDITION.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    07 February 2015
#
#  Author:
#
#    John Burkardt
#
  from dif2 import dif2
  from r8mat_print import r8mat_print

  print ''
  print 'DIF2_CONDITION_TEST'
  print '  DIF2_CONDITION computes the DIF2 condition.'

  m = 5
  n = m
 
  a = dif2 ( m, n )

  r8mat_print ( m, n, a, '  DIF2 matrix:' )

  value = dif2_condition ( n )

  print ''
  print '  Value =  %g' % ( value )

  print ''
  print 'DIF2_CONDITION_TEST'
  print '  Normal end of execution.'

  return

def dif2_determinant ( n ):

#*****************************************************************************80
#
## DIF2_DETERMINANT computes the determinant of the DIF2 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    21 January 2015
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
  determ = n + 1

  return determ

def dif2_determinant_test ( ):

#*****************************************************************************80
#
## DIF2_DETERMINANT_TEST tests DIF2_DETERMINANT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    21 January 2015
#
#  Author:
#
#    John Burkardt
#
  from dif2 import dif2
  from r8mat_print import r8mat_print

  print ''
  print 'DIF2_DETERMINANT_TEST'
  print '  DIF2_DETERMINANT computes the DIF2 determinant.'

  m = 5
  n = m
 
  a = dif2 ( m, n )

  r8mat_print ( m, n, a, '  DIF2 matrix:' )

  value = dif2_determinant ( n )

  print ''
  print '  Value =  %g' % ( value )

  print ''
  print 'DIF2_DETERMINANT_TEST'
  print '  Normal end of execution.'

  return

def dif2_eigen_right ( n ):

#*****************************************************************************80
#
## DIF2_EIGEN_RIGHT returns the right eigenvectors of the DIF2 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    16 March 2015
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

def dif2_eigenvalues ( n ):

#*****************************************************************************80
#
## DIF2_EIGENVALUES returns the eigenvalues of the second difference matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    16 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, N, the number of rows and columns of A.
#
#    Output, real LAM(N), the eigenvalues.
#
  import numpy as np

  lam = np.zeros ( n )

  for i in range ( 0, n ):
    angle = float ( i + 1 ) * np.pi / float ( 2 * ( n + 1 ) )
    lam[i] = 4.0 * ( np.sin ( angle ) ) ** 2

  return lam

def dif2_inverse ( n ):

#*****************************************************************************80
#
## DIF2_INVERSE returns the inverse of the second difference matrix.
#
#  Formula:
#
#    if ( I <= J )
#      A(I,J) = I * (N-J+1) / (N+1)
#    else
#      A(I,J) = J * (N-I+1) / (N+1)
#
#  Example:
#
#    N = 4
#
#            4 3 2 1
#    (1/5) * 3 6 4 2
#            2 4 6 3
#            1 2 3 4
#
#  Properties:
#
#    A is symmetric: A' = A.
#
#    Because A is symmetric, it is normal.
#
#    Because A is normal, it is diagonalizable.
#
#    A is persymmetric: A(I,J) = A(N+1-J,N+1-I).
#
#    det ( A ) = 1 / ( N + 1 ).
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    17 March 2015
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

  a = np.zeros  ( ( n, n ) )

  for i in range ( 0, n ):
    for j in range ( 0, n ):
      if ( i <= j ):
        a[i,j] = float ( ( i + 1 ) * ( n - j ) ) / float ( n + 1 )
      else:
        a[i,j] = float ( ( j + 1 ) * ( n - i ) ) / float ( n + 1 )

  return a

def dif2_llt ( n ):

#*****************************************************************************80
#
## DIF2_LLT returns the Cholesky factor of the DIF2 matrix.
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
#    Input, integer N, the order of A.
#
#    Output, real A(N,N), the matrix.
#
  import numpy as np

  a = np.zeros ( ( n, n ) )

  for i in range ( 0, n ):
    a[i,i] = np.sqrt ( float ( i + 2 ) ) / np.sqrt ( float ( i + 1 ) )

  for i in range ( 1, n ):
    a[i,i-1] = - np.sqrt ( float ( i ) ) / np.sqrt ( float ( i + 1 ) )

  return a

def dif2_plu ( n ):

#*****************************************************************************80
#
## DIF2_PLU returns the PLU factors of the DIF2 matrix.
#
#  Discussion:
#
#    A = P * L * U
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
#    Input, integer N, the order of A.
#
#    Output, real P(N,N), L(N,N), U(N,N), the pivot
#    matrix, the unit lower triangular matrix, and the upper
#    triangular matrix that form the PLU factoriztion of A.
#
  import numpy as np

  p = np.zeros ( ( n, n ) )
  for i in range ( 0, n ):
    p[i,i] = 1.0

  l = np.zeros ( ( n, n ) )
  for i in range ( 0, n ):
    l[i,i] = 1.0
  for i in range ( 0, n - 1 ):
    l[i+1,i] = - float ( i + 1 ) / float ( i + 2 )

  u = np.zeros ( ( n, n ) )
  for i in range ( 0, n ):
    u[i,i] = float ( i + 2 ) / float ( i + 1 )
  for i in range ( 0, n - 1 ):
    u[i,i+1] = -1.0

  return p, l, u

def dif2_rhs ( m, k ):

#*****************************************************************************80
#
## DIF2_RHS returns the DIF2 right hand side.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    04 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, the row dimension.
#
#    Input, integer K, the column dimension ( should be 2).
#
#    Output, real B(M,K), the right hand side matrix.
#
  import numpy as np

  b = np.zeros ( ( m, k ) )

  if ( 1 <= k ):
    b[0,0]   = 1.0
    b[m-1,0] = 1.0

    if ( 2 <= k ):
      b[m-1,1] = float ( m + 1 )

  return b

def dif2_solution ( n, k ):

#*****************************************************************************80
#
## DIF2_SOLUTION returns the DIF2 solution matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    04 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the row dimension.
#
#    Input, integer K, the column dimension (should be 2).
#
#    Output, real X(N,K), the solution matrix.
#
  import numpy as np

  x = np.zeros ( ( n, k ) )

  if ( 1 <= k ):

    for i in range ( 0, n ):
      x[i,0] = 1.0

    if ( 2 <= k ):
      for i in range ( 0, n ):
        x[i,1] = float ( i + 1 )

  return x

def dif2_test ( ):

#*****************************************************************************80
#
## DIF2_TEST tests DIF2.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    21 January 2015
#
#  Author:
#
#    John Burkardt
#
  from r8mat_print import r8mat_print

  print ''
  print 'DIF2_TEST'
  print '  DIF2 computes the DIF2 matrix.'

  m = 5
  n = m

  a = dif2 ( m, n )
 
  r8mat_print ( m, n, a, '  DIF2 matrix:' )

  print ''
  print 'DIF2_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  dif2_test ( )
  timestamp ( )
