#! /usr/bin/env python
#
def bab ( n, alpha, beta ):

#*****************************************************************************80
#
## BAB returns the BAB matrix.
#
#  Example:
#
#    N = 5
#    ALPHA = 5, BETA = 2
#
#    5  2  .  .  .
#    2  5  2  .  .
#    .  2  5  2  .
#    .  .  2  5  2
#    .  .  .  2  5
#
#  Properties:
#
#    A is banded, with bandwidth 3.
#
#    A is tridiagonal.
#
#    Because A is tridiagonal, it has property A (bipartite).
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
#    The family of matrices is nested as a function of N.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    05 November 2007
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    CM da Fonseca, J Petronilho,
#    Explicit Inverses of Some Tridiagonal Matrices,
#    Linear Algebra and Its Applications,
#    Volume 325, 2001, pages 7-21.
#
#  Parameters:
#
#    Input, integer N, the order of the matrix.
#
#    Input, real ALPHA, BETA, the parameters.
#
#    Output, real A(N,N), the matrix.
#
  import numpy as np

  a = np.zeros ( ( n, n ) )

  for i in range ( 0, n ):
    a[i,i] = alpha

  for i in range ( 0, n - 1 ):
    a[i,i+1] = beta
    a[i+1,i] = beta
 
  return a

def bab_condition ( n, alpha, beta ):

#*****************************************************************************80
#
## BAB_CONDITION returns the L1 condition of the BAB matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    14 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the order of the matrix.
#
#    Input, real ALPHA, BETA, the parameters.
#
#    Output, real COND, the L1 condition number.
#
  from r8mat_norm_l1 import r8mat_norm_l1

  a = bab ( n, alpha, beta )
  a_norm = r8mat_norm_l1 ( n, n, a )

  b = bab_inverse ( n, alpha, beta )
  b_norm = r8mat_norm_l1 ( n, n, b )

  cond = a_norm * b_norm

  return cond

def bab_condition_test ( ):

#*****************************************************************************80
#
## BAB_CONDITION_TEST tests BAB_CONDITION.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    14 December 2014
#
#  Author:
#
#    John Burkardt
#
  from r8_uniform_01 import r8_uniform_01
  from r8mat_print import r8mat_print

  print ''
  print 'BAB_CONDITION_TEST'
  print '  BAB_CONDITION computes the condition of the BAB matrix.'
  print ''

  seed = 123456789

  n = 5
  alpha, seed = r8_uniform_01 ( seed )
  beta, seed = r8_uniform_01 ( seed )
  a = bab ( n, alpha, beta )
  r8mat_print ( n, n, a, '  BAB matrix:' )

  value = bab_condition ( n, alpha, beta )
  print ''
  print '  Valule =  %g' % ( value )

  print ''
  print 'BAB_CONDITION_TEST'
  print '  Normal end of execution.'

  return

def bab_determinant ( n, alpha, beta ):

#*****************************************************************************80
#
## BAB_DETERMINANT computes the determinant of the BAB matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    14 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the order of the matrix.
#
#    Input, real ALPHA, BETA, parameters that define the matrix.
#
#    Output, real DETERM, the determinant.
#
  determ_nm1 = alpha

  if ( n == 1 ):
    determ = determ_nm1
    return determ

  determ_nm2 = determ_nm1
  determ_nm1 = alpha * alpha - beta * beta

  if ( n == 2 ):
    determ = determ_nm1
    return determ

  for i in range ( n - 2, 0, -1 ):
 
    determ = alpha * determ_nm1 - beta * beta * determ_nm2

    determ_nm2 = determ_nm1
    determ_nm1 = determ

  return determ

def bab_determinant_test ( ):

#*****************************************************************************80
#
## BAB_DETERMINANT_TEST tests BAB_DETERMINANT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    05 December 2014
#
#  Author:
#
#    John Burkardt
#
  from r8_uniform_01 import r8_uniform_01
  from r8mat_print import r8mat_print

  print ''
  print 'BAB_DETERMINANT_TEST'
  print '  BAB_DETERMINANT computes the BAB determinant.'

  seed = 123456789

  n = 5
  alpha, seed = r8_uniform_01 ( seed )
  beta, seed = r8_uniform_01 ( seed )
  a = bab ( n, alpha, beta )
  r8mat_print ( n, n, a, '  BAB matrix:' )

  value = bab_determinant ( n, alpha, beta )
  print '  Value =  %g' % ( value )

  print ''
  print 'BAB_DETERMINANT_TEST'
  print '  Normal end of execution.'

  return

