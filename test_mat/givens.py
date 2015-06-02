#! /usr/bin/env python
#
def givens ( m, n ):

#*****************************************************************************80
#
## GIVENS returns the GIVENS matrix.
#
#  Discussion:
#
#    Note that this is NOT the "Givens rotation matrix".  This
#    seems to be more commonly known as the Moler matrix%
#
#  Formula:
#
#    A(I,J) = 2 * min ( I, J ) - 1
#
#  Example:
#
#    N = 5
#
#    1 1 1 1 1
#    1 3 3 3 3
#    1 3 5 5 5
#    1 3 5 7 7
#    1 3 5 7 9
#
#  Rectangular Properties:
#
#    A is integral: int ( A ) = A.
#
#  Square Properties:
#
#    A is positive definite.
#
#    A is symmetric: A' = A.
#
#    Because A is symmetric, it is normal.
#
#    Because A is normal, it is diagonalizable.
#
#    The inverse of A is tridiagonal.
#
#    A has a simple Cholesky factorization.
#
#    A has eigenvalues
#
#      LAMBDA(I) = 0.5 * sec ( ( 2 * I - 1 ) * PI / ( 4 * N ) )^2
#
#    The condition number P(A) is approximately 16 N^2 / PI^2.
#
#    The family of matrices is nested as a function of N.
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
#  Reference:
#
#    Morris Newman, John Todd,
#    Example A9,
#    The evaluation of matrix inversion programs,
#    Journal of the Society for Industrial and Applied Mathematics,
#    Volume 6, Number 4, pages 466-476, 1958.
#
#    John Todd,
#    Example A9,
#    Basic Numerical Mathematics, Volume 2: Numerical Algebra,
#    Academic Press, New York, 1977, page 1.
#
#    Joan Westlake,
#    Test Matrix A8,
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

  a = np.zeros ( ( m, n ) )

  for i in range ( 0, m ):
    for j in range ( 0, n ):
      a[i,j] = 2 * min ( i, j ) + 1

  return a

def givens_condition ( n ):

#*****************************************************************************80
#
## GIVENS_CONDITION computes the L1 condition of the GIVENS matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 April 2015
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
  import numpy as np

  a_norm = float ( n * n )

  if ( n == 1 ):
    b_norm = 1.0
  else:
    b_norm = 2.0

  value = a_norm * b_norm

  return value

def givens_determinant ( n ):

#*****************************************************************************80
#
## GIVENS_DETERMINANT computes the determinant of the GIVENS matrix.
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
#    Output, real VALUE, the determinant.
#
  import numpy as np

  r8_pi = 3.141592653589793

  value = 1.0

  for i in range ( 1, n + 1 ):
    angle = float ( 2 * i - 1 ) * r8_pi / float ( 4 * n )
    value = value * 0.5 / ( np.cos ( angle ) ) ** 2

  return value

def givens_determinant_test ( ):

#*****************************************************************************80
#
## GIVENS_DETERMINANT_TEST tests GIVENS_DETERMINANT.
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
  from givens import givens
  from r8mat_print import r8mat_print

  print ''
  print 'GIVENS_DETERMINANT_TEST'
  print '  GIVENS_DETERMINANT computes the GIVENS determinant.'

  m = 5
  n = m
 
  a = givens ( m, n )

  r8mat_print ( m, n, a, '  GIVENS matrix:' )

  value = givens_determinant ( n )

  print '  Value =  %g' % ( value )

  print ''
  print 'GIVENS_DETERMINANT_TEST'
  print '  Normal end of execution.'

  return

def givens_eigenvalues ( n ):

#*****************************************************************************80
#
## GIVENS_EIGENVALUES returns the eigenvalues of the GIVENS matrix.
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
#    Input, integer N, the order of the matrix.
#
#    Output, real LAMBDA(N), the eigenvalues.
#
  import numpy as np

  lam = np.zeros ( n )

  for i in range ( 0, n ):
    angle = float ( 2 * i + 1 ) * np.pi / float ( 4 * n )
    lam[i] = 0.5 / ( np.cos ( angle ) ) ** 2

  return lam

def givens_inverse ( n ):

#*****************************************************************************80
#
## GIVENS_INVERSE returns the inverse of the GIVENS matrix.
#
#  Formula:
#
#    if ( I = J = 1 )
#      A(I,J) = 1.5
#    elseif ( I = J < N )
#      A(I,J) = 1.0
#    elseif ( I = J = N )
#      A(I,J) = 0.5
#    elseif ( J = I+1 or J = I-1 )
#      A(I,J) = -0.5
#    else
#      A(I,J) = 0
#
#  Example:
#
#    N = 5
#
#           3 -1  0  0  0
#          -1  2 -1  0  0
#    1/2 *  0 -1  2 -1  0
#           0  0 -1  2 -1
#           0  0  0 -1  1
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
        if ( i == 0 ):
          a[i,j] = 1.5
        elif ( i < n - 1 ):
          a[i,j] = 1.0
        else:
          a[i,j] = 0.5
      elif ( i == j + 1 ):
        a[i,j] = - 0.5
      elif ( i == j - 1 ):
        a[i,j] = - 0.5

  return a

def givens_llt ( n ):

#*****************************************************************************80
#
## GIVENS_LLT returns the Cholesky factor of the GIVENS matrix.
#
#  Example:
#
#    N = 5
#
#    1    0        0        0       0
#    1  sqrt(2)    0        0       0
#    1  sqrt(2)  sqrt(2)    0       0
#    1  sqrt(2)  sqrt(2)  sqrt(2)   0
#    1  sqrt(2)  sqrt(2)  sqrt(2) sqrt(2)
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
#    Input, integer N, the order of the matrix.
#
#    Output, real A(N,N), the matrix.
#
  import numpy as np

  a = np.zeros ( ( n, n ) )

  j = 0
  for i in range ( 0, n ):
    a[i,j] = 1.0

  for j in range ( 1, n ):
    for i in range ( j, n ):
      a[i,j] = np.sqrt ( 2.0 )

  return a

def givens_plu ( n ):

#*****************************************************************************80
#
#% GIVENS_PLU returns the PLU factors of the GIVENS matrix.
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

  p = np.zeros ( ( n, n ) )

  for j in range ( 0, n ):
    p[j,j] = 1.0

  l = np.zeros ( ( n, n ) )

  for j in range ( 0, n ):
    for i in range ( j, n ):
      l[i,j] = 1.0

  u = np.zeros ( ( n, n ) )

  i = 0
  for j in range ( 0, n ):
    u[i,j] = 1.0

  for i in range ( 1, n ):
    for j in range ( i, n ):
      u[i,j] = 2.0

  return p, l, u

def givens_test ( ):

#*****************************************************************************80
#
## GIVENS_TEST tests GIVENS.
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
  from r8mat_print import r8mat_print

  print ''
  print 'GIVENS_TEST'
  print '  GIVENS computes the GIVENS matrix.'

  m = 5
  n = m

  a = givens ( m, n )
 
  r8mat_print ( m, n, a, '  GIVENS matrix:' )

  print ''
  print 'GIVENS_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  givens_test ( )
  timestamp ( )
