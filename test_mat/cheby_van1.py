#! /usr/bin/env python
#
def cheby_van1 ( m, a, b, n, x ):

#*****************************************************************************80
#
## CHEBY_VAN1 returns the Chebyshev Vandermonde-like matrix for [A,B].
#
#  Discussion:
#
#    Normally, the Chebyshev polynomials are defined on -1 <= XI <= +1.
#    Here, we assume the Chebyshev polynomials have been defined on the
#    interval A <= X <= B, using the mapping
#      XI = ( - ( B - X ) + ( X - A ) ) / ( B - A )
#    so that
#      ChebyAB(A,B;X) = Cheby(XI).
#
#    if ( I == 1 ) then
#      V(1,1:N) = 1;
#    elseif ( I == 2 ) then
#      V(2,1:N) = XI(1:N);
#    else
#      V(I,1:N) = 2.0 * XI(1:N) * V(I-1,1:N) - V(I-2,1:N);
#
#  Example:
#
#    M = 5, A = -1, B = +1, N = 5, X = ( 1, 2, 3, 4, 5 )
#
#    1  1   1    1    1
#    1  2   3    4    5
#    1  7  17   31   49
#    1 26  99  244  485
#    1 97 577 1921 4801
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Nicholas Higham,
#    Stability analysis of algorithms for solving confluent
#    Vandermonde-like systems,
#    SIAM Journal on Matrix Analysis and Applications,
#    Volume 11, 1990, pages 23-41.
#
#  Parameters:
#
#    Input, integer M, the number of rows of the matrix.
#
#    Input, real A, B, the interval.
#
#    Input, integer N, the number of values in X, and the number
#    of columns in the matrix.
#
#    Input, real X(N), the abscissas.
#
#    Output, real V(M,N), the matrix.
#
  import numpy as np
#
#  Compute the normalized abscissas in [-1,+1].
#
  xi = np.zeros ( n )

  for i in range ( 0, n ):
    xi[i] = ( - 1.0 * ( b - x[i]     )   \
              + 1.0 * (     x[i] - a ) ) \
            /         ( b        - a )
#
#  Compute the matrix.
#
  v = np.zeros ( [ m, n ] );

  for j in range ( 0, n ):
    v[0,j] = 1.0
    v[1,j] = xi[j]
    for i in range ( 2, m ):
      v[i,j] = 2.0 * xi[j] * v[i-1,j] - v[i-2,j]

  return v

def cheby_van1_test ( ):

#*****************************************************************************80
#
## CHEBY_VAN1_TEST tests CHEBY_VAN1.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 January 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  from r8mat_print import r8mat_print

  print ''
  print 'CHEBY_VAN1_TEST'
  print '  CHEBY_VAN1 computes the CHEBY_VAN1 matrix.'

  m = 5
  x_lo = -5.0
  x_hi = +5.0
  x = np.linspace ( x_lo, x_hi, m )

  n = m
  a = cheby_van1 ( m, x_lo, x_hi, n, x )
  r8mat_print ( m, n, a, '  CHEBY_VAN1 matrix:' )

  print ''
  print 'CHEBY_VAN1_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  cheby_van1_test ( )
  timestamp ( )
