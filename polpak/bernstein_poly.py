#!/usr/bin/env python
#
def bernstein_poly ( n, x ):

#*****************************************************************************80
#
## BERNSTEIN_POLY evaluates the Bernstein polynomials at a point X.
#
#  Discussion:
#
#    The Bernstein polynomials are assumed to be based on [0,1].
#
#  Formula:
#
#    B(N,I)(X) = [N!/(I!*(N-I)!)] * (1-X)^(N-I) * X^I
#
#  First values:
#
#    B(0,0)(X) = 1
#
#    B(1,0)(X) =      1-X
#    B(1,1)(X) =                X
#
#    B(2,0)(X) =     (1-X)^2
#    B(2,1)(X) = 2 * (1-X)    * X
#    B(2,2)(X) =                X^2
#
#    B(3,0)(X) =     (1-X)^3
#    B(3,1)(X) = 3 * (1-X)^2  * X
#    B(3,2)(X) = 3 * (1-X)    * X^2
#    B(3,3)(X) =                X^3
#
#    B(4,0)(X) =     (1-X)^4
#    B(4,1)(X) = 4 * (1-X)^3  * X
#    B(4,2)(X) = 6 * (1-X)^2  * X^2
#    B(4,3)(X) = 4 * (1-X)    * X^3
#    B(4,4)(X) =                X^4
#
#  Special values:
#
#    B(N,I)(X) has a unique maximum value at X = I/N.
#
#    B(N,I)(X) has an I-fold zero at 0 and and N-I fold zero at 1.
#
#    B(N,I)(1/2) = C(N,K) / 2^N
#
#    For a fixed X and N, the polynomials add up to 1:
#
#      Sum ( 0 <= I <= N ) B(N,I)(X) = 1
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    31 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the degree of the Bernstein polynomials to be
#    used.  For any N, there is a set of N+1 Bernstein polynomials,
#    each of degree N, which form a basis for polynomials on [0,1].
#
#    Input, real X, the evaluation point.
#
#    Output, real BERN[0:N], the values of the N+1 Bernstein polynomials at X.
#
  import numpy as np

  bern = np.zeros ( n + 1 );

  if ( n == 0 ):
 
    bern[0] = 1.0
 
  else:
 
    bern[0] = 1.0 - x
    bern[1] = x
 
    for i in range ( 2, n + 1 ):
      bern[i] = x * bern[i-1]
      for j in range ( i - 1, 0, -1 ):
        bern[j] = x * bern[j-1] + ( 1.0 - x ) * bern[j]
      bern[0] = ( 1.0 - x ) * bern[0]

  return bern

def bernstein_poly_test ( ):

#*****************************************************************************80
#
## BERNSTEIN_POLY_TEST tests BERNSTEIN_POLY.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    31 December 2014
#
#  Author:
#
#    John Burkardt
#
  from bernstein_poly_01_values import bernstein_poly_01_values

  print ''
  print 'BERNSTEIN_POLY_TEST'
  print '  BERNSTEIN_POLY computes Bernstein polynomials;'
  print ''
  print '   N   K    X             Exact         B(N,K)(X)'
  print ''

  n_data = 0

  while ( True ):

    n_data, n, k, x, b = bernstein_poly_01_values ( n_data )

    if ( n_data == 0 ):
      break

    bvec = bernstein_poly ( n, x )

    print '  %2d  %2d  %5g  %12g  %12g' % ( n, k, x, b, bvec[k] )
 
  print ''
  print 'BERNSTEIN_POLY_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  bernstein_poly_test ( )
  timestamp ( )
