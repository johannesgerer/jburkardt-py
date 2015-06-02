#! /usr/bin/env python
#
def rodman ( m, n, alpha ):

#*****************************************************************************80
#
## RODMAN returns the RODMAN matrix.
#
#  Formula:
#
#    If ( I = J )
#      A(I,J) = 1
#    else
#      A(I,J) = ALPHA
#
#  Example:
#
#    M = 5, N = 5, ALPHA = 2
#
#    1 2 2 2 2
#    2 1 2 2 2
#    2 2 1 2 2
#    2 2 2 1 2
#    2 2 2 2 1
#
#  Properties:
#
#    A is a special case of the combinatorial matrix.
#
#    A is Toeplitz: constant along diagonals.
#
#    A is a circulant matrix: each row is shifted once to get the next row.
#
#    A has constant row sum.
#
#    Because it has a constant row sum of 1+(N-1)*ALPHA,
#    A has an eigenvalue of 1+(N-1)*ALPHA, and
#    a (right) eigenvector of ( 1, 1, 1, ..., 1 ).
#
#    A has constant column sum.
#
#    Because it has a constant column sum of 1+(N-1)*ALPHA,
#    A has an eigenvalue of 1+(N-1)*ALPHA, and
#    a (left) eigenvector of ( 1, 1, 1, ..., 1 ).
#
#    A is symmetric: A' = A.
#
#    Because A is symmetric, it is normal.
#
#    Because A is normal, it is diagonalizable.
#
#    A is persymmetric: A(I,J) = A(N+1-J,N+1-I).
#
#    A is centrosymmetric: A(I,J) = A(N+1-I,N+1-J).
#
#    A is positive definite for ALPHA < 1.
#
#    The eigenvalues and eigenvectors of A are:
#
#      For I = 1 to N-1:
#
#        LAMBDA(I) = 1 - ALPHA
#        V(I) = ( - sum ( 2 <= J <= N ) X(J), X(2), X(3), ..., X(N) )
#
#      For I = N:
#
#        LAMBDA(I) = 1 + ALPHA * ( N - 1 )
#        V(I) = ( 1, 1, 1, ..., 1 )
#
#    det ( A ) = ( 1 - ALPHA )^(N-1) * ( 1 + ALPHA * ( N - 1 ) ).
#
#    A is nonsingular if ALPHA is not 1, and ALPHA is not -1/(N-1).
#
#    The inverse of A is known.
#
#    The family of matrices is nested as a function of N.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    23 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
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
#    Input, integer M, N, the order of the matrix.
#
#    Input, real ALPHA, the parameter.
#
#    Output, real A(M,N), the matrix.
#
  import numpy as np

  a = np.zeros ( ( m, n ) )

  for i in range ( 0, m ):
    for j in range ( 0, n ):
      if ( i == j ):
        a[i,j] = 1.0
      else:
        a[i,j] = alpha

  return a

def rodman_condition ( n, alpha ):

#*****************************************************************************80
#
## RODMAN_CONDITION computes the L1 condition of the RODMAN matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    04 April 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the order of the matrix.
#
#    Input, real ALPHA, the parameter.
#
#    Output, real VALUE, the L1 condition.
#
  a_norm = 1.0 + float ( n - 1 ) * abs ( alpha )

  top = abs ( 1.0 + alpha * float ( n - 2 ) ) \
    + float ( n - 1 ) * abs ( alpha )

  bot = abs ( 1.0 + alpha * float ( n - 2 ) \
    - alpha * alpha * float ( n - 1 ) )

  b_norm = top / bot

  value = a_norm * b_norm

  return value

def rodman_determinant ( n, alpha ):

#*****************************************************************************80
#
## RODMAN_DETERMINANT computes the determinant of the RODMAN matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    23 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the order of the matrix.
#
#    Input, real ALPHA, the parameter.
#
#    Output, real VALUE, the determinant.
#
  value = ( 1.0 - alpha ) ** ( n - 1 ) * ( 1.0 + alpha * float ( n - 1 ) )

  return value

def rodman_determinant_test ( ):

