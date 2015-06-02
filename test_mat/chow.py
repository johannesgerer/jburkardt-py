#! /usr/bin/env python
#
def chow ( alpha, beta, m, n ):

#*****************************************************************************80
#
## CHOW returns the CHOW matrix.
#
#  Discussion:
#
#    By making ALPHA small compared with BETA, the eigenvalues can
#    all be made very close to BETA, and this is useful as a test
#    of eigenvalue computing routines.
#
#  Formula:
#
#    if ( I = J )
#      A(I,J) = ALPHA + BETA
#    else if ( J <= I+1 ) then
#      A(I,J) = ALPHA^(I+1-J)
#    else
#      A(I,J) = 0
#
#  Example:
#
#    ALPHA = 2, BETA = 3, M = 5, N = 5
#
#     5  1  0  0  0
#     4  5  1  0  0
#     8  4  5  1  0
#    16  8  4  5  1
#    32 16  8  4  5
#
#    ALPHA = ALPHA, BETA = BETA, M = 5, N = 5
#
#    ALPHA+BETA 1          0          0          0
#    ALPHA^2    ALPHA+BETA 1          0          0
#    ALPHA^3    ALPHA^2    ALPHA+BETA 1          0
#    ALPHA^4    ALPHA^3    ALPHA^2    ALPHA+BETA 1
#    ALPHA^5    ALPHA^4    ALPHA^3    ALPHA^2    ALPHA+BETA
#
#  Rectangular Properties:
#
#    A is Toeplitz: constant along diagonals.
#
#    A is lower Hessenberg.
#
#  Square Properties:
#
#    A is generally not symmetric: A' /= A.
#
#    If ALPHA is 0.0, then A is singular if and only if BETA is 0.0.
#
#    If BETA is 0.0, then A will be singular if 1 < N.
#
#    If BETA is 0.0 and N = 1, then A will be singular if ALPHA is 0.0.
#
#    A is persymmetric: A(I,J) = A(N+1-J,N+1-I).
#
#    For 1 <= I < N-(N+1)/2,
#
#      LAMBDA(I) = BETA + 4 * ALPHA * cos ( i * pi / ( N+2 ) )^2,
#
#    For N-(N+1)/2+1 <= I <= N
#
#      LAMBDA(I) = BETA
#
#    The family of matrices is nested as a function of N.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    23 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    TS Chow,
#    A class of Hessenberg matrices with known eigenvalues and inverses,
#    SIAM Review,
#    Volume 11, Number 3, 1969, pages 391-395.
#
#    Graeme Fairweather,
#    On the eigenvalues and eigenvectors of a class of Hessenberg matrices,
#    SIAM Review,
#    Volume 13, Number 2, 1971, pages 220-221.
#
#  Parameters:
#
#    Input, real ALPHA, the ALPHA value.  A typical value is 1.0.
#
#    Input, real BETA, the BETA value.  A typical value is 0.0.
#
#    Input, integer M, N, the number of rows and columns of A.
#
#    Output, real A(M,N), the matrix.
#
  import numpy as np

  a = np.zeros ( ( m, n ) )

  for i in range ( 0, m ):
    for j in range ( 0, n ):

      if ( i == j - 1 ):
        a[i,j] = 1.0
      elif ( i == j ):
        a[i,j] = alpha + beta
      elif ( j + 1 <= i ):
        a[i,j] = alpha ** ( i + 1 - j )
      else:
        a[i,j] = 0.0;

  return a

def chow_determinant ( alpha, beta, n ):

