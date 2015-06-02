#!/usr/bin/env python
#
def legendre_poly ( n, x ):

#*****************************************************************************80
#
## LEGENDRE_POLY evaluates the Legendre polynomials P(N)(X) at X.
#
#  Discussion:
#
#    P(N)(1) = 1.
#    P(N)(-1) = (-1)^N.
#    abs ( P(N)(X) ) <= 1 in [-1,1].
#
#    P(N,0)(X) = P(N)(X), that is, for M=0, the associated Legendre
#    function of the first kind and order N equals the Legendre polynomial
#    of the first kind and order N.
#
#    The N zeroes of P(N)(X) are the abscissas used for Gauss-Legendre
#    quadrature of the integral of a function F(X) with weight function 1
#    over the interval [-1,1].
#
#    The Legendre polynomials are orthogonal under the inner product defined
#    as integration from -1 to 1:
#
#      Integral ( -1 <= X <= 1 ) P(I)(X) * P(J)(X) dX 
#        = 0 if I =/= J
#        = 2 / ( 2*I+1 ) if I = J.
#
#    Except for P(0)(X), the integral of P(I)(X) from -1 to 1 is 0.
#
#    A function F(X) defined on [-1,1] may be approximated by the series
#      C0*P(0)(X) + C1*P(1)(X) + ... + CN*P(N)(X)
#    where
#      C(I) = (2*I+1)/(2) * Integral ( -1 <= X <= 1 ) F(X) P(I)(X) dx.
#
#  Differential equation:
#
#    (1-X*X) * P(N)(X)'' - 2 * X * P(N)(X)' + N * (N+1) = 0
#
#  First terms:
#
#    P( 0)(X) =      1
#    P( 1)(X) =      1 X
#    P( 2)(X) = (    3 X^2 -       1)/2
#    P( 3)(X) = (    5 X^3 -     3 X)/2
#    P( 4)(X) = (   35 X^4 -    30 X^2 +     3)/8
#    P( 5)(X) = (   63 X^5 -    70 X^3 +    15 X)/8
#    P( 6)(X) = (  231 X^6 -   315 X^4 +   105 X^2 -     5)/16
#    P( 7)(X) = (  429 X^7 -   693 X^5 +   315 X^3 -    35 X)/16
#    P( 8)(X) = ( 6435 X^8 - 12012 X^6 +  6930 X^4 -  1260 X^2 +   35)/128
#    P( 9)(X) = (12155 X^9 - 25740 X^7 + 18018 X^5 -  4620 X^3 +  315 X)/128
#    P(10)(X) = (46189 X^10-109395 X^8 + 90090 X^6 - 30030 X^4 + 3465 X^2-63 )/256
#
#  Recursion:
#
#    P(0)(X) = 1
#    P(1)(X) = X
#    P(N)(X) = ( (2*N-1)*X*P(N-1)(X)-(N-1)*P(N-2)(X) ) / N
#
#    P'(0)(X) = 0
#    P'(1)(X) = 1
#    P'(N)(X) = ( (2*N-1)*(P(N-1)(X)+X*P'(N-1)(X)-(N-1)*P'(N-2)(X) ) / N
#
#  Formula:
#
#    P(N)(X) = (1/2**N) * sum ( 0 <= M <= N/2 ) C(N,M) C(2N-2M,N) X^(N-2*M)
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 August 2004
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
#    Daniel Zwillinger, editor,
#    CRC Standard Mathematical Tables and Formulae,
#    30th Edition,
#    CRC Press, 1996.
#
#  Parameters:
#
#    Input, integer N, the highest order polynomial to evaluate.
#    Note that polynomials 0 through N will be evaluated.
#
#    Input, real X, the point at which the polynomials are to be evaluated.
#
#    Output, real CX(1:N+1), the values of the Legendre polynomials 
#    of order 0 through N at the point X.
#
#    Output, real CPX(1:N+1), the values of the derivatives of the
#    Legendre polynomials of order 0 through N at the point X.
#
  import numpy as np

  cx = np.zeros ( n + 1 )
  cpx = np.zeros ( n + 1 )

  cx[0] = 1.0
  cpx[0] = 0.0

  if ( 0 < n ):

    cx[1] = x
    cpx[1] = 1.0
 
    for i in range ( 2, n + 1 ):
 
      cx[i] = ( float ( 2 * i - 1 ) * x * cx[i-1] \
              - float (     i - 1 ) *   cx[i-2] ) \
              / float (     i     )
 
      cpx[i] = ( float ( 2 * i - 1 ) * ( cx[i-1] + x * cpx[i-1] ) \
               - float (     i - 1 ) *   cpx[i-2]               ) \
               / float (     i     )

  return cx, cpx

def legendre_poly_test ( ):

#*****************************************************************************80
#
## LEGENDRE_POLY_TEST tests LEGENDRE_POLY.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 February 2015
#
#  Author:
#
#    John Burkardt
#
  from legendre_poly_values import legendre_poly_values

  print ''
  print 'LEGENDRE_POLY_TEST'
  print '  LEGENDRE_POLY computes Legendre polynomials;'
  print ''
  print '     N      X        Exact F       L(N)(X)'
  print ''

  n_data = 0

  while ( True ):

    n_data, n, x, f = legendre_poly_values ( n_data )

    if ( n_data == 0 ):
      break

    f2, fp2 = legendre_poly ( n, x )

    print '  %6d  %6f  %12f  %12f' % ( n, x, f, f2[n] )

  print ''
  print 'LEGENDRE_POLY_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  legendre_poly_test ( )
  timestamp ( )
