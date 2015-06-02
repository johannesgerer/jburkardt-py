#!/usr/bin/env python
#
def gegenbauer_poly ( n, alpha, x ):

#*****************************************************************************80
#
## GEGENBAUER_POLY computes the Gegenbauer polynomials C(I,ALPHA)(X).
#
#  Discussion:
#
#    The Gegenbauer polynomial can be evaluated in Mathematica with
#    the command
#
#      GegenbauerC[n,m,x]
#
#  Differential equation:
#
#    (1-X*X) Y'' - (2 ALPHA + 1) X Y' + N (N + 2 ALPHA) Y = 0
#
#  Recursion:
#
#    C(0,ALPHA,X) = 1,
#    C(1,ALPHA,X) = 2*ALPHA*X
#    C(N,ALPHA,X) = (  ( 2*N-2+2*ALPHA) * X * C(N-1,ALPHA,X) 
#                    + (  -N+2-2*ALPHA)   *   C(N-2,ALPHA,X) ) / N
#
#  Restrictions:
#
#    ALPHA must be greater than -0.5.
#
#  Special values:
#
#    If ALPHA = 1, the Gegenbauer polynomials reduce to the Chebyshev
#    polynomials of the second kind.
#
#  Norm:
#
#    Integral ( -1 <= X <= 1 ) 
#      ( 1 - X^2 )^( ALPHA - 0.5 ) * C(N,ALPHA,X)^2 dX
#
#    = PI * 2^( 1 - 2 * ALPHA ) * Gamma ( N + 2 * ALPHA ) 
#      / ( N! * ( N + ALPHA ) * ( Gamma ( ALPHA ) )^2 )
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Stephen Wolfram,
#    The Mathematica Book,
#    Fourth Edition,
#    Wolfram Media / Cambridge University Press, 1999.
#
#  Parameters:
#
#    Input, integer N, the highest order polynomial to compute.
#    Note that polynomials 0 through N will be computed.
#
#    Input, real ALPHA, a parameter which is part of the definition of
#    the Gegenbauer polynomials.  It must be greater than -0.5.
#
#    Input, real X, the point at which the polynomials are to be evaluated.
#
#    Output, real CX(1:N+1), the values of the first N+1 Gegenbauer
#    polynomials at the point X.  
#
  import numpy as np

  if ( alpha <= -0.5 ):
    print ''
    print 'GEGENBAUER_POLY - Fatal error!'
    print '  Illegal value of ALPHA = %f' % ( alpha )
    print '  but ALPHA must be greater than -0.5.'
    sys.error ( 'GEGENBAUER_POLY - Fatal error!' );

  cx = np.zeros ( n + 1 );

  cx[0] = 1.0

  if ( 0 < n ):

    cx[1] = 2.0 * alpha * x

  for i in range ( 2, n + 1 ):
    cx[i] = ( float (     2 * i - 2  + 2.0 * alpha ) * x * cx[i]     \
           +  float (       - i + 2  - 2.0 * alpha ) *     cx[i-1] ) \
           /  float (         i );

  return cx

def gegenbauer_poly_test ( ):

#*****************************************************************************80
#
## GEGENBAUER_POLY_TEST tests GEGENBAUER_POLY.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 February 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  from gegenbauer_poly_values import gegenbauer_poly_values

  print ''
  print 'GEGENBAUER_POLY_TEST'
  print '  GEGENBAUER_POLY computes values of the Gegenbauer polynomial.'
  print ''
  print '       N       A       X       GPV      GEGENBAUER'
  print ''

  n_data = 0

  while ( True ):

    [ n_data, n, a, x, fx ] = gegenbauer_poly_values ( n_data )

    if ( n_data == 0 ):
      break

    c = gegenbauer_poly ( n, a, x )
    fx2 = c[n];

    print '  %6d  %8g  %8g  %12g  %12g' % ( n, a, x, fx, fx2 )

 
  print ''
  print 'GEGENBAUER_POLY_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  gegenbauer_poly_test ( )
  timestamp ( )
