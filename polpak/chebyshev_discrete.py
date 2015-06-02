#!/usr/bin/env python
#
def chebyshev_discrete ( n, m, x ):

#*****************************************************************************80
#
## CHEBYSHEV_DISCRETE evaluates discrete Chebyshev polynomials at a point.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    19 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Walter Gautschi,
#    Orthogonal Polynomials: Computation and Approximation,
#    Oxford, 2004,
#    ISBN: 0-19-850672-4,
#    LC: QA404.5 G3555.
#
#  Parameters:
#
#    Input, integer N, the highest order of the polynomials to be evaluated.
#    0 <= N <= M.
#
#    Input, integer M, the maximum order of the polynomials.
#    0 <= M.
#
#    Input, real X, the evaluation point.
#
#    Output, real V(N+1), the value of the polynomials at X.
#
  import numpy as np
  from sys import exit

  if ( m < 0 ):
    print ''
    print 'CHEBYSHEV_DISCRETE - Fatal error!'
    print '  Parameter M must be nonnegative.'
    exit ( 'CHEBYSHEV_DISCRETE - Fatal error!');

  if ( n < 0 ):
    print ''
    print 'CHEBYSHEV_DISCRETE - Fatal error!'
    print '  Parameter N must be nonnegative.'
    exit ( 'CHEBYSHEV_DISCRETE - Fatal error!');

  if ( m < n ):
    print ''
    print 'CHEBYSHEV_DISCRETE - Fatal error!'
    print '  Parameter N must be no greater than M.'
    exit ( 'CHEBYSHEV_DISCRETE - Fatal error!');
 
  v = np.zeros ( n + 1 )

  v[0] = 1.0

  if ( 0 < n ):

    v[1] = 2.0 * x + 1 - m

    if ( 1 < n ):

      for i in range ( 1, n ):
        v[i+1] = ( \
          ( 2 * i + 1 ) * ( 2.0 * x + 1 - m ) * v[i] \
          - i * ( m + i ) * ( m - i ) * v[i-1] \
        ) / ( i + 1 )

  return v

def chebyshev_discrete_test ( ):

#*****************************************************************************80
#
## CHEBYSHEV_DISCRETE_TEST tests CHEBYSHEV_DISCRETE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    19 January 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
 
  print ''
  print 'CHEBYSHEV_DISCRETE_TEST'
  print '  CHEBY_T_POLY evaluates the Chebyshev T polynomial.'
  print ''
  print '       N      M         X        T(N,M,X)'
  print ''

  n = 5
  m = 5

  for j in range ( 0, 6 ):

    x = j / 2.0

    value = chebyshev_discrete ( n, m, x )

    print ''

    for i in range ( 0, n + 1 ): 

      print '  %8d  %8d  %12g  %12g' % ( i, m, x, value[i] )

 
  print ''
  print 'CHEBYSHEV_DISCRETE_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  chebyshev_discrete_test ( )
  timestamp ( )
