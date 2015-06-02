#! /usr/bin/env python
#
def pei ( alpha, n ):

#*****************************************************************************80
#
## PEI returns the PEI matrix.
#
#  Formula:
#
#    if ( I = J )
#      A(I,J) = 1.0 + ALPHA
#    else
#      A(I,J) = 1.0
#
#  Example:
#
#    ALPHA = 2, N = 5
#
#    3 1 1 1 1
#    1 3 1 1 1
#    1 1 3 1 1
#    1 1 1 3 1
#    1 1 1 1 3
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
#    A is positive definite for 0 < ALPHA.
#
#    A is Toeplitz: constant along diagonals.
#
#    A is a circulant matrix: each row is shifted once to get the next row.
#
#    A is singular if and only if ALPHA = 0 or ALPHA = -N.
#
#    A becomes more ill-conditioned as ALPHA approaches 0.
#
#    The condition number under the spectral norm is 
#      abs ( ( ALPHA + N ) / ALPHA )
#
#    The eigenvalues of A are
#
#      LAMBDA(1:N-1) = ALPHA
#      LAMBDA(N) = ALPHA + N
#
#    A has constant row sum of ALPHA + N.
#
#    Because it has a constant row sum of ALPHA + N,
#    A has an eigenvalue of ALPHA + N, and
#    a (right) eigenvector of ( 1, 1, 1, ..., 1 ).
#
#    A has constant column sum of ALPHA + N.
#
#    Because it has a constant column sum of ALPHA + N,
#    A has an eigenvalue of ALPHA + N, and
#    a (left) eigenvector of ( 1, 1, 1, ..., 1 ).
#
#    The eigenvectors are:
#
#      V1 = 1 / sqrt ( N )       * ( 1, 1, 1, ... , 1 )
#      VR = 1 / sqrt ( R * (R-1) ) * ( 1, 1, 1, ... 1, -R+1, 0, 0, 0, ... 0 )
#
#    where the "-R+1" occurs at index R.
#
#    det ( A ) = ALPHA^(N-1) * ( N + ALPHA ).
#
#    The family of matrices is nested as a function of N.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Morris Newman, John Todd,
#    Example A3,
#    The evaluation of matrix inversion programs,
#    Journal of the Society for Industrial and Applied Mathematics,
#    Volume 6, Number 4, pages 466-476, 1958.
#
#    ML Pei,
#    A test matrix for inversion procedures,
#    Communications of the ACM,
#    Volume 5, 1962, page 508.
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
#    Input, real ALPHA, the scalar that defines the Pei matrix.  A
#    typical value of ALPHA is 1.0.
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
        a[i,j] = 1.0 + alpha
      else:
        a[i,j] = 1.0

  return a

def pei_condition ( alpha, n ):

#*****************************************************************************80
#
## PEI_CONDITION returns the L1 condition of the PEI matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real ALPHA, the scalar defining A.  
#
#    Input, integer N, the order of A.
#
#    Output, real VALUE, the L1 condition.
#
  a_norm = abs ( alpha + 1.0 ) + n - 1
  b_norm = ( abs ( alpha + n - 1.0 ) + n - 1.0 ) \
    / abs ( alpha * ( alpha + n ) )
  value = a_norm * b_norm

  return value

def pei_condition_test ( ):

#*****************************************************************************80
#
## PEI_CONDITION_TEST tests PEI_CONDITION.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 February 2015
#
#  Author:
#
#    John Burkardt
#
  from pei import pei
  from r8mat_print import r8mat_print
  from r8_uniform_ab import r8_uniform_ab

  print ''
  print 'PEI_CONDITION_TEST'
  print '  PEI_CONDITION computes the condition of the PEI matrix.'
  print ''

  m = 5
  n = m

  r8_lo = -5.0
  r8_hi = +5.0
  seed = 123456789
  alpha, seed = r8_uniform_ab ( r8_lo, r8_hi, seed )

  a = pei ( alpha, n )
  r8mat_print ( m, n, a, '  PEI matrix:' )

  value = pei_condition ( alpha )

  print ''
  print '  Value =  %g' % ( value )

  print ''
  print 'PEI_CONDITION_TEST'
  print '  Normal end of execution.'

  return

def pei_determinant ( alpha, n ):

#*****************************************************************************80
#
## PEI_DETERMINANT returns the determinant of the PEI matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real ALPHA, the scalar defining A.  
#
#    Input, integer N, the order of A.
#
#    Output, real VALUE, the determinant.
#
  value = alpha ** ( n - 1 ) * ( alpha + n )

  return value

def pei_determinant_test ( ):

