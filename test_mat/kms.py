#! /usr/bin/env python
#
def kms ( alpha, m, n ):

#*****************************************************************************80
#
## KMS returns the KMS matrix.
#
#  Formula:
#
#    A(I,J) = ALPHA^abs ( I - J )
#
#  Example:
#
#    ALPHA = 2, N = 5
#
#     1  2  4  8  16
#     2  1  2  4   8
#     4  2  1  2   4
#     8  4  2  1   2
#    16  8  4  2   1
#
#    ALPHA = 1/2, N = 5
#
#     1   1/2  1/4  1/8  1/16
#    1/2   1   1/2  1/4  1/8
#    1/4  1/2   1   1/2  1/4
#    1/8  1/4  1/2   1   1/2
#    1/16 1/8  1/4  1/2   1
#
#  Properties:
#
#    A is Toeplitz: constant along diagonals.
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
#    A has an L*D*L' factorization, with L being the inverse
#    of the transpose of the matrix with 1's on the diagonal and
#    -ALPHA on the superdiagonal and zero elsewhere, and
#    D(I,I) = (1-ALPHA^2) except that D(1,1)=1.
#
#    det ( A ) = ( 1 - ALPHA^2 )^(N-1).
#
#    The inverse of A is tridiagonal.
#
#    A is positive definite if and only if 0 < abs ( ALPHA ) < 1.
#
#    The family of matrices is nested as a function of N.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    17 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    William Trench,
#    Numerical solution of the eigenvalue problem for Hermitian
#    Toeplitz matrices,
#    SIAM Journal on Matrix Analysis and Applications,
#    Volume 10, Number 2, April 1989, pages 135-146.
#
#  Parameters:
#
#    Input, real ALPHA, the scalar that defines A.  
#    A typical value is 0.5.
#
#    Input, integer M, N, the number of rows and columns of A.
#
#    Output, real A(M,N), the matrix.
#
  import numpy as np

  a = np.zeros ( ( m, n ) )

  for i in range ( 0, m ):
    for j in range ( 0, n ):

      if ( alpha == 0.0 and i == j ):
        a[i,j] = 1.0
      else:
        a[i,j] = alpha ** ( abs ( i - j ) )

  return a

def kms_determinant ( alpha, n ):

#*****************************************************************************80
#
## KMS_DETERMINANT computes the determinant of the KMS matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    17 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real ALPHA, the parameter.
#
#    Input, integer N, the order of the matrix.
#
#    Output, real VALUE, the determinant.
#
  import numpy as np

  if ( n == 1 ):
    value = 1.0
  else:
    value = ( 1.0 - alpha * alpha ) ** ( n - 1 )

  return value

def kms_determinant_test ( ):

#*****************************************************************************80
#
## KMS_DETERMINANT_TEST tests KMS_DETERMINANT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    17 December 2015
#
#  Author:
#
#    John Burkardt
#
  from kms import kms
  from r8_uniform_ab import r8_uniform_ab
  from r8mat_print import r8mat_print

  print ''
  print 'KMS_DETERMINANT_TEST'
  print '  KMS_DETERMINANT computes the KMS determinant.'

  seed = 123456789

  m = 5
  n = m
  r8_lo = 0.0
  r8_hi = 1.0
  alpha, seed = r8_uniform_ab ( r8_lo, r8_hi, seed )
  a = kms ( alpha, m, n )
  r8mat_print ( m, n, a, '  KMS matrix:' )

  value = kms_determinant ( alpha, n )

  print ''
  print '  Value =  %g' % ( value )

  print ''
  print 'KMS_DETERMINANT_TEST'
  print '  Normal end of execution.'

  return

def kms_eigen_right ( alpha, n ):

#*****************************************************************************80
#
## KMS_EIGEN_RIGHT returns the right eigenvectors of the KMS matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 April 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    William Trench,
#    Spectral decomposition of Kac-Murdock-Szego matrices,
#    Unpublished technical report.
#
#  Parameters:
#
#    Input, real ALPHA, the parameter.
#    Eigenvalue computations require 0 <= ALPHA <= 1.
#
#    Input, integer N, the order of A.
#
#    Output, real A(N,N), the right eigenvector matrix.
#
  import numpy as np
 
  t = kms_eigenvalues_theta ( alpha, n )

  a = np.zeros ( ( n, n ) )

  for i in range ( 0, n ):
    for j in range ( 0, n ):
      a[i,j] = np.sin ( ( float ) ( i + 1 ) * t[j] ) \
        - alpha * np.sin ( float ( i ) * t[j] )

  return a

