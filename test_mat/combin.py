#! /usr/bin/env python
#
def combin ( alpha, beta, n ):

#*****************************************************************************80
#
## COMBIN returns the COMBIN matrix.
#
#  Formula:
#
#    If ( I = J ) then
#      A(I,J) = ALPHA + BETA
#    else
#      A(I,J) = BETA
#
#  Example:
#
#    N = 5, ALPHA = 2, BETA = 3
#
#    5 3 3 3 3
#    3 5 3 3 3
#    3 3 5 3 3
#    3 3 3 5 3
#    3 3 3 3 5
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
#    det ( A ) = ALPHA^(N-1) * ( ALPHA + N * BETA ).
#
#    LAMBDA(1:N-1) = ALPHA,
#    LAMBDA(N) = ALPHA + N * BETA.
#
#    The eigenvector associated with LAMBDA(N) is (1,1,1,...,1)/sqrt(N).
#
#    The other N-1 eigenvectors are simply any (orthonormal) basis
#    for the space perpendicular to (1,1,1,...,1).
#
#    A is nonsingular if ALPHA /= 0 and ALPHA + N * BETA /= 0.
#
#    The family of matrices is nested as a function of N.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 October 2007
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Robert Gregory, David Karney,
#    Example 3.25,
#    A Collection of Matrices for Testing Computational Algorithms,
#    Wiley, New York, 1969, page 53,
#    LC: QA263.G68.
#
#    Donald Knuth,
#    The Art of Computer Programming,
#    Volume 1, Fundamental Algorithms, Second Edition,
#    Addison-Wesley, Reading, Massachusetts, 1973, page 36.
#
#  Parameters:
#
#    Input, real ALPHA, BETA, scalars that define A.
#
#    Input, integer N, the order of A.
#
#    Output, real A(N,N), the matrix.
#
  import numpy as np

  a = np.zeros ( [ n, n ] )

  for j in range ( 0, n ):
    for i in range ( 0, n ):
      a[i,j] = beta
    a[j,j] = a[j,j] + alpha

  return a

def combin_condition ( alpha, beta, n ):

#*****************************************************************************80
#
## COMBIN_CONDITION returns the L1 condition of the COMBIN matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    16 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real ALPHA, BETA, scalars that define A.
#
#    Input, integer N, the order of the matrix.
#
#    Output, real COND, the L1 condition.
#
  a_norm = abs ( alpha + beta ) + ( n - 1 ) * abs ( beta )

  b_norm_top = abs ( alpha + ( n - 1 ) * beta ) + ( n - 1 ) * abs ( beta )

  b_norm_bot = abs ( alpha * ( alpha + n * beta ) )

  b_norm = b_norm_top / b_norm_bot

  cond = a_norm * b_norm

  return cond

def combin_condition_test ( ):

#*****************************************************************************80
#
## COMBIN_CONDITION_TEST tests COMBIN_CONDITION.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    16 December 2014
#
#  Author:
#
#    John Burkardt
#
  from r8_uniform_01 import r8_uniform_01
  from r8mat_print import r8mat_print

  print ''
  print 'COMBIN_CONDITION_TEST'
  print '  COMBIN_CONDITION computes the condition of the COMBIN matrix.'
  print ''

  seed = 123456789

  n = 3
  seed = 123456789
  alpha, seed = r8_uniform_01 ( seed )
  alpha = round ( 50.0 * alpha ) / 5.0
  beta, seed = r8_uniform_01 ( seed )
  beta = round ( 50.0 * beta ) / 5.0
  a = combin ( alpha, beta, n )
  r8mat_print ( n, n, a, '  COMBIN matrix:' )

  value = combin_condition ( alpha, beta, n )

  print ''
  print '  Value =  %g' % ( value )

  print ''
  print 'COMBIN_CONDITION_TEST'
  print '  Normal end of execution.'

  return

def combin_determinant ( alpha, beta, n ):

#*****************************************************************************80
#
## COMBIN_DETERMINANT computes the determinant of the COMBIN matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real ALPHA, BETA, scalars that define the matrix.
#
#    Input, integer N, the order of the matrix.
#
#    Output, real DETERM, the determinant.
#
  determ = alpha ** ( n - 1 ) * ( alpha + n * beta )
 
  return determ

def combin_determinant_test ( ):

