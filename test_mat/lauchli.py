#! /usr/bin/env python
#
def lauchli ( alpha, m, n ):

#*****************************************************************************80
#
## LAUCHLI returns the LAUCHLI matrix.
#
#  Discussion:
#
#    The Lauchli matrix is of order M by N, with M = N + 1.
#
#    This matrix is a well-known example in least squares that indicates
#    the danger of forming the matrix of the normal equations,  A' * A.
#
#    A common value for ALPHA is sqrt(EPS) where EPS is the machine epsilon.
#
#  Formula:
#
#    if ( I = 1 )
#      A(I,J) = 1
#    else if ( I-1 = J )
#      A(I,J) = ALPHA
#    else
#      A(I,J) = 0
#
#  Example:
#
#    M = 5, N = 4
#    ALPHA = 2
#
#    1  1  1  1
#    2  0  0  0
#    0  2  0  0
#    0  0  2  0
#    0  0  0  2
#
#  Properties:
#
#    The matrix is singular in a simple way.  The first row is
#    equal to the sum of the other rows, divided by ALPHA.
#
#    if ( ALPHA /= 0 )
#      rank ( A ) = N - 1
#    else if ( ALPHA == 0 )
#      rank ( A ) = 1
#
#    The family of matrices is nested as a function of N.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Peter Lauchli,
#    Jordan-Elimination und Ausgleichung nach kleinsten Quadraten,
#    (Jordan elimination and smoothing by least squares),
#    Numerische Mathematik,
#    Volume 3, Number 1, December 1961, pages 226-240.
#
#  Parameters:
#
#    Input, real ALPHA, the scalar defining the matrix.
#
#    Input, integer M, N, the order of A.  It should be the case
#    that M = N + 1.
#
#    Output, real A(M,N), the matrix.
#
  import numpy as np

  a = np.zeros ( ( m, n ) )

  for i in range ( 0, m ):
    for j in range ( 0, n ):
 
      if ( i == 0 ):
        a[i,j] = 1.0
      elif ( i == j + 1 ):
        a[i,j] = alpha

  return a

def lauchli_null_left ( alpha, m, n ):

#*****************************************************************************80
#
## LAUCHLI_NULL_LEFT returns a left null vector of the LAUCHLI matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real ALPHA, the scalar defining the matrix.
#
#    Input, integer M, N, the order of A.
#    It should be the case that M = N + 1.
#
#    Output, real X(M), the vector.
#
  import numpy as np

  x = np.zeros ( m )

  x[0] = - alpha
  for i in range ( 1, m ):
    x[i] = 1.0

  return x

def lauchli_null_left_test ( ):

#*****************************************************************************80
#
## LAUCHLI_NULL_LEFT_TEST tests LAUCHLI_NULL_LEFT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 March 2015
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
  print 'LAUCHLI_NULL_LEFT_TEST'
  print '  LAUCHLI_NULL_LEFT returns a left null vector of the LAUCHLI matrix.'
  print ''

  m = 5
  n = m - 1

  r8_lo = -5.0
  r8_hi = +5.0
  seed = 123456789
  alpha, seed = r8_uniform_ab ( r8_lo, r8_hi, seed )

  a = lauchli ( alpha, m, n )
  r8mat_print ( m, n, a, '  LAUCHLI matrix A:' )

  x = lauchli_null_left ( alpha, m, n )
  r8vec_print ( m, x, '  Left null vector X:' )

  value = r8mat_is_null_left ( m, n, a, x )

  print ''
  print '  ||x\'*A||/||x|| =  %g' % ( value )

  print ''
  print 'LAUCHLI_NULL_LEFT_TEST'
  print '  Normal end of execution.'

  return

def lauchli_test ( ):

#*****************************************************************************80
#
## LAUCHLI_TEST tests LAUCHLI.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 March 2015
#
#  Author:
#
#    John Burkardt
#
  from r8_uniform_01 import r8_uniform_01
  from r8mat_print import r8mat_print

  print ''
  print 'LAUCHLI_TEST'
  print '  LAUCHLI computes the LAUCHLI matrix.'

  seed = 123456789

  m = 5
  n = m - 1
  alpha, seed = r8_uniform_01 ( seed )
  a = lauchli ( alpha, m, n )
  r8mat_print ( m, n, a, '  LAUCHLI matrix:' )

  print ''
  print 'LAUCHLI_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  lauchli_test ( )
  lauchli_null_left_test ( )
  timestamp ( )