def kms_eigenvalues ( alpha, n ):

#*****************************************************************************80
#
## KMS_EIGENVALUES returns the eigenvalues of the KMS matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 April 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    William Trench,
#    Spectral decomposition of Kac-Murdock-Szego matrices,
#    Unpublished technical document.
#
#  Parameters:
#
#    Input, real ALPHA, the scalar that defines A.  
#    Eigenvalue computations require 0 <= ALPHA <= 1.
#
#    Input, integer N, the order of the matrix.
#
#    Output, real LAM(N), the eigenvalues.
#
  import numpy as np

  theta = kms_eigenvalues_theta ( alpha, n )

  lam = np.zeros ( n )
 
  for i in range ( 0, n ):
    lam[i] = ( 1.0 + alpha ) * ( 1.0 - alpha ) \
      / ( 1.0 - 2.0 * alpha * np.cos ( theta[i] ) + alpha * alpha )

  return lam

def kms_eigenvalues_theta ( alpha, n ):

#*****************************************************************************80
#
## KMS_EIGENVALUES_THETA returns data needed to compute KMS eigenvalues.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 April 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    William Trench,
#    Spectral decomposition of Kac-Murdock-Szego matrices,
#    Unpublished technical document.
#
#  Parameters:
#
#    Input, real ALPHA, the scalar that defines A.  
#    Eigenvalue computations require 0 <= ALPHA <= 1.
#
#    Input, integer N, the order of the matrix.
#
#    Output, real T(N), the angles associated with
#    the eigenvalues.
#
  import numpy as np

  step_max = 100

  t = np.zeros ( n )

  for i in range ( 0, n ):
#
#  Avoid confusion in first subinterval, where f(0) = 0.
#
    if ( i == 0 ):
      xa = 0.0001
    else:
      xa = float ( i ) * np.pi / float ( n + 1 )

    fxa = kms_eigenvalues_theta_f ( alpha, n, xa )
    xb = float ( i + 1 ) * np.pi / float ( n + 1 )
    fxb = kms_eigenvalues_theta_f ( alpha, n, xb )

    if ( 0.0 < fxa ):
      temp = xa
      xa = xb
      xb = temp
      temp = fxa
      fxa = fxb
      fxb = temp

    for step in range ( 0, step_max ):

      xc = 0.5 * ( xa + xb )
      fxc = kms_eigenvalues_theta_f ( alpha, n, xc )
#
#  Return if residual is small.
#
      if ( abs ( fxc ) <= 0.0000001 ):
        break
#
#  Return if interval is small.
#
      if ( abs ( xb - xa ) <= 0.0000001 ):
        break

      if ( fxc < 0.0 ):
        xa = xc
        fxa = fxc
      else:
        xb = xc
        fxb = fxc

    t[i] = xc

  return t

def kms_eigenvalues_theta_f ( alpha, n, t ):

#*****************************************************************************80
#
## KMS_EIGENVALUES_THETA_F evaluates a function for KMS eigenvalues.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 April 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    William Trench,
#    Spectral decomposition of Kac-Murdock-Szego matrices,
#    Unpublished technical document.
#
#  Parameters:
#
#    Input, real ALPHA, the scalar that defines A.  
#    Eigenvalue computations require 0 <= ALPHA <= 1.
#
#    Input, integer N, the order of the matrix.
#
#    Input, real T, an angle associated with the eigenvalue.
#
#    Output, real VALUE, the function value.
#
  import numpy as np

  n_r8 = float ( n ) 

  value = np.sin ( ( n_r8 + 1.0 ) * t ) \
    - 2.0 * alpha * np.sin ( n_r8 * t ) \
    + alpha * alpha * np.sin ( ( n_r8 - 1.0 ) * t )

  return value

def kms_inverse ( alpha, n ):

