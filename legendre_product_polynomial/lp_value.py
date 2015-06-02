#!/usr/bin/env python

def lp_value ( n, o, x ):

#*****************************************************************************80
#
## LP_VALUE evaluates the Legendre polynomials P(n,x).
#
#  Discussion:
#
#    P(n,1) = 1.
#    P(n,-1) = (-1)^N.
#    | P(n,x) | <= 1 in [-1,1].
#
#    The N zeroes of P(n,x) are the abscissas used for Gauss-Legendre
#    quadrature of the integral of a function F(X) with weight function 1
#    over the interval [-1,1].
#
#    The Legendre polynomials are orthogonal under the inner product defined
#    as integration from -1 to 1:
#
#      Integral ( -1 <= X <= 1 ) P(I,X) * P(J,X) dX
#        = 0 if I =/= J
#        = 2 / ( 2*I+1 ) if I = J.
#
#    Except for P(0,X), the integral of P(I,X) from -1 to 1 is 0.
#
#    A function F(X) defined on [-1,1] may be approximated by the series
#      C0*P(0,x) + C1*P(1,x) + ... + CN*P(n,x)
#    where
#      C(I) = (2*I+1)/(2) * Integral ( -1 <= X <= 1 ) F(X) P(I,x) dx.
#
#    The formula is:
#
#      P(n,x) = (1/2^N) * sum ( 0 <= M <= N/2 ) C(N,M) C(2N-2M,N) X^(N-2*M)
#
#  Differential equation:
#
#    (1-X*X) * P(n,x)'' - 2 * X * P(n,x)' + N * (N+1) = 0
#
#  First terms:
#
#    P( 0,x) =      1
#    P( 1,x) =      1 X
#    P( 2,x) = (    3 X^2 -       1)/2
#    P( 3,x) = (    5 X^3 -     3 X)/2
#    P( 4,x) = (   35 X^4 -    30 X^2 +     3)/8
#    P( 5,x) = (   63 X^5 -    70 X^3 +    15 X)/8
#    P( 6,x) = (  231 X^6 -   315 X^4 +   105 X^2 -     5)/16
#    P( 7,x) = (  429 X^7 -   693 X^5 +   315 X^3 -    35 X)/16
#    P( 8,x) = ( 6435 X^8 - 12012 X^6 +  6930 X^4 -  1260 X^2 +   35)/128
#    P( 9,x) = (12155 X^9 - 25740 X^7 + 18018 X^5 -  4620 X^3 +  315 X)/128
#    P(10,x) = (46189 X^10-109395 X^8 + 90090 X^6 - 30030 X^4 + 3465 X^2-63)/256
#
#  Recursion:
#
#    P(0,x) = 1
#    P(1,x) = x
#    P(n,x) = ( (2*n-1)*x*P(n-1,x)-(n-1)*P(n-2,x) ) / n
#
#    P'(0,x) = 0
#    P'(1,x) = 1
#    P'(N,x) = ( (2*N-1)*(P(N-1,x)+X*P'(N-1,x)-(N-1)*P'(N-2,x) ) / N
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    31 October 2014
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Milton Abramowitz, Irene Stegun,
#    Handbook of Mathematical Functions,
#    National Bureau of Standards, 1964,
#    ISBN: 0-486-61272-4,
#    LC: QA47.A34.
#
#    Daniel Zwillinger, editor,
#    CRC Standard Mathematical Tables and Formulae,
#    30th Edition,
#    CRC Press, 1996.
#
#  Parameters:
#
#    Input, int N, the number of evaluation points.
#
#    Input, int O, the degree of the polynomial.
#
#    Input, double X[N], the evaluation points.
#
#    Output, double V[N], the value of the Legendre polynomial 
#    of degree N at the points X.
#
  import numpy as np

  vtable = np.zeros ( [ n, o + 1 ], dtype = np.float64 )

  for i in range ( 0, n ):
    vtable[i][0] = 1.0

  if ( 1 <= o ):
    for i in range ( 0, n ):
      vtable[i][1] = x[i]

    for j in range ( 2, o + 1 ):
      for i in range ( 0, n ):
        vtable[i][j] = \
          ( ( 2 * j - 1 ) * x[i] * vtable[i][j-1]   \
          - (     j - 1 ) *        vtable[i][j-2] ) \
          / (     j     )

  v = np.zeros ( n, dtype = np.float64 )

  for i in range ( 0, n ):
    v[i] = vtable[i][o]

  return v

def lp_value_test ( ):

#*****************************************************************************80
#
## LP_VALUE_TEST tests LP_VALUE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    31 October 2014
#
#  Author:
#
#    John Burkardt
#
  from lp_values import lp_values
  import numpy as np

  n = 1
  xvec = np.zeros ( 1, dtype = np.float64 )

  print ''
  print 'LP_VALUE_TEST:'
  print '  LP_VALUE evaluates a Legendre polynomial.'
  print ''
  print '                        Tabulated                 Computed'
  print '     O        X           L(O,X)                    L(O,X)',
  print '                   Error'
  print ''

  n_data = 0

  while ( True ):

    n_data, o, x, fx1 = lp_values ( n_data )

    if ( n_data == 0 ):
      break

    xvec[0] = x

    fx2 = lp_value ( n, o, xvec )

    e = fx1 - fx2[0]

    print '  %4d  %12.8f  %24.16g  %24.16g  %8.2g' % ( o, x, fx1, fx2[0], e )

  print ''
  print 'LP_VALUE_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp

  timestamp ( )
  lp_value_test ( )
  timestamp ( )
