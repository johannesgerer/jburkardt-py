#! /usr/bin/env python
#
def tris ( m, n, x, y, z ):

#*****************************************************************************80
#
## TRIS returns the TRIS matrix.
#
#  Formula:
#
#    if ( J = I-1 )
#      A(I,J) = X
#    elseif ( J = I )
#      A(I,J) = Y
#    elseif ( J = I + 1 )
#      A(I,J) = Z
#    else
#      A(I,J) = 0
#
#  Example:
#
#    M = 5, N = 5, X = 1, Y = 2, Z = 3
#
#    2 3 0 0 0
#    1 2 3 0 0
#    0 1 2 3 0
#    0 0 1 2 3
#    0 0 0 1 2
#
#  Properties:
#
#    A is generally not symmetric: A' /= A.
#
#    A is tridiagonal.
#
#    Because A is tridiagonal, it has property A (bipartite).
#
#    A is banded, with bandwidth 3.
#
#    A is Toeplitz: constant along diagonals.
#
#    If Y is not zero, then for A to be singular, it must be the case that
#
#      0.5 * Y / sqrt ( X * Z ) < 1
#
#    and
#
#      cos (K*PI/(N+1)) = - 0.5 * Y / sqrt ( X * Z ) for some 1 <= K <= N.
#
#    If Y is zero, then A is singular when N is odd, or if X or Z is zero.
#
#    A is persymmetric: A(I,J) = A(N+1-J,N+1-I).
#
#    A has eigenvalues
#
#      LAMBDA(I) = Y + 2 * sqrt(X*Z) * COS(I*PI/(N+1))
#
#    The eigenvalues will be complex if X * Z < 0.
#
#    If X = Z, the matrix is symmetric.
#
#    As long as X and Z are nonzero, the matrix is irreducible.
#
#    If X = Z = -1, and Y = 2, the matrix is a symmetric, positive
#    definite M matrix, the negative of the second difference matrix.
#
#    The family of matrices is nested as a function of N.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    John Todd,
#    Basic Numerical Mathematics,
#    Volume 2: Numerical Algebra,
#    Academic Press, 1978, page 155.
#
#  Parameters:
#
#    Input, integer M, N, the order of A.
#
#    Input, real X, Y, Z, the scalars that define A.
#
#    Output, real A(M,N), the matrix.
#
  import numpy as np

  a = np.zeros ( ( m, n ) )

  for i in range ( 0, m ):
    for j in range ( 0, n ):

      if ( j == i - 1 ):
        a[i,j] = x
      elif ( j == i ):
        a[i,j] = y
      elif ( j == i + 1 ):
        a[i,j] = z

  return a

def tris_determinant ( n, x, y, z ):

#*****************************************************************************80
#
## TRIS_DETERMINANT computes the determinant of the TRIS matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the order of the matrix.
#
#    Input, real X, Y, Z, parameters.
#
#    Output, real VALUE, the determinant.
#
  import numpy as np

  value = 1.0

  if ( 0.0 <= x * z ):

    for i in range ( 1, n + 1 ):
      angle = float ( i ) * np.pi / float ( n + 1 )
      value = value * ( y + 2.0 * sqrt ( x * z ) * np.cos ( angle ) );

  else:

    i_hi = ( n // 2 )

    for i in range ( 1, i_hi + 1 ):
      angle = float ( i ) * np.pi / float ( n + 1 )
      value = value * ( y * y - 4.0 * x * z * ( np.cos ( angle ) ) ** 2 )

    if ( ( n % 2 ) == 1 ):
      value = value * y

  return value

def tris_determinant_test ( ):

#*****************************************************************************80
#
## TRIS_DETERMINANT_TEST tests TRIS_DETERMINANT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 February 2015
#
#  Author:
#
#    John Burkardt
#
  from tris import tris
  from r8_uniform_ab import r8_uniform_ab
  from r8mat_print import r8mat_print

  print ''
  print 'TRIS_DETERMINANT_TEST'
  print '  TRIS_DETERMINANT computes the TRIS determinant.'

  m = 5
  n = m

  r8_lo = -5.0
  r8_hi = +5.0
  seed = 123456789
  x, seed = r8_uniform_ab ( r8_lo, r8_hi, seed )
  y, seed = r8_uniform_ab ( r8_lo, r8_hi, seed )
  z, seed = r8_uniform_ab ( r8_lo, r8_hi, seed )

  a = tris ( m, n, x, y, z )

  r8mat_print ( m, n, a, '  TRIS matrix:' )

  value = tris_determinant ( n, x, y, z )

  print ''
  print '  Value =  %g' % ( value )

  print ''
  print 'TRIS_DETERMINANT_TEST'
  print '  Normal end of execution.'

  return

def tris_inverse ( n, alpha, beta, gam ):

#*****************************************************************************80
#
## TRIS_INVERSE returns the inverse of the TRIS matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 March 2015
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
#    Input, integer N, the order of the matrix.
#
#    Input, real ALPHA, BETA, GAM, the constant values associated with the 
#    subdiagonal, diagonal and superdiagonal of the matrix.
#
#    Output, real A(N,N), the inverse of the matrix.
#
  import numpy as np
  from r8_mop import r8_mop

  d = np.zeros ( n )
  d[n-1] = beta
  for i in range ( n - 2, -1, -1 ):
    d[i] = beta - alpha * gam / d[i+1]

  a = np.zeros ( ( n, n ) )

  for i in range ( 0, n ):
    for j in range ( 0, i + 1 ):
      p1 = 1.0
      for k in range ( i + 1, n ):
        p1 = p1 * d[k]
      p2 = 1.0
      for k in range ( 0, n - j ):
        p2 = p2 * d[k]
      a[i,j] = r8_mop ( i + j ) * alpha ** ( i - j ) * p1 / p2
    for j in range ( i + 1, n ):
      p1 = 1.0
      for k in range ( j + 1, n ):
        p1 = p1 * d[k]
      p2 = 1.0
      for k in range ( 0, n - i ):
        p2 = p2 * d[k]
      a[i,j] = r8_mop ( i + j ) * gam ** ( j - i ) * p1 / p2

  return a

def tris_test ( ):

#*****************************************************************************80
#
## TRIS_TEST tests TRIS.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 February 2015
#
#  Author:
#
#    John Burkardt
#
  from r8_uniform_ab import r8_uniform_ab
  from r8mat_print import r8mat_print

  print ''
  print 'TRIS_TEST'
  print '  TRIS computes the TRIS matrix.'

  m = 5
  n = m

  r8_lo = -5.0
  r8_hi = +5.0
  seed = 123456789
  x, seed = r8_uniform_ab ( r8_lo, r8_hi, seed )
  y, seed = r8_uniform_ab ( r8_lo, r8_hi, seed )
  z, seed = r8_uniform_ab ( r8_lo, r8_hi, seed )

  a = tris ( m, n, x, y, z )

  r8mat_print ( m, n, a, '  TRIS matrix:' )

  print ''
  print 'TRIS_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  tris_test ( )
  timestamp ( )