def bab_eigen_right ( n, alpha, beta ):

#*****************************************************************************80
#
## BAB_EIGEN_RIGHT returns the right eigenvectors of the BAB matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 April 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the order of A.
#
#    Input, real ALPHA, BETA, the parameters.
#
#    Output, real A(N,N), the right eigenvector matrix.
#
  import numpy as np

  a = np.zeros ( ( n, n ) )

  for i in range ( 0, n ):
    for j in range ( 0, n ):
      angle = float ( ( i + 1 ) *  ( j + 1 ) ) * np.pi / float ( n + 1 )
      a[i,j] = np.sqrt ( 2.0 / float ( n + 1 ) ) * np.sin ( angle )

  return a

def bab_eigenvalues ( n, alpha, beta ):

#*****************************************************************************80
#
## BAB_EIGENVALUES returns the eigenvalues of the BAB matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 April 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the order of the matrix.
#
#    Input, real ALPHA, BETA, the parameters.
#
#    Output, real LAM(N), the eigenvalues.
#
  import numpy as np

  lam = np.zeros ( n )

  for i in range ( 0, n ):
    angle = float ( i + 1 ) * np.pi / float ( n + 1 )
    lam[i] = alpha + 2.0 * beta * np.cos ( angle )

  return lam

def bab_inverse ( n, alpha, beta ):

#*****************************************************************************80
#
## BAB_INVERSE returns the inverse of the BAB matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    14 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the order of the matrix.
#
#    Input, real ALPHA, BETA, the parameters.
#
#    Output, real A(N,N), the matrix.
#
  from sys import exit
  import numpy as np
  from cheby_u_polynomial import cheby_u_polynomial
  from r8_mop import r8_mop

  a = np.zeros ( ( n, n ) )

  if ( beta == 0.0 ):

    if ( alpha == 0.0 ):
      print ''
      print 'BAB_INVERSE - Fatal error!'
      print '  ALPHA = BETA = 0.'
      exit ( 'BAB_INVERSE - Fatal error!' )

    for i in range ( 0, n ):
      a[i,i] = 1.0 / alpha

  else:

    x = 0.5 * alpha / beta

    u = cheby_u_polynomial ( n, x )

    for i in range ( 1, n + 1 ):
      for j in range ( 1, i + 1 ):
        a[i-1,j-1] = r8_mop ( i + j ) * u[j-1] * u[n-i] / u[n] / beta
      for j in range ( i + 1, n + 1 ):
        a[i-1,j-1] = r8_mop ( i + j ) * u[i-1] * u[n-j] / u[n] / beta

  return a

def bab_inverse_test ( ):

#*****************************************************************************80
#
## BAB_INVERSE_TEST tests BAB_INVERSE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    14 December 2014
#
#  Author:
#
#    John Burkardt
#
  from r8_uniform_01 import r8_uniform_01
  from r8mat_print import r8mat_print

  print ''
  print 'BAB_INVERSE_TEST'
  print '  BAB_INVERSE computes the inverse of the BAB matrix.'

  seed = 123456789

  n = 5
  alpha, seed = r8_uniform_01 ( seed )
  beta, seed = r8_uniform_01 ( seed )
  b = bab_inverse ( n, alpha, beta )
  r8mat_print ( n, n, b, '  BAB inverse:' )

  print ''
  print 'BAB_INVERSE_TEST'
  print '  Normal end of execution.'

  return

def bab_test ( ):

#*****************************************************************************80
#
## BAB_TEST tests BAB.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    14 December 2014
#
#  Author:
#
#    John Burkardt
#
  from r8_uniform_01 import r8_uniform_01
  from r8mat_print import r8mat_print

  print ''
  print 'BAB_TEST'
  print '  BAB computes the BAB matrix.'

  seed = 123456789

  n = 5
  alpha, seed = r8_uniform_01 ( seed )
  beta, seed = r8_uniform_01 ( seed )
  a = bab ( n, alpha, beta )
  r8mat_print ( n, n, a, '  BAB matrix:' )

  print ''
  print 'BAB_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  bab_test ( )
  timestamp ( )