#*****************************************************************************80
#
## KMS_INVERSE returns the inverse of the KMS matrix.
#
#  Formula:
#
#    if ( I = J )
#      if ( I = 1 )
#        A(I,J) = -1/(ALPHA^2-1)
#      elseif ( I < N )
#        A(I,J) = -(ALPHA^2+1)/(ALPHA^2-1)
#      elseif ( I = N )
#        A(I,J) = -1/(ALPHA^2-1)
#    elseif ( J = I + 1 or I = J + 1 )
#      A(I,J) = ALPHA/(ALPHA^2-1)
#    else
#      A(I,J) = 0 otherwise
#
#  Example:
#
#    ALPHA = 2, N = 5
#
#         -1  2  0  0  0
#          2 -5  2  0  0
#    1/3 * 0  2 -5  2  0
#          0  0  2 -5  2
#          0  0  0  2 -1
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
#    William Trench,
#    Numerical solution of the eigenvalue problem for Hermitian
#    Toeplitz matrices,
#    SIAM Journal on Matrix Analysis and Applications,
#    Volume 10, Number 2, April 1989, pages 135-146.
#
#  Parameters:
#
#    Input, real ALPHA, the scalar that defines A.
#
#    Input, integer N, the order of A.
#
#    Output, real A(N,N), the matrix.
#
  import numpy as np

  a = np.zeros ( ( n, n ) )

  bot = alpha * alpha - 1.0

  for i in range ( 0, n ):
    for j in range ( 0, n ):

      if ( i == j ):
        if ( j == 0 ):
          a[i,j] = - 1.0 / bot
        elif ( j < n - 1 ):
          a[i,j] = - ( alpha * alpha + 1.0 ) / bot
        elif ( j == n - 1 ):
          a[i,j] = -1.0 / bot
      elif ( i == j + 1 or j == i + 1 ):
        a[i,j] = alpha / bot

  return a

def kms_plu ( alpha, n ):

#*****************************************************************************80
#
## KMS_PLU returns the PLU factors of the KMS matrix.
#
#  Example:
#
#    ALPHA = 0.5, N = 5
#
#    P = Identity matrix
#
#    L =
#
#       1    0   0   0   0
#      1/2   1   0   0   0
#      1/4  1/2  1   0   0
#      1/8  1/4 1/2  1   0
#      1/16 1/8 1/4 1/2  1
#
#    U =
#
#       1   1/2  1/4  1/8  1/16
#       0   3/4  3/8  3/16 3/32
#       0    0   3/4  3/8  3/16
#       0    0    0   3/4  3/8
#       0    0    0    0   3/4
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
#  Reference:
#
#    William Trench,
#    Numerical solution of the eigenvalue problem for Hermitian
#    Toeplitz matrices,
#    SIAM Journal on Matrix Analysis and Applications,
#    Volume 10, Number 2, April 1989, pages 135-146.
#
#  Parameters:
#
#    Input, real ALPHA, the scalar that defines A.  
#    A typical value is 0.5.
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

  l[0,0] = 1.0
  for i in range ( 1, n ):
    l[i,0] = alpha * l[i-1,0]

  for j in range ( 1, n ):
    for i in range ( j, n ):
      l[i,j] = l[i-j,0]

  u = np.zeros ( ( n, n ) )

  for j in range ( 0, n ):
    u[0,j] = l[j,0]
    for i in range ( 1, n ):
      u[i,j] = l[j,i] * ( 1.0 - alpha * alpha )

  return p, l, u

def kms_test ( ):

#*****************************************************************************80
#
## KMS_TEST tests KMS.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    17 February 2015
#
#  Author:
#
#    John Burkardt
#
  from r8_uniform_ab import r8_uniform_ab
  from r8mat_print import r8mat_print

  print ''
  print 'KMS_TEST'
  print '  KMS computes the KMS matrix.'

  seed = 123456789

  m = 5
  n = 5
  r8_lo = 0.0
  r8_hi = 1.0
  alpha, seed = r8_uniform_ab ( r8_lo, r8_hi, seed )
  a = kms ( alpha, m, n )
  r8mat_print ( m, n, a, '  KMS matrix:' )

  print ''
  print 'KMS_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  kms_test ( )
  timestamp ( )
