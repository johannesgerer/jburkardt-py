#!/usr/bin/env python
#
def legendre_associated_normalized ( n, m, x ):

#*****************************************************************************80
#
## LEGENDRE_ASSOCIATED_NORMALIZED evaluates the associated Legendre functions.
#
#  Discussion:
#
#    The unnormalized associated Legendre functions P_N^M(X) have
#    the property that
#
#      Integral ( -1 <= X <= 1 ) ( P_N^M(X) )^2 dX
#      = 2 * ( N + M )! / ( ( 2 * N + 1 ) * ( N - M )! )
#
#    By dividing the function by the square root of this term,
#    the normalized associated Legendre functions have norm 1.
#
#    However, we plan to use these functions to build spherical
#    harmonics, so we use a slightly different normalization factor of
#
#      sqrt ( ( ( 2 * N + 1 ) * ( N - M )! ) / ( 4 * pi * ( N + M )! ) )
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    20 February 2015
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
#    Input, integer N, the maximum first index of the Legendre
#    function, which must be at least 0.
#
#    Input, integer M, the second index of the Legendre function,
#    which must be at least 0, and no greater than N.
#
#    Input, real X, the point at which the function is to be
#    evaluated.  X must satisfy -1 <= X <= 1.
#
#    Output, real CX(1:N+1), the values of the first N+1 function.
#
  import numpy as np
  from r8_factorial import r8_factorial

  if ( m < 0 ):
    print ''
    print 'LEGENDRE_ASSOCIATED_NORMALIZED - Fatal error!'
    print '  Input value of M is %d' % ( m )
    print '  but M must be nonnegative.'
 
  if ( n < m ):
    print ''
    print 'LEGENDRE_ASSOCIATED_NORMALIZED - Fatal error!'
    print '  Input value of M = %d' % ( m )
    print '  Input value of N = %d' % ( n )
    print '  but M must be less than or equal to N.'
 
  if ( x < -1.0 ):
    print ''
    print 'LEGENDRE_ASSOCIATED_NORMALIZED - Fatal error!'
    print '  Input value of X = %f' % ( x )
    print '  but X must be no less than -1.'

  if ( 1.0 < x ):
    print ''
    print 'LEGENDRE_ASSOCIATED_NORMALIZED - Fatal error!'
    print '  Input value of X = %f' % ( x )
    print '  but X must be no more than 1.'
  
  cx = np.zeros ( n + 1 )

  cx[m] = 1.0
  somx2 = np.sqrt ( 1.0 - x * x )
 
  fact = 1.0
  for i in range ( 0, m ):
    cx[m] = - cx[m] * fact * somx2
    fact = fact + 2.0
 
  if ( m != n ):

    cx[m+1] = x * float ( 2 * m + 1 ) * cx[m]

    for i in range ( m + 2, n + 1 ):
      cx[i] = ( float ( 2 * i     - 1 ) * x * cx[i-1] \
              + float (   - i - m + 1 ) *     cx[i-2] ) \
              / float (     i - m     )
#
#  Normalization.
#
  for mm in range ( m, n + 1 ):

    factor = np.sqrt ( ( ( 2 * mm + 1 ) * r8_factorial ( mm - m ) ) \
      / ( 4.0 * np.pi * r8_factorial ( mm + m ) ) )

    cx[mm] = cx[mm] * factor

  return cx

def legendre_associated_normalized_test ( ):

#*****************************************************************************80
#
## LEGENDRE_ASSOCIATED_NORMALIZED_TEST tests LEGENDRE_ASSOCIATED_NORMALIZED.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    20 February 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  from legendre_associated_normalized_sphere_values import legendre_associated_normalized_sphere_values

  print ''
  print 'LEGENDRE_ASSOCIATED_NORMALIZED_TEST'
  print '  LEGENDRE_ASSOCIATED_NORMALIZED evaluates the associated Legendre functions;'

  print ''
  print '      N       M    X     Exact F     PNM(X)'
  print ''

  n_data = 0

  while ( True ):

    n_data, n, m, x, f = legendre_associated_normalized_sphere_values ( n_data )

    if ( n_data == 0 ):
      break

    f2 = legendre_associated_normalized ( n, m, x )

    print '  %6d  %6d  %6f  %12f  %12f' % ( n, m, x, f, f2[n] )

  print ''
  print 'LEGENDRE_ASSOCIATED_NORMALIZED_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  legendre_associated_normalized_test ( )
  timestamp ( )
