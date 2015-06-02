#! /usr/bin/env python
#
def exchange ( m, n ):

#*****************************************************************************80
#
## EXCHANGE returns the EXCHANGE matrix.
#
#  Formula:
#
#    if ( I + J = N + 1 )
#      A(I,J) = 1
#    else
#      A(I,J) = 0
#
#  Example:
#
#    M = 4, N = 5
#
#    0 0 0 0 1
#    0 0 0 1 0
#    0 0 1 0 0
#    0 1 0 0 0
#
#    M = 5, N = 5
#
#    0 0 0 0 1
#    0 0 0 1 0
#    0 0 1 0 0
#    0 1 0 0 0
#    1 0 0 0 0
#
#  Rectangular properties:
#
#    A is integral: int ( A ) = A.
#
#    A is a zero/one matrix.
#
#  Square Properties:
#
#    A is nonsingular.
#
#    A is a permutation matrix.
#
#    A has property A.
#
#    A is symmetric: A' = A.
#
#    Because A is symmetric, it is normal.
#
#    Because A is normal, it is diagonalizable.
#
#    A is persymmetric: A(I,J) = A(N+1-J,N+1-I).
#
#    A is a Hankel matrix: constant along anti-diagonals.
#
#    A is involutional: A * A = I.
#
#    A is a square root of the identity matrix.
#
#    A is orthogonal: A' * A = A * A' = I.
#
#    det ( A ) = ( -1 )^(N/2).
#
#    There are N/2 eigenvalues of -1, and (N+1)/2 eigenvalues of 1.
#
#    For each pair of distinct vector indices I1 and I2 that sum to N+1, there
#    is an eigenvector which has a 1 in the I1 and I2 positions and 0 elsewhere,
#    and there is an eigenvector for -1, with a 1 in the I1 position and a -1
#    in the I2 position.  If N is odd, then there is a single eigenvector
#    associated with the index I1 = (N+1)/2, having a 1 in that index and zero
#    elsewhere, associated with the eigenvalue 1.
#
#    The exchange matrix is also called the "counter-identity matrix".
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
#    Input, integer M, N, the number of rows and columns 
#    of the matrix.
#
#    Output, real A(M,N), the matrix.
#
  import numpy as np

  a = np.zeros ( [ m, n ] )

  for i in range ( 0, m ):
    for j in range ( 0, n ):
      if ( i + j == n - 1 ):
        a[i,j] = 1.0

  return a

def exchange_condition ( n ):

#*****************************************************************************80
#
## EXCHANGE_CONDITION returns the L1 condition of the EXCHANGE matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 February 2015
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
  a_norm = 1;
  b_norm = 1;
  value = a_norm * b_norm;

  return value

def exchange_condition_test ( ):

#*****************************************************************************80
#
## EXCHANGE_CONDITION_TEST tests EXCHANGE_CONDITION.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 February 2015
#
#  Author:
#
#    John Burkardt
#
  from exchange import exchange
  from r8mat_print import r8mat_print
 
  print ''
  print 'EXCHANGE_CONDITION_TEST'
  print '  EXCHANGE_CONDITION computes the condition of the EXCHANGE matrix.'
  print ''

  m = 4
  n = m

  a = exchange ( m, n )
  r8mat_print ( m, n, a, '  EXCHANGE matrix:' )

  value = exchange_condition ( n )

  print ''
  print '  Value =  %g' % ( value )

  print ''
  print 'EXCHANGE_CONDITION_TEST'
  print '  Normal end of execution.'

  return

def exchange_determinant ( n ):

#*****************************************************************************80
#
## EXCHANGE_DETERMINANT returns the determinant of the EXCHANGE matrix.
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
  n2 = ( n // 2 )

  if ( ( n2 % 2 ) == 0 ):
    value = 1.0
  else:
    value = -1.0

  return value

def exchange_determinant_test ( ):

#*****************************************************************************80
#
## EXCHANGE_DETERMINANT_TEST tests EXCHANGE_DETERMINANT.
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
  from exchange import exchange
  from r8mat_print import r8mat_print
 
  print ''
  print 'EXCHANGE_DETERMINANT_TEST'
  print '  EXCHANGE_DETERMINANT computes the determinant of the EXCHANGE matrix.'
  print ''

  m = 4
  n = m

  a = exchange ( m, n )
  r8mat_print ( m, n, a, '  EXCHANGE matrix:' )

  value = exchange_determinant ( n )

  print ''
  print '  Value =  %g' % ( value )

  print ''
  print 'EXCHANGE_DETERMINANT_TEST'
  print '  Normal end of execution.'

  return

def exchange_eigen_right ( n ):

#*****************************************************************************80
#
## EXCHANGE_EIGEN_RIGHT returns the right eigenvectors of the EXCHANGE matrix.
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
#    Output, real X(N,N), the eigenvector matrix.
#
  import numpy as np

  x = np.zeros ( ( n, n ) )

  n2 = ( n // 2 )

  for j in range ( 0, n2 ):

    i = n - 1 - j

    x[j,j] =  1.0
    x[i,j] = -1.0

    x[j,i] =  1.0
    x[i,i] =  1.0

  if ( ( n % 2 ) == 1 ):
    x[n2,n2] = 1.0

  return x

def exchange_eigenvalues ( n ):

#*****************************************************************************80
#
## EXCHANGE_EIGENVALUES returns the eigenvalues of the exchange matrix.
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
#    Output, real LAM(N), the eigenvalues.
#
  import numpy as np

  lam = np.zeros ( n )

  n2 = ( n // 2 )

  for i in range ( 0, n2 ):
    lam[i] = -1.0
  for i in range ( n2, n ):
    lam[i] = +1.0

  return lam

def exchange_inverse ( n ):

#*****************************************************************************80
#
## EXCHANGE_INVERSE returns the inverse of the exchange matrix.
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
  a = exchange ( n, n )

  return a

def exchange_test ( ):

#*****************************************************************************80
#
## EXCHANGE_TEST tests EXCHANGE.
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
  print 'EXCHANGE_TEST'
  print '  EXCHANGE computes the EXCHANGE matrix.'

  m = 4
  n = m

  a = exchange ( m, n )
  r8mat_print ( m, n, a, '  EXCHANGE matrix:' )

  print ''
  print 'EXCHANGE_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  exchange_test ( )
  timestamp ( )
