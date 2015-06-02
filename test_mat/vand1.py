#! /usr/bin/env python
#
def vand1 ( n, x ):

#*****************************************************************************80
#
## VAND1 returns the VAND1 matrix.
#
#  Formula:
#
#    A(I,J) = X(J)^(I-1)
#
#  Example:
#
#    N = 5, X = ( 2, 3, 4, 5, 6 )
#
#    1  1   1   1   1
#    2  3   4   5   6
#    4  9  16  25  36
#    8 27  64 125  216
#   16 81 256 625 1296
#
#  Properties:
#
#    A is generally not symmetric: A' /= A.
#
#    A is nonsingular if, and only if, the X values are distinct.
#
#    det ( A ) = product ( 1 <= I <= N ) ( 1 <= J < I ) ( X(I) - X(J) ).
#             = product ( 1 <= J <= N ) X(J)
#             * product ( 1 <= I < J ) ( X(J) - X(I) ).
#
#    A is generally ill-conditioned.
#
#    The family of matrices is nested as a function of N.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Robert Gregory, David Karney,
#    A Collection of Matrices for Testing Computational Algorithms,
#    Wiley, 1969, page 27,
#    LC: QA263.G68.
#
#    Nicholas Higham,
#    Stability analysis of algorithms for solving confluent
#    Vandermonde-like systems,
#    SIAM Journal on Matrix Analysis and Applications,
#    Volume 11, 1990, pages 23-41.
#
#  Parameters:
#
#    Input, integer N, the order of the matrix desired.
#
#    Input, real X(N), the values that define A.
#
#    Output, real A(N,N), the matrix.
#
  import numpy as np

  a = np.zeros ( ( n, n ) )

  for i in range ( 0, n ):
    for j in range ( 0, n):

      if ( i == 0 and x[j] == 0.0 ):
        a[i,j] = 1.0
      else:
        a[i,j] = x[j] ** i

  return a

def vand1_determinant ( n, x ):

#*****************************************************************************80
#
## VAND1_DETERMINANT computes the determinant of the VAND1 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the order of the matrix.
#
#    Input, real X(N), the parameters.
#
#    Output, real VALUE, the determinant.
#
  value = 1.0;

  for i in range ( 0, n ):
    for j in range ( 0, i ):
      value = value * ( x[i] - x[j] )

  return value

def vand1_determinant_test ( ):

#*****************************************************************************80
#
## VAND1_DETERMINANT_TEST tests VAND1_DETERMINANT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 February 2015
#
#  Author:
#
#    John Burkardt
#
  from vand1 import vand1
  from r8vec_uniform_ab import r8vec_uniform_ab
  from r8mat_print import r8mat_print

  print ''
  print 'VAND1_DETERMINANT_TEST'
  print '  VAND1_DETERMINANT computes the VAND1 determinant.'

  m = 5
  n = m
  r8_lo = -5.0
  r8_hi = +5.0
  seed = 123456789
  x, seed = r8vec_uniform_ab ( n, r8_lo, r8_hi, seed )

  a = vand1 ( n, x )

  r8mat_print ( m, n, a, '  VAND1 matrix:' )

  value = vand1_determinant ( n, x )

  print ''
  print '  Value =  %g' % ( value )

  print ''
  print 'VAND1_DETERMINANT_TEST'
  print '  Normal end of execution.'

  return

def vand1_inverse ( n, x ):

#*****************************************************************************80
#
## VAND1_INVERSE returns the inverse of the VAND1 matrix.
#
#  Formula:
#
#    A(I,J) = coefficient of X^(J-1) in I-th Lagrange basis polynomial.
#
#  Example:
#
#    N = 5, 
#    X = ( 2, 3, 4, 5, 6 )
#
#     15.00  -14.25    4.96  -0.75   0.04
#    -40.00   44.67  -17.33   2.83  -0.17
#     45.00  -54.00   22.75  -4.00   0.25
#    -24.00   30.00  -13.33   2.50  -0.17
#      5.00   -6.42    2.96  -0.58   0.04
#
#  Properties:
#
#    The sum of the entries of A is
#
#      1 - product ( 1 <= I <= N ) ( 1 - 1 / X(I) ).
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
#  Parameters:
#
#    Input, integer N, the order of the matrix.
#
#    Input, real X(N), the values that define A.
#
#    Output, real A(N,N), the matrix.
#
  import numpy as np

  a = np.zeros ( ( n, n ) )

  for i in range ( 0, n ):
    a[i,0] = 1.0

  for i in range ( 0, n ):

    index = 0

    for k in range ( 0, n ):

      if ( k != i ):

        for j in range ( index + 1, -1, -1 ):

          a[i,j] = - x[k] * a[i,j] / ( x[i] - x[k] )

          if ( 0 < j ):
            a[i,j] = a[i,j] + a[i,j-1] / ( x[i] - x[k] )

        index = index + 1

  return a

def vand1_test ( ):

#*****************************************************************************80
#
## VAND1_TEST tests VAND1.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 February 2015
#
#  Author:
#
#    John Burkardt
#
  from r8vec_uniform_ab import r8vec_uniform_ab
  from r8mat_print import r8mat_print

  print ''
  print 'VAND1_TEST'
  print '  VAND1 computes the VAND1 matrix.'

  m = 5
  n = m
  r8_lo = -5.0
  r8_hi = +5.0
  seed = 123456789
  x, seed = r8vec_uniform_ab ( n, r8_lo, r8_hi, seed )

  a = vand1 ( n, x )
 
  r8mat_print ( m, n, a, '  VAND1 matrix:' )

  print ''
  print 'VAND1_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  vand1_test ( )
  timestamp ( )
