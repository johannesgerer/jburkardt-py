#!/usr/bin/env python
#
def gen_laguerre_poly ( n, alpha, x ):

#*****************************************************************************80
#
## GEN_LAGUERRE_POLY evaluates generalized Laguerre polynomials.
#
#  Differential equation:
#
#    X * Y'' + (ALPHA+1-X) * Y' + N * Y = 0
#
#  Recursion:
#
#    L(0,ALPHA)(X) = 1
#    L(1,ALPHA)(X) = 1+ALPHA-X
#
#    L(N,ALPHA)(X) = ( (2*N-1+ALPHA-X) * L(N-1,ALPHA)(X) 
#                   - (N-1+ALPHA) * L(N-2,ALPHA)(X) ) / N
#
#  Restrictions:
#
#    -1 < ALPHA
#
#  Special values:
#
#    For ALPHA = 0, the generalized Laguerre polynomial L(N,ALPHA)(X)
#    is equal to the Laguerre polynomial L(N)(X).
#
#    For ALPHA integral, the generalized Laguerre polynomial
#    L(N,ALPHA)(X) equals the associated Laguerre polynomial L(N,ALPHA)(X).
#
#  Norm:
#
#    Integral ( 0 <= X < Infinity ) exp ( - X ) * L(N,ALPHA)(X)**2 dX
#    = Gamma ( N + ALPHA + 1 ) / N!
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 February 2015
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
#    Input, integer N, the highest order function to compute.
#
#    Input, real ALPHA, the parameter.  -1 < ALPHA is required.
#
#    Input, real X, the point at which the functions are to be
#    evaluated.
#
#    Output, real CX(1:N+1), the polynomials of 
#    degrees 0 through N evaluated at the point X.
#
  import numpy as np
  from sys import exit

  if ( alpha <= -1.0 ):
    print ''
    print 'GEN_LAGUERRE_POLY - Fatal error!'
    print '  The input value of ALPHA is %f' % ( alpha )
    print '  but ALPHA must be greater than -1.'
    exit ( 'GEN_LAGUERRE_POLY - Fatal error!' )
 
  cx = np.zeros ( n + 1 )

  cx[0] = 1.0

  if ( 0 < n ):

    cx[1] = 1.0 + alpha - x

    for i in range ( 2, n ):
      cx[i] = ( ( float ( 2 * i - 1 ) + alpha - x ) * cx[i-1]     \
              + ( float (   - i + 1 ) - alpha     ) * cx[i-2] ) \
                / float (     i )

  return cx

def gen_laguerre_poly_test ( ):

#*****************************************************************************80
#
## GEN_LAGUERRE_POLY_TEST tests GEN_LAGUERRE_POLY.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 February 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 10

  alpha_test = np.array ( ( 0.0, 0.0, 0.1, 0.1, 0.5, 1.0 ) );
  x_test = np.array ( ( 0.0, 1.0, 0.0, 0.5, 0.5, 0.5 ) )

  print ''
  print 'GEN_LAGUERRE_POLY_TEST'
  print '  GEN_LAGUERRE_POLY evaluates the generalized Laguerre polynomial.'

  for i in range ( 0, 6 ):

    x = x_test[i]
    alpha = alpha_test[i]

    print ''
    print '  Table of L(N,ALPHA)(X) for'
    print ''
    print '    N(max) = %d' % ( n )
    print '    ALPHA =  %f' % ( alpha )
    print '    X =      %f' % ( x )
    print ''
  
    c = gen_laguerre_poly ( n, alpha, x )
 
    for j in range ( 0, n + 1 ):
      print '  %4d  %12f' % ( j, c[j] )
 
  print ''
  print 'GEN_LAGUERRE_POLY_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  gen_laguerre_poly_test ( )
  timestamp ( )
