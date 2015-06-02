#!/usr/bin/env python
#
def hermite_poly_phys ( n, x ):

#*****************************************************************************80
#
## HERMITE_POLY_PHYS evaluates the Hermite polynomials at X.
#
#  Differential equation:
#
#    Y'' - 2 X Y' + 2 N Y = 0
#
#  First terms:
#
#      1
#      2 X
#      4 X^2     -  2
#      8 X^3     - 12 X
#     16 X^4     - 48 X^2     + 12
#     32 X^5    - 160 X^3    + 120 X
#     64 X^6    - 480 X^4    + 720 X^2    - 120
#    128 X^7   - 1344 X^5   + 3360 X^3   - 1680 X
#    256 X^8   - 3584 X^6  + 13440 X^4  - 13440 X^2   + 1680
#    512 X^9   - 9216 X^7  + 48384 X^5  - 80640 X^3  + 30240 X
#   1024 X^10 - 23040 X^8 + 161280 X^6 - 403200 X^4 + 302400 X^2 - 30240
#
#  Recursion:
#
#    H(0,X) = 1,
#    H(1,X) = 2*X,
#    H(N,X) = 2*X * H(N-1,X) - 2*(N-1) * H(N-2,X)
#
#  Norm:
#
#    Integral ( -oo < X < oo ) exp ( - X^2 ) * H(N,X)^2 dX
#    = sqrt ( pi ) * 2^N * N!
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 July 2004
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Milton Abramowitz and Irene Stegun,
#    Handbook of Mathematical Functions,
#    US Department of Commerce, 1964.
#
#  Parameters:
#
#    Input, integer N, the highest order polynomial to compute.
#    Note that polynomials 0 through N will be computed.
#
#    Input, real X, the point at which the polynomials are to be evaluated.
#
#    Output, real CX[0:N], the values of the first N+1 Hermite
#    polynomials at the point X.
#
  import numpy as np

  cx = np.zeros ( n + 1 )

  cx[0] = 1.0

  if ( 0 < n ):

    cx[1] = 2.0 * x
 
    for i in range ( 2, n + 1 ):
      cx[i] = 2.0 * x * cx[i-1] - 2.0 * ( i - 1 ) * cx[i-2]

  return cx

def hermite_poly_phys_test ( ):

#*****************************************************************************80
#
## HERMITE_POLY_PHYS_TEST tests HERMITE_POLY_PHYS.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    12 February 2015
#
#  Author:
#
#    John Burkardt
#
  from hermite_poly_phys_values import hermite_poly_phys_values
 
  print ''
  print 'HERMITE_POLY_PHYS_TEST'
  print '  HERMITE_POLY_PHYS computes the Hermite physicist polynomials;'
  print ''
  print '       N      X        Exact F       H(N)(X)'
  print ''

  n_data = 0

  while ( True ):

    n_data, n, x, fx = hermite_poly_phys_values ( n_data )

    if ( n_data == 0 ):
      break

    fx2 = hermite_poly_phys ( n, x )

    print '  %2d  %12f  %14g  %14g' % ( n, x, fx, fx2[n] )

  print ''
  print 'HERMITE_POLY_PHYS_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  hermite_poly_phys_test ( )
  timestamp ( )
