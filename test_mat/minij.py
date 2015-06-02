#! /usr/bin/env python
#
def minij ( m, n ):

#*****************************************************************************80
#
## MINIJ returns the MINIJ matrix.
#
#  Formula:
#
#    A(I,J) = min ( I, J )
#
#  Example:
#
#    N = 5
#
#    1 1 1 1 1
#    1 2 2 2 2
#    1 2 3 3 3
#    1 2 3 4 4
#    1 2 3 4 5
#
#  Properties:
#
#    A is integral, therefore det ( A ) is integral, and 
#    det ( A ) * inverse ( A ) is integral.
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
#    The eigenvalues of A are
#
#      LAMBDA(I) = 0.5 / ( 1 - cos ( ( 2 * I - 1 ) * pi / ( 2 * N + 1 ) ) ),
#
#    For N = 12, the characteristic polynomial is
#      P(X) = X^12 - 78 X^11 + 1001 X^10 - 5005 X^9 + 12870 X^8
#        - 19448 X^7 + 18564 X^6 - 11628 X^5 + 4845 X^4 - 1330 X^3
#        + 231 X^2 - 23 X + 1.
#
#    (N+1)*ONES(N) - A also has a tridiagonal inverse.
#
#    Gregory and Karney consider the matrix defined by
#
#      B(I,J) = N + 1 - MAX(I,J)
#
#    which is equal to the MINIJ matrix, but with the rows and
#    columns reversed.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    05 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Robert Gregory, David Karney,
#    Example 3.12, Example 4.14,
#    A Collection of Matrices for Testing Computational Algorithms,
#    Wiley, 1969, page 41, page 74, 
#    LC: QA263.G68.
#
#    Daniel Rutherford,
#    Some continuant determinants arising in physics and chemistry II,
#    Proceedings of the Royal Society Edinburgh,
#    Volume 63, A, 1952, pages 232-241.
#
#    John Todd,
#    Basic Numerical Mathematics, Vol. 2: Numerical Algebra,
#    Academic Press, 1977, page 158.
#
#    Joan Westlake,
#    A Handbook of Numerical Matrix Inversion and Solution of 
#    Linear Equations,
#    John Wiley, 1968,
#    ISBN13: 978-0471936756,
#    LC: QA263.W47.
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

      a[i,j] = min ( i, j ) + 1

  return a

def minij_condition ( n ):

#*****************************************************************************80
#
## MINIJ_CONDITION returns the L1 condition of the MINIJ matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    05 February 2015
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
  a_norm = float ( n * ( n + 1 ) ) / 2.0
  if ( n == 1 ):
    b_norm = 1.0
  elif ( n == 2 ):
    b_norm = 3.0
  else:
    b_norm = 4.0

  value = a_norm * b_norm

  return value

def minij_condition_test ( ):

#*****************************************************************************80
#
## MINIJ_CONDITION_TEST tests MINIJ_CONDITION.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    05 February 2015
#
#  Author:
#
#    John Burkardt
#
  from minij import minij
  from r8mat_print import r8mat_print

  print ''
  print 'MINIJ_CONDITION_TEST'
  print '  MINIJ_CONDITION computes the condition of the MINIJ matrix.'
  print ''

  n = 4
  a = minij ( n, n )
  r8mat_print ( n, n, a, '  MINIJ matrix:' )

  value = minij_condition ( n )

  print ''
  print '  Value =  %g' % ( value )

  print ''
  print 'MINIJ_CONDITION_TEST'
  print '  Normal end of execution.'

  return

def minij_determinant ( n ):

#*****************************************************************************80
#
## MINIJ_DETERMINANT returns the determinant of the MINIJ matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    05 February 2015
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

  for i in range ( 0, n ):
    angle = float ( 2 * i + 1 ) * r8_pi / float ( 2 * n + 1 )
    value = value * 0.5 / ( 1.0 - np.cos ( angle ) )

  return value

def minij_determinant_test ( ):

