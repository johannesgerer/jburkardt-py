#! /usr/bin/env python
#
def jordan ( m, n, alpha ):

#*****************************************************************************80
#
## JORDAN returns the JORDAN matrix.
#
#  Formula:
#
#    if ( I = J )
#      A(I,J) = ALPHA
#    else if ( I = J-1 )
#      A(I,J) = 1
#    else
#      A(I,J) = 0
#
#  Example:
#
#    ALPHA = 2, M = 5, N = 5
#
#    2  1  0  0  0
#    0  2  1  0  0
#    0  0  2  1  0
#    0  0  0  2  1
#    0  0  0  0  2
#
#  Properties:
#
#    A is upper triangular.
#
#    A is lower Hessenberg.
#
#    A is bidiagonal.
#
#    Because A is bidiagonal, it has property A (bipartite).
#
#    A is banded, with bandwidth 2.
#
#    A is generally not symmetric: A' /= A.
#
#    A is persymmetric: A(I,J) = A(N+1-J,N+1-I).
#
#    A is nonsingular if and only if ALPHA is nonzero.
#
#    det ( A ) = ALPHA^N.
#
#    LAMBDA(I) = ALPHA.
#
#    A is defective, having only one eigenvector, namely (1,0,0,...,0).
#
#    The family of matrices is nested as a function of N.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    16 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, N, the number of rows and columns of A.
#
#    Input, real ALPHA, the eigenvalue of the Jordan matrix.
#
#    Output, real A(M,N), the matrix.
#
  import numpy as np

  a = np.zeros ( ( m, n ) )

  for i in range ( 0, m ):
    for j in range ( 0, n ):

      if ( i == j ):
        a[i,j] = alpha
      elif ( j == i + 1 ):
        a[i,j] = 1.0

  return a

def jordan_condition ( n, alpha ):

#*****************************************************************************80
#
## JORDAN_CONDITION returns the L1 condition of the JORDAN matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    16 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the order of the matrix.
#
#    Input, real ALPHA, the eigenvalue of the Jordan matrix.
#
#    Output, real VALUE, the L1 condition number.
#
  a2 = abs ( alpha )

  if ( n == 1 ):
    a_norm = a2
  else:
    a_norm = a2 + 1.0

  if ( a2 == 1.0 ):
    b_norm = float ( n ) * a2
  else:
    b_norm = ( a2 ** n - 1.0 ) / ( a2 - 1.0 ) / a2 ** n

  value = a_norm * b_norm

  return value

def jordan_condition_test ( ):

#*****************************************************************************80
#
## JORDAN_CONDITION_TEST tests JORDAN_CONDITION.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    16 February 2015
#
#  Author:
#
#    John Burkardt
#
  from jordan import jordan
  from r8_uniform_01 import r8_uniform_01
  from r8mat_print import r8mat_print

  print ''
  print 'JORDAN_CONDITION_TEST'
  print '  JORDAN_CONDITION computes the condition of the JORDAN matrix.'
  print ''

  seed = 123456789

  m = 5
  n = m
  alpha, seed = r8_uniform_01 ( seed )
  a = jordan ( m, n, alpha )
  r8mat_print ( n, n, a, '  JORDAN matrix:' )

  value = jordan_condition ( n, alpha )
  print ''
  print '  Value =  %g' % ( value )

  print ''
  print 'JORDAN_CONDITION_TEST'
  print '  Normal end of execution.'

  return

def jordan_determinant ( n, alpha ):

#*****************************************************************************80
#
## JORDAN_DETERMINANT returns the determinant of the JORDAN matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    16 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the order of the matrix.
#
#    Input, real ALPHA, the eigenvalue of the Jordan matrix.
#
#    Output, real VALUE, the determinant.
#
  value = alpha ** n

  return value

def jordan_determinant_test ( ):

