#!/usr/bin/env python
#
def legendre_function_q ( n, x ):

#*****************************************************************************80
#
## LEGENDRE_FUNCTION_Q evaluates the Legendre QN functions.
#
#  Differential equation:
#
#    (1-X*X) Y'' - 2 X Y' + N (N+1) = 0
#
#  First terms:
#
#    Q(0)(X) = 0.5 * log((1+X)/(1-X))
#    Q(1)(X) = Q(0)(X)*X - 1 
#    Q(2)(X) = Q(0)(X)*(3*X*X-1)/4 - 1.5*X
#    Q(3)(X) = Q(0)(X)*(5*X*X*X-3*X)/4 - 2.5*X^2 + 2/3
#    Q(4)(X) = Q(0)(X)*(35*X^4-30*X^2+3)/16 - 35/8 * X^3 + 55/24 * X
#    Q(5)(X) = Q(0)(X)*(63*X^5-70*X^3+15*X)/16 - 63/8*X^4 + 49/8*X^2 - 8/15
#
#  Recursion:
#
#    Q(0) = 0.5 * log ( (1+X) / (1-X) )
#    Q(1) = 0.5 * X * log ( (1+X) / (1-X) ) - 1.0
#
#    Q(N) = ( (2*N-1) * X * Q(N-1) - (N-1) * Q(N-2) ) / N
#
#  Restrictions:
#
#    -1 < X < 1
#
#  Special values:
#
#    Note that the Legendre function Q(N)(X) is equal to the
#    associated Legendre function of the second kind,
#    Q(N,M)(X) with M = 0.
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
#  Reference:
#
#    Milton Abramowitz and Irene Stegun,
#    Handbook of Mathematical Functions,
#    US Department of Commerce, 1964.
#
#  Parameters:
#
#    Input, integer N, the highest order function to evaluate.
#
#    Input, real X, the point at which the functions are to be
#    evaluated.  X must satisfy -1 < X < 1.
#
#    Output, real CX(1:N+1), the values of the first N+1 Legendre
#    functions at the point X.
#
  import numpy as np
#
#  Check the value of X.
#
  if ( x <= -1.0 or 1.0 <= x ):
    print ''
    print 'LEGENDRE_FUNCTION_Q - Fatal error!'
    print '  Illegal input value of X = %f' % ( x )
    print '  But X must be between -1 and 1.'

  cx = np.zeros ( n + 1 )

  cx[0] = 0.5 * np.log ( ( 1.0 + x ) / ( 1.0 - x ) )

  if ( 0 < n ):

    cx[1] = x * cx[0] - 1.0

    for i in range ( 2, n + 1 ):
      cx[i] = ( float ( 2 * i - 1 ) * x * cx[i]     \
            +   float (   - i + 1 )     * cx[i-1] ) \
            /   float (     i     )

  return cx

def legendre_function_q_test ( ):

#*****************************************************************************80
#
## LEGENDRE_FUNCTION_Q_TEST tests LEGENDRE_FUNCTION_Q.
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
  from legendre_function_q_values import legendre_function_q_values

  print ''
  print 'LEGENDRE_FUNCTION_Q_TEST'
  print '  LEGENDRE_FUNCTION_Q computes Legendre QN functions'
  print ''
  print '     N      X        Exact F       Q(N)(X)'
  print ''

  n_data = 0

  while ( True ):

    n_data, n, x, f = legendre_function_q_values ( n_data )

    if ( n_data == 0 ):
      break

    f2 = legendre_function_q ( n, x )

    print '  %6d  %6f  %12f  %12f' % ( n, x, f, f2[n] )

  print ''
  print 'LEGENDRE_FUNCTION_Q_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  legendre_function_q_test ( )
  timestamp ( )
