#!/usr/bin/env python
#
def jacobi_poly ( n, alpha, beta, x ):

#*****************************************************************************80
#
## JACOBI_POLY evaluates the Jacobi polynomials at X.
#
#  Differential equation:
#
#    (1-X*X) Y'' + (BETA-ALPHA-(ALPHA+BETA+2) X) Y' + N (N+ALPHA+BETA+1) Y = 0
#
#  Recursion:
#
#    P(0,ALPHA,BETA,X) = 1,
#
#    P(1,ALPHA,BETA,X) = ( (2+ALPHA+BETA)*X + (ALPHA-BETA) ) / 2
#
#    P(N,ALPHA,BETA,X)  = 
#      ( 
#        (2*N+ALPHA+BETA-1) 
#        * ((ALPHA**2-BETA**2)+(2*N+ALPHA+BETA)*(2*N+ALPHA+BETA-2)*X) 
#        * P(N-1,ALPHA,BETA,X)
#        -2*(N-1+ALPHA)*(N-1+BETA)*(2*N+ALPHA+BETA) * P(N-2,ALPHA,BETA,X)
#      ) / 2*N*(N+ALPHA+BETA)*(2*N-2+ALPHA+BETA)
#
#  Restrictions:
#
#    -1 < ALPHA
#    -1 < BETA
#
#  Norm:
#
#    Integral ( -1 <= X <= 1 ) ( 1 - X )**ALPHA * ( 1 + X )**BETA 
#      * P(N,ALPHA,BETA,X)**2 dX 
#    = 2**(ALPHA+BETA+1) * Gamma ( N + ALPHA + 1 ) * Gamma ( N + BETA + 1 ) /
#      ( 2 * N + ALPHA + BETA ) * N! * Gamma ( N + ALPHA + BETA + 1 )
#
#  Special values:
#
#    P(N,ALPHA,BETA)(1) = (N+ALPHA)!/(N!*ALPHA!) for integer ALPHA.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    15 February 2015
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
#    Input, integer N, the highest order polynomial to compute.  Note
#    that polynomials 0 through N will be computed.
#
#    Input, real ALPHA, one of the parameters defining the Jacobi
#    polynomials, ALPHA must be greater than -1.
#
#    Input, real BETA, the second parameter defining the Jacobi
#    polynomials, BETA must be greater than -1.
#
#    Input, real X, the point at which the polynomials are to be evaluated.
#
#    Output, real CX(1:N+1), the values of the first N+1 Jacobi
#    polynomials at the point X.
#
  import numpy as np
  from sys import exit

  if ( alpha <= -1.0 ):
    print ''
    print 'JACOBI_POLY - Fatal error!'
    print '  Illegal input value of ALPHA = %f' % ( alpha )
    print '  But ALPHA must be greater than -1.'
    exit ( 'JACOBI_POLY - Fatal error!' )
 
  if ( beta <= -1.0 ):
    print ''
    print 'JACOBI_POLY - Fatal error!'
    print '  Illegal input value of BETA = %f' % ( beta )
    print '  But BETA must be greater than -1.'
    exit ( 'JACOBI_POLY - Fatal error!' )
  
  cx = np.zeros ( n + 1 );

  cx[0] = 1.0

  if ( 0 < n ):

    cx[1] = ( 1.0 + 0.5 * ( alpha + beta ) ) * x  + 0.5 * ( alpha - beta );
 
    for i in range ( 2, n + 1 ):

      c1 = 2 * i * ( i + alpha + beta ) * ( 2 * i - 2 + alpha + beta )

      c2 = ( 2 * i - 1 + alpha + beta ) * ( 2 * i + alpha + beta ) \
        * ( 2 * i - 2 + alpha + beta )

      c3 = ( 2 * i - 1 + alpha + beta ) * ( alpha + beta ) * ( alpha - beta )

      c4 = - 2 * ( i - 1 + alpha ) * ( i - 1 + beta )  * ( 2 * i + alpha + beta )

      cx[i] = ( ( c3 + c2 * x ) * cx[i-1] + c4 * cx[i-2] ) / c1

  return cx

def jacobi_poly_test ( ):

#*****************************************************************************80
#
## JACOBI_POLY_TEST tests JACOBI_POLY.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    15 February 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  from jacobi_poly_values import jacobi_poly_values

  print ''
  print 'JACOBI_POLY_TEST'
  print '  JACOBI_POLY computes values of the Jacobi polynomial.'
  print ''
  print '       N       A       B        X       GPV      JACOBI'
  print ''

  n_data = 0

  while ( True ):

    [ n_data, n, a, b, x, fx ] = jacobi_poly_values ( n_data )

    if ( n_data == 0 ):
      break

    c = jacobi_poly ( n, a, b, x )
    fx2 = c[n];

    print '  %6d  %8g  %8g  %8g  %12g  %12g' % ( n, a, b, x, fx, fx2 )

 
  print ''
  print 'JACOBI_POLY_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  jacobi_poly_test ( )
  timestamp ( )