#*****************************************************************************80
#
## PEI_DETERMINANT_TEST tests PEI_DETERMINANT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 February 2015
#
#  Author:
#
#    John Burkardt
#
  from pei import pei
  from r8mat_print import r8mat_print
  from r8_uniform_ab import r8_uniform_ab

  print ''
  print 'PEI_DETERMINANT_TEST'
  print '  PEI_DETERMINANT computes the determinant of the PEI matrix.'
  print ''

  m = 5
  n = m

  alpha_lo = 1.0
  alpha_hi = 100.0
  seed = 123456789
  alpha, seed = r8_uniform_ab ( alpha_lo, alpha_hi, seed )

  a = pei ( alpha, n )
  r8mat_print ( m, n, a, '  PEI matrix:' )

  value = pei_determinant ( alpha, n )

  print ''
  print '  Value =  %g' % ( value )

  print ''
  print 'PEI_DETERMINANT_TEST'
  print '  Normal end of execution.'

  return

def pei_eigen_right ( alpha, n ):

#*****************************************************************************80
#
## PEI_EIGEN_RIGHT returns the right eigenvectors of the PEI matrix.
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
#    Input, real ALPHA, the scalar that defines A.
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

  for i in range ( 0, n ):
    x[i,n-1] = 1.0

  return x

def pei_eigenvalues ( alpha, n ):

#*****************************************************************************80
#
## PEI_EIGENVALUES returns the eigenvalues of the Pei matrix.
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
#    Input, real ALPHA, the scalar that defines the Pei matrix.  A
#    typical value of ALPHA is 1.0.
#
#    Input, integer N, the order of A.
#
#    Output, real LAM(N), the eigenvalues.
#
  import numpy as np

  lam = np.zeros ( n )

  for i in range ( 0, n - 1 ):
    lam[i] = alpha

  lam[n-1] = alpha + float ( n )

  return lam

def pei_inverse ( alpha, n ):

#*****************************************************************************80
#
## PEI_INVERSE returns the inverse of the Pei matrix.
#
#  Formula:
#
#    if ( I = J )
#      A(I,J) = (ALPHA+N-1) / ( (ALPHA+1)*(ALPHA+N-1)-(N-1) )
#    else
#      A(I,J) =          -1 / ( (ALPHA+1)*(ALPHA+N-1)-(N-1) )
#
#  Example:
#
#    ALPHA = 2, N = 5
#
#            6 -1 -1 -1 -1
#           -1  6 -1 -1 -1
#    1/14 * -1 -1  6 -1 -1
#           -1 -1 -1  6 -1
#           -1 -1 -1 -1  6
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
#    A is a "combinatorial" matrix.  See routine COMBIN.
#
#    A is Toeplitz: constant along diagonals.
#
#    A is a circulant matrix: each row is shifted once to get the next row.
#
#    A has constant row sum.
#
#    Because it has a constant row sum of 1 / ( ALPHA + N ),
#    A has an eigenvalue of 1 / ( ALPHA + N ), and
#    a (right) eigenvector of ( 1, 1, 1, ..., 1 ).
#
#    A has constant column sum.
#
#    Because it has constant column sum of 1 / ( ALPHA + N ),
#    A has an eigenvalue of 1 / ( ALPHA + N ), and
#    a (left) eigenvector of ( 1, 1, 1, ..., 1 ).
#
#    The eigenvalues of A are
#      LAMBDA(1:N-1) = 1 / ALPHA
#      LAMBDA(N) = 1 / ( ALPHA + N )
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
#  Reference:
#
#    ML Pei,
#    A test matrix for inversion procedures,
#    Communications of the ACM,
#    Volume 5, 1962, page 508.
#
#  Parameters:
#
#    Input, real ALPHA, the scalar that defines the inverse 
#    of the Pei matrix.
#
#    Input, integer N, the order of A.
#
#    Output, real A(N,N), the matrix.
#
  import numpy as np
  from sys import exit

  a = np.zeros ( ( n, n ) )

  bottom = ( alpha + 1.0 ) * ( alpha + n - 1.0 ) - n + 1.0

  if ( bottom == 0.0 ):
    print ''
    print 'PEI_INVERSE - Fatal error!'
    print '  The matrix is not invertible.'
    print '  (ALPHA+1)*(ALPHA+N-1)-N+1 is zero.'
    exit ( 'PEI_INVERSE - Fatal error!' )

  alpha1 = ( alpha + ( n ) - 1.0 ) / bottom
  beta1 = - 1.0 / bottom

  for i in range ( 0, n ):
    for j in range ( 0, n ):
      if ( i == j ):
        a[i,j] = alpha1
      else:
        a[i,j] = beta1

  return a


def pei_test ( ):

#*****************************************************************************80
#
## PEI_TEST tests PEI.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 February 2015
#
#  Author:
#
#    John Burkardt
#
  from r8mat_print import r8mat_print
  from r8_uniform_ab import r8_uniform_ab

  print ''
  print 'PEI_TEST'
  print '  PEI computes the PEI matrix.'

  m = 5
  n = m

  alpha_lo = 1.0
  alpha_hi = 100.0
  seed = 123456789
  alpha, seed = r8_uniform_ab ( alpha_lo, alpha_hi, seed )

  a = pei ( alpha, n )
  r8mat_print ( m, n, a, '  PEI matrix:' )

  print ''
  print 'PEI_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  pei_test ( )
  timestamp ( )