#*****************************************************************************80
#
## COMBIN_DETERMINANT_TEST tests COMBIN_DETERMINANT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 December 2014
#
#  Author:
#
#    John Burkardt
#
  from r8_uniform_01 import r8_uniform_01
  from r8mat_print import r8mat_print

  print ''
  print 'COMBIN_DETERMINANT_TEST'
  print '  COMBIN_DETERMINANT computes the COMBIN determinant.'

  m = 4
  n = 4
  seed = 123456789
  alpha, seed = r8_uniform_01 ( seed )
  alpha = round ( 50.0 * alpha ) / 5.0
  beta, seed = r8_uniform_01 ( seed )
  beta = round ( 50.0 * beta ) / 5.0
  a = combin ( alpha, beta, n )

  r8mat_print ( m, n, a, '  COMBIN matrix:' )

  value = combin_determinant ( alpha, beta, n )

  print '  Value =  %g' % ( value )

  print ''
  print 'COMBIN_DETERMINANT_TEST'
  print '  Normal end of execution.'

  return

def combin_eigen_right ( alpha, beta, n ):

#*****************************************************************************80
#
## COMBIN_EIGEN_RIGHT returns the right eigenvectors of the COMBIN matrix.
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
#    Input, real ALPHA, BETA, scalars that define A.
#
#    Input, integer N, the order of the matrix.
#
#    Output, real X(N,N), the right eigenvectors.
#
  import numpy as np

  x = np.zeros ( ( n, n ) )

  for j in range ( 0, n - 1 ):
    x[  0,j] = +1.0
    x[j+1,j] = -1.0

  j = n - 1
  for i in range ( 0, n ):
    x[i,j] = 1.0

  return x

def combin_eigenvalues ( alpha, beta, n ):

#*****************************************************************************80
#
## COMBIN_EIGENVALUES returns the eigenvalues of the COMBIN matrix.
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
#    Input, real ALPHA, BETA, scalars that define A.
#
#    Input, integer N, the order of A.
#
#    Output, real LAM(N), the eigenvalues.
#
  import numpy as np

  lam = np.zeros ( n )

  for i in range ( 0, n - 1 ):
    lam[i] = alpha
  lam[n-1] = alpha + n * beta

  return lam

def combin_inverse ( alpha, beta, n ):

#*****************************************************************************80
#
## COMBIN_INVERSE returns the inverse of the combinatorial matrix A.
#
#  Formula:
#
#    if ( I = J )
#      A(I,J) = (ALPHA+(N-1)*BETA) / (ALPHA*(ALPHA+N*BETA))
#    else
#      A(I,J) =             - BETA / (ALPHA*(ALPHA+N*BETA))
#
#  Example:
#
#    N = 5, ALPHA = 2, BETA = 3
#
#           14 -3 -3 -3 -3
#           -3 14 -3 -3 -3
#   1/34 *  -3 -3 14 -3 -3
#           -3 -3 -3 14 -3
#           -3 -3 -3 -3 14
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
#    A is Toeplitz: constant along diagonals.
#
#    det ( A ) = 1 / (ALPHA^(N-1) * (ALPHA+N*BETA)).
#
#    A is well defined if ALPHA /= 0.0 and ALPHA+N*BETA /= 0.
#
#    A is also a combinatorial matrix.
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
#  Reference:
#
#    Donald Knuth,
#    The Art of Computer Programming,
#    Volume 1, Fundamental Algorithms, Second Edition,
#    Addison-Wesley, Reading, Massachusetts, 1973, page 36.
#
#  Parameters:
#
#    Input, real ALPHA, BETA, scalars that define the matrix.
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
    print 'COMBIN_INVERSE - Fatal error!'
    print '  The entries of the matrix are undefined'
    print '  because ALPHA = 0.'
    exit ( 'COMBIN_INVERSE - Fatal error!' )
  elif ( alpha + n * beta == 0.0 ):
    print ''
    print 'COMBIN_INVERSE - Fatal error!'
    print '  The entries of the matrix are undefined'
    print '  because ALPHA+N*BETA is zero.'
    exit ( 'COMBIN_INVERSE - Fatal error!' )

  bot = alpha * ( alpha + n * beta )

  for i in range ( 0, n ):
    for j in range ( 0, n ):

      if ( i == j ):
        a[i,j] = ( alpha + float ( n - 1 ) * beta ) / bot
      else:
        a[i,j] = - beta / bot

  return a

def combin_test ( ):

#*****************************************************************************80
#
## COMBIN_TEST tests COMBIN.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    16 December 2014
#
#  Author:
#
#    John Burkardt
#
  from r8_uniform_01 import r8_uniform_01
  from r8mat_print import r8mat_print

  print ''
  print 'COMBIN_TEST'
  print '  COMBIN computes the COMBIN matrix.'

  n = 4
  seed = 123456789
  alpha, seed = r8_uniform_01 ( seed )
  alpha = round ( 50.0 * alpha ) / 5.0
  beta, seed = r8_uniform_01 ( seed )
  beta = round ( 50.0 * beta ) / 5.0
  a = combin ( alpha, beta, n )
  r8mat_print ( n, n, a, '  COMBIN matrix:' )

  print ''
  print 'COMBIN_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  combin_test ( )
  timestamp ( )
