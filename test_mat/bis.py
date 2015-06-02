#! /usr/bin/env python
#
def bis ( alpha, beta, m, n ):

#*****************************************************************************80
#
## BIS returns the BIS matrix.
#
#  Discussion:
#
#    BIS is a bidiagonal scalar matrix.
#
#  Formula:
#
#    if ( I = J )
#      A(I,J) = ALPHA
#    else if ( J = I+1 )
#      A(I,J) = BETA
#    else
#      A(I,J) = 0
#
#  Example:
#
#    ALPHA = 7, BETA = 2, M = 5, N = 4
#
#    7  2  0  0
#    0  7  2  0
#    0  0  7  2
#    0  0  0  7
#    0  0  0  0
#
#  Rectangular Properties:
#
#    A is bidiagonal.
#
#    Because A is bidiagonal, it has property A (bipartite).
#
#    A is upper triangular.
#
#    A is banded with bandwidth 2.
#
#    A is Toeplitz: constant along diagonals.
#
#  Square Properties:
#
#    A is generally not symmetric: A' /= A.
#
#    A is nonsingular if and only if ALPHA is nonzero.
#
#    det ( A ) = ALPHA^N.
#
#    LAMBDA(1:N) = ALPHA.
#
#    A is persymmetric: A(I,J) = A(N+1-J,N+1-I).
#
#    The family of matrices is nested as a function of N.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    21 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real ALPHA, BETA, the scalars which define the
#    diagonal and first superdiagonal of the matrix.
#
#    Input, integer M, N, the number of rows and columns of A.
#
#    Output, real A(M,N), the matrix.
#
  import numpy as np

  a = np.zeros ( [ m, n ] )
  
  for i in range ( 0, m ):
    for j in range ( 0, n ):

      if ( j == i ):
        a[i,j] = alpha
      elif ( j == i + 1 ):
        a[i,j] = beta
      else:
        a[i,j] = 0.0

  return a

def bis_condition ( alpha, beta, n ):

#*****************************************************************************80
#
## BIS_CONDITION computes the L1 condition of the BIS matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real ALPHA, BETA, the scalars which define the
#    diagonal and first superdiagonal of the matrix.
#
#    Input, integer N, the order of the matrix.
#
#    Output, real VALUE, the L1 condition.
#
  a_norm = abs ( alpha ) + abs ( beta )
  ba = abs ( beta / alpha )
  b_norm = ( ba ** n - 1.0 ) / ( ba - 1.0 ) / abs ( alpha )
  value = a_norm * b_norm

  return value

def bis_condition_test ( ):

#*****************************************************************************80
#
## BIS_CONDITION_TEST tests BIS_CONDITION.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    20 January 2015
#
#  Author:
#
#    John Burkardt
#
  from r8_uniform_01 import r8_uniform_01
  from r8mat_print import r8mat_print

  print ''
  print 'BIS_CONDITION_TEST'
  print '  BIS_CONDITION computes the BIS condition.'

  seed = 123456789

  n = 5
  alpha, seed = r8_uniform_01 ( seed )
  beta, seed = r8_uniform_01 ( seed )
  a = bis ( alpha, beta, n, n )
  r8mat_print ( n, n, a, '  BIS matrix:' )

  value = bis_condition ( alpha, beta, n )
  print '  Value =  %g' % ( value )

  print ''
  print 'BIS_CONDITION_TEST'
  print '  Normal end of execution.'

  return

def bis_determinant ( alpha, beta, n ):

#*****************************************************************************80
#
## BIS_DETERMINANT computes the determinant of the BIS matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    21 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real ALPHA, BETA, the scalars which define the
#    diagonal and first superdiagonal of the matrix.
#
#    Input, integer N, the order of the matrix.
#
#    Output, real DETERM, the determinant.
#
  determ = alpha ** n

  return determ

def bis_determinant_test ( ):

#*****************************************************************************80
#
## BIS_DETERMINANT_TEST tests BIS_DETERMINANT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    21 December 2014
#
#  Author:
#
#    John Burkardt
#
  from r8_uniform_01 import r8_uniform_01
  from r8mat_print import r8mat_print

  print ''
  print 'BIS_DETERMINANT_TEST'
  print '  BIS_DETERMINANT computes the BIS determinant.'

  seed = 123456789

  n = 5
  alpha, seed = r8_uniform_01 ( seed )
  beta, seed = r8_uniform_01 ( seed )
  a = bis ( alpha, beta, n, n )
  r8mat_print ( n, n, a, '  BIS matrix:' )

  value = bis_determinant ( alpha, beta, n )
  print '  Value =  %g' % ( value )

  print ''
  print 'BIS_DETERMINANT_TEST'
  print '  Normal end of execution.'

  return

def bis_inverse ( alpha, beta, n ):

#*****************************************************************************80
#
#% BIS_INVERSE returns the inverse of a bidiagonal scalar matrix.
#
#  Formula:
#
#    if ( I <= J )
#      A(I,J) = (-BETA)^(J-I) / ALPHA^(J+1-I)
#    else
#      A(I,J) = 0
#
#  Example:
#
#    ALPHA = 7.0, BETA = 2.0, N = 4
#
#    0.1429   -0.0408    0.0117   -0.0033
#        0     0.1429   -0.0408    0.0117
#        0          0    0.1429   -0.0408
#        0          0         0    0.1429
#
#  Properties:
#
#    A is generally not symmetric: A' /= A.
#
#    A is upper triangular
#
#    A is Toeplitz: constant along diagonals.
#
#    A is persymmetric: A(I,J) = A(N+1-J,N+1-I).
#
#    det ( A ) = (1/ALPHA)^N.
#
#    LAMBDA(1:N) = 1 / ALPHA.
#
#    The family of matrices is nested as a function of N.
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
#    Input, real ALPHA, BETA, the scalars which define the
#    diagonal and first superdiagonal of the matrix.
#
#    Input, integer N, the order of A.
#
#    Output, real A(N,N), the matrix.
#
  import numpy as np
  from sys import exit

  a = np.zeros ( ( n, n ) )

  if ( alpha == 0.0 ):
    print ''
    print 'BIS_INVERSE - Fatal error!'
    print '  The input parameter ALPHA was 0.'
    exit ( 'BIS_INVERSE - Fatal error!' )

  for i in range ( 0, n ):
    for j in range ( 0, n ):

      if ( i <= j ):
        a[i,j] = ( - beta ) ** ( j - i ) / alpha ** ( j - i + 1 )

  return a

def bis_test ( ):

#*****************************************************************************80
#
## BIS_TEST tests BIS.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    21 December 2014
#
#  Author:
#
#    John Burkardt
#
  from r8_uniform_01 import r8_uniform_01
  from r8mat_print import r8mat_print

  print ''
  print 'BIS_TEST'
  print '  BIS computes the BIS matrix.'

  seed = 123456789

  m = 5
  n = 5
  alpha, seed = r8_uniform_01 ( seed )
  beta, seed = r8_uniform_01 ( seed )
  a = bis ( alpha, beta, m, n )
  r8mat_print ( m, n, a, '  BIS matrix:' )

  print ''
  print 'BIS_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  bis_test ( )
  timestamp ( )