#*****************************************************************************80
#
## CHOW_DETERMINANT computes the determinant of the CHOW matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    23 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real ALPHA, the ALPHA value.  A typical value is 1.0.
#
#    Input, real BETA, the BETA value.  A typical value is 0.0.
#
#    Input, integer N, the order of the matrix.
#
#    Output, real DETERM, the determinant.
#
  from math import cos

  r8_pi = 3.141592653589793

  determ = 1.0

  k = n - ( n // 2 )

  for i in range ( 1, k + 1 ):
    angle = i * r8_pi / ( n + 2 )
    determ = determ * ( beta + 4.0 * alpha * ( cos ( angle ) ) ** 2 )

  determ  = determ * beta ** ( n - k )

  return determ

def chow_determinant_test ( ):

#*****************************************************************************80
#
## CHOW_DETERMINANT_TEST tests CHOW_DETERMINANT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    23 December 2014
#
#  Author:
#
#    John Burkardt
#
  from chow import chow
  from r8_uniform_01 import r8_uniform_01
  from r8mat_print import r8mat_print

  print ''
  print 'CHOW_DETERMINANT_TEST'
  print '  CHOW_DETERMINANT computes the CHOW determinant.'

  m = 5
  n = 5
  seed = 123456789
  alpha, seed = r8_uniform_01 ( seed )
  alpha = round ( 50.0 * alpha ) / 5.0
  beta, seed = r8_uniform_01 ( seed )
  beta = round ( 50.0 * beta ) / 5.0
  a = chow ( alpha, beta, m, n )
  r8mat_print ( m, n, a, '  CHOW matrix:' )

  value = chow_determinant ( alpha, beta, n )
  print '  Value =  %g' % ( value )

  print ''
  print 'CHOW_DETERMINANT_TEST'
  print '  Normal end of execution.'

  return

def chow_eigen_left ( alpha, beta, n ):

#*****************************************************************************80
#
## CHOW_EIGEN_LEFT returns the left eigenvector matrix for the CHOW matrix.
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
#    Input, real ALPHA, the ALPHA value.  A typical value is 1.0.
#
#    Input, real BETA, the BETA value.  A typical value is 0.0.
#
#    Input, integer N, the order of the matrix.
#
#    Output, real V(N,N), the left eigenvector matrix.
#
  import numpy as np

  v = np.zeros ( ( n, n ) )

  k = n - ( ( n + 1 ) // 2 )

  for i in range ( 0, k ):
    angle = float ( i + 1 ) * np.pi / float ( n + 2 )
    for j in range ( 0, n ):
      v[i,j] = alpha ** ( n - j - 1 ) * 2.0 ** ( n - j - 2 ) \
        * ( np.cos ( angle ) ) ** ( n - j ) \
        * np.sin ( ( n - j + 1 ) * angle ) / np.sin ( angle )

  for i in range ( k, n ):
    v[i,n-2] = -alpha
    v[i,n-1] = 1.0

  return v

def chow_eigen_right ( alpha, beta, n ):

#*****************************************************************************80
#
## CHOW_EIGEN_RIGHT returns the right eigenvectors of the CHOW matrix.
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
#    Input, real ALPHA, the ALPHA value.  A typical value is 1.0.
#
#    Input, real BETA, the BETA value.  A typical value is 0.0.
#
#    Input, integer N, the order of the matrix.
#
#    Output, real U(N,N), the right eigenvector matrix.
#
  import numpy as np

  u = np.zeros ( ( n, n ) )

  k = n - ( ( n + 1 ) // 2 )

  for j in range ( 0, k ):
    angle = float ( j + 1 ) * np.pi / float ( n + 2 )
    for i in range ( 0, n ):
      u[i,j] = alpha ** ( i ) * 2.0 ** ( i - 1 ) \
        * ( np.cos ( angle ) ) ** ( i - 1 ) \
        * np.sin ( float ( i + 2 ) * angle ) / np.sin ( angle )

  for j in range ( k, n ):
    u[0,j] = 1.0
    u[1,j] = -alpha

  return u

def chow_eigenvalues ( alpha, beta, n ):

#*****************************************************************************80
#
## CHOW_EIGENVALUES returns the eigenvalues of the CHOW matrix.
#
#  Example:
#
#    ALPHA = 2, BETA = 3, N = 5
#
#    9.49395943
#    6.10991621
#    3.0
#    3.0
#    3.0
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
#    Input, real ALPHA, the ALPHA value.  A typical value is 1.0.
#
#    Input, real BETA, the BETA value.  A typical value is 0.0.
#
#    Input, integer N, the order of A.
#
#    Output, real LAM(N), the eigenvalues of A.
#
  import numpy as np

  lam = np.zeros ( n );

  k = n - ( ( n + 1 ) // 2 )

  for i in range ( 0, k ):
    angle = float ( i + 1 ) * np.pi / float ( n + 2 )
    lam[i] = beta + 4.0 * alpha * ( np.cos ( angle ) ) ** 2

  for i in range ( k, n ):
    lam[i] = beta

  return lam

def chow_inverse ( alpha, beta, n ):

#*****************************************************************************80
#
#%\# CHOW_INVERSE returns the inverse of the Chow matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    24 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real ALPHA, the ALPHA value.  A typical value is 1.0.
#
#    Input, real BETA, the BETA value.  A typical value is 0.0.
#
#    Input, integer N, the order of A.
#
#    Output, real A(N,N), the matrix.
#
  import numpy as np
  from r8_mop import r8_mop
  from sys import exit

  a = np.zeros ( ( n, n ) )

  if ( 0.0 == alpha and beta == 0.0 ):

    print ''
    print 'CHOW_INVERSE - Fatal error!'
    print '  The Chow matrix is not invertible, because'
    print '  ALPHA = 0 and BETA = 0.'
    exit ( 'CHOW_INVERSE - Fatal error!' )

  elif ( 0.0 == alpha and beta != 0.0 ):

    for i in range ( 0, n ):
      for j in range ( 0, n ):

        if ( i <= j ):
          a[i,j] = r8_mop ( j - i ) / beta ** ( j + 1 - i )

  elif ( 0.0 != alpha and beta == 0.0 ):

    if ( 1 < n ):
      print ''
      print 'CHOW_INVERSE - Fatal error!'
      print '  The Chow matrix is not invertible, because'
      print '  BETA = 0 and 1 < N.'
      exit ( 'CHOW_INVERSE - Fatal error!' )

    a[0.0] = 1.0 / alpha

  else:

    d = np.zeros ( n + 1 )

    d[0] = 1.0
    d[1] = beta
    for i in range ( 2, n + 1 ):
      d[i] = beta * d[i-1] + alpha * beta * d[i-2]

    dp = np.zeros ( n + 2 )
    dp[0] = 1.0 / beta
    dp[1] = 1.0
    dp[2] = alpha + beta
    for i in range ( 2, n + 1 ):
      dp[i+1] = d[i] + alpha * d[i-1]

    for i in range ( 0, n ):
      for j in range ( 0, i ):
        a[i,j] = - alpha * ( alpha * beta ) ** ( i - j ) * dp[j] * d[n-1-i] \
          / dp[n+1]

      for j in range ( i, n ):
        a[i,j] = r8_mop ( i + j ) * dp[i+1] * d[n-j] / ( beta * dp[n+1] )

  return a

def chow_test ( ):

#*****************************************************************************80
#
## CHOW_TEST tests CHOW.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    23 December 2014
#
#  Author:
#
#    John Burkardt
#
  from r8_uniform_01 import r8_uniform_01
  from r8mat_print import r8mat_print

  print ''
  print 'CHOW_TEST'
  print '  CHOW computes the CHOW matrix.'

  m = 5
  n = 5
  seed = 123456789
  alpha, seed = r8_uniform_01 ( seed )
  alpha = round ( 50.0 * alpha ) / 5.0
  beta, seed = r8_uniform_01 ( seed )
  beta = round ( 50.0 * beta ) / 5.0
  a = chow ( alpha, beta, m, n )
  r8mat_print ( m, n, a, '  CHOW matrix:' )

  print ''
  print 'CHOW_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  chow_test ( )
  timestamp ( )
