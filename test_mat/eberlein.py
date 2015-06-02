#! /usr/bin/env python
#
def eberlein ( alpha, n ):

#*****************************************************************************80
#
## EBERLEIN returns the Eberlein matrix.
#
#  Formula:
#
#    if ( I = J )
#      A(I,J) = - ( 2 * I - 1 ) * ( N - 1 ) - ( I - 1 ) * ALPHA + 2 * ( I - 1 )**2
#    else if ( J = I+1 )
#      A(I,J) = I * ( N + ALPHA - I )
#    else if ( J = I-1 )
#      A(I,J) = ( I - 1 ) * ( N - I + 1 )
#    else
#      A(I,J) = 0
#
#  Example:
#
#    N = 5, ALPHA = 2
#
#    -4   6   0   0   0
#     4 -12  10   0   0
#     0   6 -16  12   0
#     0   0   6 -16  12
#     0   0   0   4 -12
#
#  Properties:
#
#    A is generally not symmetric: A' /= A.
#
#    The matrix is tridiagonal.
#
#    Because A is tridiagonal, it has property A (bipartite).
#
#    A is banded, with bandwidth 3.
#
#    The sum of the entries in any row except the last one is ALPHA.
#
#    The sum of the entries in the last row is -(N-1)*ALPHA.
#
#    The sum of the entries in any column is zero.
#
#    A is singular.
#
#    det ( A ) = 0
#
#    A has the LEFT null vector ( 1, 1, ..., 1 ).
#
#    LAMBDA(I) = - ( I - 1 ) * ( ALPHA + I ).
#
#    Left eigenvectors are
#
#      V^J(I) = 1/COMB(N-1,I-1) * sum ( 0 <= K <= min ( I, J ) ) [ (-1)**K *
#        COMB(N-1-K,N-I) * COMB(J-1,K) * COMB(ALPHA+J-1+K, K )
#
#    For ALPHA = -2, ..., -2*(N-1), the matrix is defective with two or more
#    pairs of eigenvectors coalescing.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    24 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Patricia Eberlein,
#    A Two-Parameter Test Matrix,
#    Mathematics of Computation,
#    Volume 18, 1964, pages 296-298.
#
#    Joan Westlake,
#    Test Matrix A41,
#    A Handbook of Numerical Matrix Inversion and Solution of Linear Equations,
#    John Wiley, 1968.
#
#  Parameters:
#
#    Input, real ALPHA, the parameter.
#
#    Input, integer N, the order of A.
#
#    Output, real A(N,N), the matrix.
#
  import numpy as np

  a = np.zeros ( [ n, n ] )

  for i in range ( 0, n ):
    for j in range ( 0, n ):

      if ( j == i ):

        a[i,j] = - ( ( 2 * i + 1 ) * ( n - 1 )  +  i * alpha - 2 * i * i )

      elif ( j == i + 1 ):

        a[i,j] =  ( i + 1 ) * ( n - i - 1 + alpha )

      elif ( j == i - 1 ):

        a[i,j] = i * ( n - i )

  return a

def eberlein_determinant ( alpha, n ):

#*****************************************************************************80
#
## EBERLEIN_DETERMINANT returns the determinant of the EBERLEIN matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    24 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real ALPHA, the scalar defining A.  
#    A common value is 100.0.
#
#    Input, integer N, the order of the matrix.
#
#    Output, real DETERM, the determinant.
#
  determ = 0.0

  return determ

def eberlein_determinant_test ( ):

#*****************************************************************************80
#
## EBERLEIN_DETERMINANT_TEST tests EBERLEIN_DETERMINANT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    24 January 2015
#
#  Author:
#
#    John Burkardt
#
  from eberlein import eberlein
  from r8mat_print import r8mat_print
  from r8_uniform_ab import r8_uniform_ab

  print ''
  print 'EBERLEIN_DETERMINANT_TEST'
  print '  EBERLEIN_DETERMINANT computes the determinant of the EBERLEIN matrix.'
  print ''

  m = 4
  n = m

  r8_lo = -5.0
  r8_hi = +5.0
  seed = 123456789
  alpha, seed = r8_uniform_ab ( r8_lo, r8_hi, seed )

  a = eberlein ( alpha, n )
  r8mat_print ( m, n, a, '  EBERLEIN matrix:' )

  value = eberlein_determinant ( alpha, n )

  print ''
  print '  Value =  %g' % ( value )

  print ''
  print 'EBERLEIN_DETERMINANT_TEST'
  print '  Normal end of execution.'

  return

def eberlein_null_left ( m, n ):

#*****************************************************************************80
#
## EBERLEIN_NULL_LEFT returns a left null vector of the EBERLEIN matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    07 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, N, the order of the matrix.
#
#    Output, real X(M), the left null vector.
#
  import numpy as np

  x = np.ones ( m )

  return x

def eberlein_null_left_test ( ):

#*****************************************************************************80
#
## EBERLEIN_NULL_LEFT_TEST tests EBERLEIN_NULL_LEFT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    07 March 2015
#
#  Author:
#
#    John Burkardt
#
  from r8_uniform_ab import r8_uniform_ab
  from r8mat_is_null_left import r8mat_is_null_left
  from r8mat_print import r8mat_print
  from r8vec_print import r8vec_print

  print ''
  print 'EBERLEIN_NULL_LEFT_TEST'
  print '  EBERLEIN_NULL_LEFT returns a left null vector of the EBERLEIN matrix.'
  print ''

  m = 5
  n = 5

  r8_lo = -5.0
  r8_hi = +5.0
  seed = 123456789
  alpha, seed = r8_uniform_ab ( r8_lo, r8_hi, seed )

  a = eberlein ( alpha, n )
  r8mat_print ( m, n, a, '  EBERLEIN matrix A:' )

  x = eberlein_null_left ( m, n )
  r8vec_print ( m, x, '  Left null vector X:' )

  value = r8mat_is_null_left ( m, n, a, x )

  print ''
  print '  ||x\'*A||/||x|| =  %g' % ( value )

  print ''
  print 'EBERLEIN_NULL_LEFT_TEST'
  print '  Normal end of execution.'

  return

def eberlein_test ( ):

#*****************************************************************************80
#
## EBERLEIN_TEST tests EBERLEIN.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    24 January 2015
#
#  Author:
#
#    John Burkardt
#
  from r8mat_print import r8mat_print
  from r8_uniform_ab import r8_uniform_ab

  print ''
  print 'EBERLEIN_TEST'
  print '  EBERLEIN computes the EBERLEIN matrix.'

  m = 4
  n = m

  alpha_lo = 1.0
  alpha_hi = 100.0
  seed = 123456789
  alpha, seed = r8_uniform_ab ( alpha_lo, alpha_hi, seed )

  a = eberlein ( alpha, n )
  r8mat_print ( m, n, a, '  EBERLEIN matrix:' )

  print ''
  print 'EBERLEIN_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  eberlein_test ( )
  eberlein_determinant_test ( )
  eberlein_null_left_test ( )
  timestamp ( )