#*****************************************************************************80
#
## RODMAN_DETERMINANT_TEST tests RODMAN_DETERMINANT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    23 February 2015
#
#  Author:
#
#    John Burkardt
#
  from rodman import rodman
  from r8_uniform_ab import r8_uniform_ab
  from r8mat_print import r8mat_print

  print ''
  print 'RODMAN_DETERMINANT_TEST'
  print '  RODMAN_DETERMINANT computes the RODMAN determinant.'

  m = 5
  n = m
 
  r8_lo = -5.0
  r8_hi = +5.0
  seed = 123456789
  alpha, seed = r8_uniform_ab ( r8_lo, r8_hi, seed )

  a = rodman ( m, n, alpha )

  r8mat_print ( m, n, a, '  RODMAN matrix:' )

  value = rodman_determinant ( n, alpha )

  print ''
  print '  Value =  %g' % ( value )

  print ''
  print 'RODMAN_DETERMINANT_TEST'
  print '  Normal end of execution.'

  return

def rodman_eigen_right ( n, alpha ):

#*****************************************************************************80
#
## RODMAN_EIGEN_RIGHT returns the right eigenvectors of the RODMAN matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    19 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the order of the matrix.
#
#    Input, real ALPHA, the parameter.
#
#    Output, real X(N,N), the right eigenvectors.
#
  import numpy as np

  x = np.zeros ( ( n, n ) )

  for j in range ( 0, n - 1 ):
    x[  0,j] = +1.0
    x[j+1,j] = -1.0

  for i in range ( 0, n ):
    x[i,n-1] = 1.0

  return x

def rodman_eigenvalues ( n, alpha ):

#*****************************************************************************80
#
## RODMAN_EIGENVALUES returns the eigenvalues of the RODMAN matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    19 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the order of A.
#
#    Input, real ALPHA, the parameter.
#
#    Output, real LAM(N), the eigenvalues.
#
  import numpy as np

  lam = np.zeros ( n )

  for i in range ( 0, n - 1 ):
    lam[i] = 1.0 - alpha

  lam[n-1] = 1.0 + alpha * float ( n - 1 )

  return lam

def rodman_inverse ( n, alpha ):

#*****************************************************************************80
#
## RODMAN_INVERSE returns the inverse of the RODMAN matrix.
#
#  Formula:
#
#    If ( I = J )
#      A(I,J) = ( 1 + ALPHA * ( N - 2 ) ) /
#        ( 1 + ALPHA * ( N - 2 ) - ALPHA^2 * ( N - 1 ) )
#    else
#      A(I,J) = - ALPHA /
#        ( 1 + ALPHA * ( N - 2 ) - ALPHA^2 * ( N - 1 ) )
#
#  Example:
#
#    N = 5, ALPHA = 2.0
#
#   -0.7778    0.2222    0.2222    0.2222    0.2222
#    0.2222   -0.7778    0.2222    0.2222    0.2222
#    0.2222    0.2222   -0.7778    0.2222    0.2222
#    0.2222    0.2222    0.2222   -0.7778    0.2222
#    0.2222    0.2222    0.2222    0.2222   -0.7778
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
#    Joan Westlake,
#    A Handbook of Numerical Matrix Inversion and Solution of 
#    Linear Equations,
#    John Wiley, 1968,
#    ISBN13: 978-0471936756,
#    LC: QA263.W47.
#
#  Parameters:
#
#    Input, integer N, the order of the matrix.
#
#    Input, real ALPHA, the parameter.
#
#    Output, real A(N,N), the matrix.
#
  import numpy as np

  a = np.zeros ( ( n, n ) )

  bot = 1.0 + alpha * float ( n - 2 ) - alpha * alpha * float ( n - 1 )

  for i in range ( 0, n ):
    for j in range ( 0, n ):

      if ( i == j ):
        a[i,j] = ( 1.0 + alpha * float ( n - 2 ) ) / bot
      else:
        a[i,j] = - alpha / bot

  return a

def rodman_test ( ):

#*****************************************************************************80
#
## RODMAN_TEST tests RODMAN.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    23 February 2015
#
#  Author:
#
#    John Burkardt
#
  from r8_uniform_ab import r8_uniform_ab
  from r8mat_print import r8mat_print

  print ''
  print 'RODMAN_TEST'
  print '  RODMAN computes the RODMAN matrix.'

  m = 5
  n = m

  r8_lo = -5.0
  r8_hi = +5.0
  seed = 123456789
  alpha, seed = r8_uniform_ab ( r8_lo, r8_hi, seed )

  a = rodman ( m, n, alpha )
 
  r8mat_print ( m, n, a, '  RODMAN matrix:' )

  print ''
  print 'RODMAN_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  rodman_test ( )
  timestamp ( )
