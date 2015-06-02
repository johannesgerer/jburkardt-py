#! /usr/bin/env python
#
def vand2 ( n, x ):

#*****************************************************************************80
#
## VAND2 returns the VAND2 matrix.
#
#  Discussion:
#
#    This is the Vandermonde matrix with 1's in the first column.
#
#  Formula:
#
#    A(I,J) = X(J)^(J-1)
#
#  Example:
#
#    N = 5, X = ( 2, 3, 4, 5, 6 )
#
#    1 2  4   8   16
#    1 3  9  27   81
#    1 4 16  64  256
#    1 5 25 125  625
#    1 6 36 216 1296
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

      if ( j == 0 and x[i] == 0.0 ):
        a[i,j] = 1.0
      else:
        a[i,j] = x[i] ** j

  return a

def vand2_determinant ( n, x ):

#*****************************************************************************80
#
## VAND2_DETERMINANT computes the determinant of the VAND2 matrix.
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

def vand2_determinant_test ( ):

#*****************************************************************************80
#
## VAND2_DETERMINANT_TEST tests VAND2_DETERMINANT.
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
  from vand2 import vand2
  from r8vec_uniform_ab import r8vec_uniform_ab
  from r8mat_print import r8mat_print

  print ''
  print 'VAND2_DETERMINANT_TEST'
  print '  VAND2_DETERMINANT computes the VAND2 determinant.'

  m = 5
  n = m
  r8_lo = -5.0
  r8_hi = +5.0
  seed = 123456789
  x, seed = r8vec_uniform_ab ( n, r8_lo, r8_hi, seed )

  a = vand2 ( n, x )

  r8mat_print ( m, n, a, '  VAND2 matrix:' )

  value = vand2_determinant ( n, x )

  print ''
  print '  Value =  %g' % ( value )

  print ''
  print 'VAND2_DETERMINANT_TEST'
  print '  Normal end of execution.'

  return

def vand2_inverse ( n, x ):

#*****************************************************************************80
#
## VAND2_INVERSE returns the inverse of the VAND2 matrix.
#
#  Formula:
#
#    A(I,J) = coefficient of X^(I-1) in J-th Lagrange basis polynomial.
#
#  Example:
#
#    N = 5, X = ( 2, 3, 4, 5, 6 )
#
#     15.00  -40.00   45.00  -24.00   5.00
#    -14.25   44.67  -54.00   30.00  -6.42
#      4.96  -17.33   22.75  -13.33   2.96
#     -0.75    2.83   -4.00    2.50  -0.58
#      0.04   -0.17    0.25   -0.17   0.04
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

  for j in range ( 0, n ):
    a[0,j] = 1.0

  for i in range ( 0, n ):

    index = 0

    for k in range ( 0, n ):

      if ( k != i ):

        for j in range ( index + 1, -1, -1 ):
          a[j,i] = - x[k] * a[j,i] / ( x[i] - x[k] )

          if ( 0 < j ):
            a[j,i] = a[j,i] + a[j-1,i] / ( x[i] - x[k] )

        index = index + 1;

  return a

def vand2_plu ( n, x ):

#*****************************************************************************80
#
## VAND2_PLU returns the PLU factors of the Vandermonde2 matrix.
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
#  Reference:
#
#    Halil Oruc, George Phillips,
#    Explicit factorization of the Vandermonde matrix,
#    Linear Algebra and its Applications,
#    Volume 315, Number 1-3, 15 August 2000, pages 113-123.
#
#  Parameters:
#
#    Input, integer N, the order of the matrix.
#
#    Input, real X(N), the values that define the matrix.
#
#    Output, real P(N,N), L(N,N), U(N,N), the PLU factors.
#
  import numpy as np
  from complete_symmetric_poly import complete_symmetric_poly

  p = np.zeros ( ( n, n ) )

  for j in range ( 0, n ):
    p[j,j] = 1.0

  l = np.zeros ( ( n, n ) )

  for i in range ( 0, n ):
    for j in range ( 0, i + 1 ):
      l[i,j] = 1.0
      for k in range ( 0, j ):
        l[i,j] = l[i,j] * ( x[i] - x[k] ) / ( x[j] - x[k] )

  u = np.zeros ( ( n, n ) )

  for i in range ( 0, n ):
    for j in range ( i, n ):
      u[i,j] = complete_symmetric_poly ( i + 1, j - i, x )
      for k in range ( 0, i ):
        u[i,j] = u[i,j] * ( x[i] - x[k] )

  return p, l, u

def vand2_test ( ):

#*****************************************************************************80
#
## VAND2_TEST tests VAND2.
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
  print 'VAND2_TEST'
  print '  VAND2 computes the VAND2 matrix.'

  m = 5
  n = m
  r8_lo = -5.0
  r8_hi = +5.0
  seed = 123456789
  x, seed = r8vec_uniform_ab ( n, r8_lo, r8_hi, seed )

  a = vand2 ( n, x )
 
  r8mat_print ( m, n, a, '  VAND2 matrix:' )

  print ''
  print 'VAND2_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  vand2_test ( )
  timestamp ( )
