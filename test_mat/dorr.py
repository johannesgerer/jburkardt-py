#! /usr/bin/env python
#
def dorr ( alpha, n ):

#*****************************************************************************80
#
## DORR returns the DORR matrix.
#
#  Formula:
#
#    if ( I <= (N+1) / 2 )
#
#      if ( J = I - 1 )
#        A(I,J) = - ALPHA * (N+1)^2
#      else if ( J = I )
#        A(I,J) = 2 * ALPHA * (N+1)^2 + 0.5 * (N+1) - I
#      else if ( J = I + 1 )
#        A(I,J) = - ALPHA * (N+1)^2 - 0.5 * (N+1) + I
#      else
#        A(I,J) = 0
#
#    else
#
#      if ( J = I - 1 )
#        A(I,J) = - ALPHA * (N+1)^2 + 0.5 * (N+1) - I
#      else if ( J = I )
#        A(I,J) = 2 * ALPHA * (N+1)^2 - 0.5 * (N+1) + I
#      else if ( J = I + 1 )
#        A(I,J) = - ALPHA * (N+1)^2
#      else
#        A(I,J) = 0
#
#  Example:
#
#    ALPHA = 7, N = 5
#
#     506 -254    0    0    0
#    -252  505 -253    0    0
#       0 -252  504 -252    0
#       0    0 -253  505 -252
#       0    0    0 -254  506
#
#  Properties:
#
#    A is generally not symmetric: A' /= A.
#
#    A is row diagonally dominant, since the absolute value of the diagonal
#    entry always equals ( or exceeds, I = 1 and N ) the sum of the
#    absolute values of the two off diagonal row entries.
#
#    A is irreducibly diagonally dominant, and hence nonsingular.
#
#    A is tridiagonal.
#
#    Because A is tridiagonal, it has property A (bipartite).
#
#    A is banded, with bandwidth 3.
#
#    A is an M matrix.
#
#    0 < INVERSE(A).
#
#    A is centrosymmetric: A(I,J) = A(N+1-I,N+1-J).
#
#    A is symmetrizable.  There is a positive definite diagonal matrix
#    D so that INVERSE(D)*A*D is symmetric.
#
#    The eigenvalues of A are positive, so the matrix
#    INVERSE(D)*A*D is positive definite.
#
#    The Gauss-Seidel and Jacobi iterative methods for solving
#    A*x = b both converge.  Furthermore, if RHO(GS) is the
#    spectral radius of the Gauss-Seidel iteration matrix, and
#    RHO(J) the spectral radius of the Jacobi iteration matrix,
#    then RHO(GS) = RHO(J)^2 < 1.
#
#    A is ill-conditioned for small values of ALPHA.  The
#    test case used N = 100, and ALPHA=0.01, 0.003, 0.001 and
#    1.0D-10.  The matrix A was already very ill-conditioned for
#    ALPHA = 0.003, with the minimum eigenvalue being 1.8D-12, and
#    the maximum one being 199.87.
#
#    The columns of INVERSE(A) vary greatly in norm.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Fred Dorr,
#    An example of ill-conditioning in the numerical solution of
#    singular perturbation problems,
#    Mathematics of Computation,
#    Volume 25, Number 114, 1971, pages 271-283.
#
#  Parameters:
#
#    Input, real ALPHA, scalar that defines the matrix.
#    A typical value of ALPHA is 0.01.
#
#    Input, integer N, the order of A.
#
#    Output, real A(N,N), the matrix.
#
  import numpy as np

  a = np.zeros ( ( n, n ) )

  np1_r8 = float ( n + 1 )

  for i in range ( 0, n ):
    for j in range ( 0, n ):
 
      if ( i + 1 <= ( ( n + 1 ) // 2 ) ):

        if ( j == i - 1 ):
          a[i,j] = - alpha * np1_r8 ** 2
        elif ( j == i ):
          a[i,j] = 2.0 * alpha * np1_r8 ** 2 + 0.5 * np1_r8 - float ( i + 1 )
        elif ( j == i + 1 ):
          a[i,j] = - alpha * np1_r8 ** 2 - 0.5 * np1_r8 + float ( i + 1 )

      else:

        if ( j == i - 1 ):
          a[i,j] = - alpha * np1_r8 ** 2 + 0.5 * np1_r8 - float ( i + 1 )
        elif ( j == i ):
          a[i,j] = 2.0 * alpha * np1_r8 ** 2 - 0.5 * np1_r8 + float ( i + 1 )
        elif ( j == i + 1 ):
          a[i,j] = - alpha * np1_r8 ** 2
 
  return a

def dorr_determinant ( alpha, n ):

#*****************************************************************************80
#
## DORR_DETERMINANT returns the determinant of the DORR matrix.
#
#  Discussion:
#
#    The DORR matrix is a special case of the TRIV matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 March 2015
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
#
#  Form the three diagonals.
#
  x = np.zeros ( n - 1 )
  y = np.zeros ( n )
  z = np.zeros ( n - 1 )

  np1_r8 = float ( n + 1 )

  for i in range ( 0, n ):
    for j in range ( 0, n ):

      if ( i + 1 <=  ( ( n + 1 ) // 2 ) ):

        if ( j == i - 1 ):
          x[i-1] = - alpha * np1_r8 ** 2
        elif ( j == i ):
          y[i] = 2.0 * alpha * np1_r8 ** 2 + 0.5 * np1_r8 - float ( i + 1 )
        elif ( j == i + 1 ):
          z[i] = - alpha * np1_r8 ** 2 - 0.5 * np1_r8 + float ( i + 1 )

      else:

        if ( j == i - 1 ):
          x[i-1] = - alpha * np1_r8 ** 2 + 0.5 * np1_r8 - float ( i + 1 )
        elif ( j == i ):
          y[i] = 2.0 * alpha * np1_r8 ** 2 - 0.5 * np1_r8 + float ( i + 1 )
        elif ( j == i + 1 ):
          z[i] = - alpha * np1_r8 ** 2
#
#  Now evaluate the determinant.
#
  determ_nm1 = y[n-1]

  if ( n == 1 ):
    value = determ_nm1
    return value

  determ_nm2 = determ_nm1
  determ_nm1 = y[n-2] * y[n-1] - z[n-2] * x[n-2];

  if ( n == 2 ):
    value = determ_nm1
    return value

  for i in range ( n - 3, -1, -1 ):

    value = y[i] * determ_nm1 - z[i] * x[i] * determ_nm2

    determ_nm2 = determ_nm1
    determ_nm1 = value

  return value

def dorr_determinant_test ( ):

#*****************************************************************************80
#
## DORR_DETERMINANT_TEST tests DORR_DETERMINANT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 March 2015
#
#  Author:
#
#    John Burkardt
#
  from r8_uniform_ab import r8_uniform_ab
  from r8mat_print import r8mat_print

  print ''
  print 'DORR_DETERMINANT_TEST'
  print '  DORR_DETERMINANT computes the determinant of the DORR matrix.'
  print ''

  m = 5
  n = m

  r8_lo = -5.0
  r8_hi = +5.0
  seed = 123456789
  alpha, seed = r8_uniform_ab ( r8_lo, r8_hi, seed )

  a = dorr ( alpha, n )
  r8mat_print ( n, n, a, '  DORR matrix:' )

  value = dorr_determinant ( alpha, n )
  print ''
  print '  Value =  %8' % ( value )

  print ''
  print 'DORR_DETERMINANT_TEST'
  print '  Normal end of execution.'

  return

def dorr_inverse ( alpha, n ):

#*****************************************************************************80
#
## DORR_INVERSE returns the inverse of the DORR matrix.
#
#  Discussion:
#
#    The DORR matrix is a special case of the TRIV matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    CM daFonseca, J Petronilho,
#    Explicit Inverses of Some Tridiagonal Matrices,
#    Linear Algebra and Its Applications,
#    Volume 325, 2001, pages 7-21.
#
#  Parameters:
#
#    Input, real ALPHA, the parameter.
#
#    Input, integer N, the order of the matrix.
#
#    Output, real A(N,N), the inverse of the matrix.
#
  import numpy as np
  from r8_mop import r8_mop
#
#  Form the three diagonals.
#
  x = np.zeros ( n - 1 )
  y = np.zeros ( n )
  z = np.zeros ( n - 1 )

  np1 = float ( n + 1 )

  for i in range ( 0, n ):
    for j in range ( 0, n ):

      if ( i + 1 <= ( ( n + 1 ) // 2 ) ):

        if ( j == i - 1 ):
          x[i-1] = - alpha * np1 ** 2
        elif ( j == i ):
          y[i] = 2.0 * alpha * np1 ** 2 + 0.5 * np1 - float ( i + 1 )
        elif ( j == i + 1 ):
          z[i] = - alpha * np1 ** 2 - 0.5 * np1 + float ( i + 1 )

      else:

        if ( j == i - 1 ):
          x[i-1] = - alpha * np1 ** 2 + 0.5 * np1 - float ( i + 1 )
        elif ( j == i ):
          y[i] = 2.0 * alpha * np1 ** 2 - 0.5 * np1 + float ( i + 1 )
        elif ( j == i + 1 ):
          z[i] = - alpha * np1 ** 2
#
#  Now evaluate the inverse.
#
  a = np.zeros ( ( n, n ) )

  d = np.zeros ( n )
  e = np.zeros ( n )

  d[n-1] = y[n-1]
  for i in range ( n - 2, -1, -1 ):
    d[i] = y[i] - x[i] * z[i] / d[i+1]

  e[0] = y[0]
  for i in range ( 1, n ):
    e[i] = y[i] - x[i-1] * z[i-1] / e[i-1]

  for i in range ( 0, n ):

    for j in range ( 0, i + 1 ):

      p1 = 1.0
      for k in range ( j, i ):
        p1 = p1 * x[k]
      p2 = 1.0
      for k in range ( i + 1, n ):
        p2 = p2 * d[k]
      p3 = 1.0
      for k in range ( j, n ):
        p3 = p3 * e[k]
      a[i,j] = r8_mop ( i + j ) * p1 * p2 / p3

    for j in range ( i + 1, n ):

      p1 = 1.0
      for k in range ( i, j ):
        p1 = p1 * z[k]
      p2 = 1.0
      for k in range ( j + 1, n ):
        p2 = p2 * d[k]
      p3 = 1.0
      for k in range ( i, n ):
        p3 = p3 * e[k]
      a[i,j] = r8_mop ( i + j ) * p1 * p2 / p3

  return a

def dorr_test ( ):

#*****************************************************************************80
#
## DORR_TEST tests DORR.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 March 2015
#
#  Author:
#
#    John Burkardt
#
  from r8_uniform_ab import r8_uniform_ab
  from r8mat_print import r8mat_print

  print ''
  print 'DORR_TEST'
  print '  DORR computes the DORR matrix.'

  seed = 123456789

  n = 5
  r8_lo = -5.0
  r8_hi = +5.0
  alpha, seed = r8_uniform_ab ( r8_lo, r8_hi, seed )
  a = dorr ( alpha, n )
  r8mat_print ( n, n, a, '  DORR matrix:' )

  print ''
  print 'DORR_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  dorr_test ( )
  timestamp ( )