#*****************************************************************************80
#
## JORDAN_DETERMINANT_TEST tests JORDAN_DETERMINANT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    16 February 2015
#
#  Author:
#
#    John Burkardt
#
  from jordan import jordan
  from r8mat_print import r8mat_print
  from r8_uniform_ab import r8_uniform_ab

  print ''
  print 'JORDAN_DETERMINANT_TEST'
  print '  JORDAN_DETERMINANT computes the determinant of the JORDAN matrix.'
  print ''

  m = 4
  n = m

  r8_lo = -5.0
  r8_hi = +5.0
  seed = 123456789
  alpha, seed = r8_uniform_ab ( r8_lo, r8_hi, seed )

  a = jordan ( m, n, alpha )
  r8mat_print ( m, n, a, '  JORDAN matrix:' )

  value = jordan_determinant ( n, alpha )

  print ''
  print '  Value =  %g' % ( value )

  print ''
  print 'JORDAN_DETERMINANT_TEST'
  print '  Normal end of execution.'

  return

def jordan_eigenvalues ( n, alpha ):

#*****************************************************************************80
#
## JORDAN_EIGENVALUES returns the eigenvalues of the JORDAN matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    12 April 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the order of the matrix.
#
#    Input, real ALPHA, the eigenvalue of the Jordan matrix.
#
#    Output, real LAM[N], the eigenvalues.
#
  import numpy as np

  lam = np.zeros ( n )

  for i in range ( 0, n ):
    lam[i] = alpha

  return value

def jordan_inverse ( n, alpha ):

#*****************************************************************************80
#
## JORDAN_INVERSE returns the inverse of the Jordan block matrix.
#
#  Formula:
#
#    if ( I <= J )
#      A(I,J) =  -1 * (-1/ALPHA)^(J+1-I)
#    else
#      A(I,J) = 0
#
#  Example:
#
#    ALPHA = 2, N = 4
#
#    1/2 -1/4  1/8 -1/16
#    0    1/2 -1/4  1/8
#    0    0    1/2 -1/4
#    0    0    0    1/2
#
#  Properties:
#
#    A is upper triangular.
#
#    A is Toeplitz: constant along diagonals.
#
#    A is generally not symmetric: A' /= A.
#
#    A is persymmetric: A(I,J) = A(N+1-J,N+1-I).
#
#    The inverse of A is the Jordan block matrix, whose diagonal
#    entries are ALPHA, whose first superdiagonal entries are 1,
#    with all other entries zero.
#
#    det ( A ) = (1/ALPHA)^N.
#
#    LAMBDA(1:N) = 1 / ALPHA.
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
#    Input, real ALPHA, the eigenvalue of the Jordan matrix.
#
#    Output, real A(N,N), the matrix.
#
  import numpy as np
  from sys import exit

  a = np.zeros ( ( n, n ) )

  if ( alpha == 0.0 ):
    print ''
    print 'JORDAN_INVERSE - Fatal error!'
    print '  The input parameter ALPHA was 0.'
    exit ( 'JORDAN_INVERSE - Fatal error!' )

  for i in range ( 0, n ):
    for j in range ( 0, n ):
      if ( i <= j ):
        a[i,j] =  - ( - 1.0 / alpha ) ** ( j + 1 - i )

  return a

def jordan_test ( ):

#*****************************************************************************80
#
## JORDAN_TEST tests JORDAN.
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
  from r8mat_print import r8mat_print
  from r8_uniform_ab import r8_uniform_ab

  print ''
  print 'JORDAN_TEST'
  print '  JORDAN computes the JORDAN matrix.'

  m = 6
  n = m

  r8_lo = -5.0
  r8_hi = +5.0
  seed = 123456789
  alpha, seed = r8_uniform_ab ( r8_lo, r8_hi, seed )

  a = jordan ( m, n, alpha )
  r8mat_print ( m, n, a, '  JORDAN matrix:' )

  print ''
  print 'JORDAN_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  jordan_test ( )
  timestamp ( )