#*****************************************************************************80
#
## MINIJ_DETERMINANT_TEST tests MINIJ_DETERMINANT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    05 February 2015
#
#  Author:
#
#    John Burkardt
#
  from minij import minij
  from r8mat_print import r8mat_print

  print ''
  print 'MINIJ_DETERMINANT_TEST'
  print '  MINIJ_DETERMINANT computes the determinant of the MINIJ matrix.'
  print ''

  n = 4
  a = minij ( n, n )
  r8mat_print ( n, n, a, '  MINIJ matrix:' )

  value = minij_determinant ( n )

  print ''
  print '  Value =  %g' % ( value )

  print ''
  print 'MINIJ_DETERMINANT_TEST'
  print '  Normal end of execution.'

  return

def minij_eigenvalues ( n ):

#*****************************************************************************80
#
## MINIJ_EIGENVALUES returns the eigenvalues of the MINIJ matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    16 October 2007
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

  lam = zeros ( n, 1 );

  for i in range ( 0, n ):
    angle = float ( 2 * i + 1 ) * np.pi / float ( 2 * n + 1 )
    lam[i] = 0.5 / ( 1.0 - np.cos ( angle ) )

  return lam

def minij_inverse ( n ):

#*****************************************************************************80
#
## MINIJ_INVERSE returns the inverse of the MINIJ matrix.
#
#  Formula:
#
#    A(I,J) =  -1  if J=I-1 or J=I+1
#    A(I,J) =   2  if J=I and J is not N.
#    A(I,J) =   1  if J=I and J=N.
#    A(I,J) =   0  otherwise
#
#  Example:
#
#    N = 5
#
#     2 -1  0  0  0
#    -1  2 -1  0  0
#     0 -1  2 -1  0
#     0  0 -1  2 -1
#     0  0  0 -1  1
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
#    A is integral, therefore det ( A ) is integral, and 
#    det ( A ) * inverse ( A ) is integral.
#
#    A is "almost" equal to the second difference matrix,
#    as computed by DIF.
#
#    The family of matrices is nested as a function of N.
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

      if ( i == j ):
        if ( i < n - 1 ):
          a[i,j] = 2.0
        else:
          a[i,j] = 1.0
      elif ( i == j + 1 or i == j - 1 ):
        a[i,j] = -1.0
 
  return a

def minij_llt ( n ):

#*****************************************************************************80
#
## MINIJ_LLT returns the Cholesky factor of the MINIJ matrix.
#
#  Example:
#
#    N = 5
#
#    1  0  0  0  0
#    1  1  0  0  0
#    1  1  1  0  0
#    1  1  1  1  0
#    1  1  1  1  1
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
#    Output, real A(N,N), the matrix.
#
  import numpy as np

  a = np.zeros ( ( n, n ) )

  for i in range ( 0, n ):
    for j in range ( 0, i + 1 ):
      a[i,j] = 1.0

  return a

def minij_plu ( n ):

#*****************************************************************************80
#
## MINIJ_PLU returns the PLU factors of the MINIJ matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 June 2011
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the order of the matrix.
#
#    Output, real P(N,N), L(N,N), U(N,N) the PLU factors.
#
  import numpy as np

  p = np.zeros ( ( n, n ) )
  for j in range ( 0, n ):
    for i in range ( 0, n ):
      if ( i == j ):
        p[i,j] = 1.0

  l = np.zeros ( ( n, n ) )
  for j in range ( 0, n ):
    for i in range ( j, n ):
      l[i,j] = 1.0

  u = np.zeros ( ( n, n ) )
  for j in range ( 0, n ):
    for i in range ( 0, j + 1 ):
      u[i,j] = 1.0

  return p, l, u

def minij_test ( ):

#*****************************************************************************80
#
## MINIJ_TEST tests MINIJ.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    05 February 2015
#
#  Author:
#
#    John Burkardt
#
  from r8mat_print import r8mat_print

  print ''
  print 'MINIJ_TEST'
  print '  MINIJ computes the MINIJ matrix.'

  m = 5
  n = 5
  a = minij ( m, n )
  r8mat_print ( m, n, a, '  MINIJ matrix:' )

  print ''
  print 'MINIJ_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  minij_test ( )
  timestamp ( )
