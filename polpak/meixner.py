#!/usr/bin/env python
#
def meixner ( n, beta, c, x ):

#*****************************************************************************80
#
## MEIXNER evaluates Meixner polynomials at a point.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    23 February 2010
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
#    Input, integer N, the maximum order of the polynomial.  
#    N must be at least 0.
#
#    Input, real BETA, the Beta parameter.  0 < BETA.
#
#    Input, real C, the C parameter.  0 < C < 1.
#
#    Input, real X, the evaluation point.
#
#    Output, real VALUE(N+1), the value of the polynomials at X.
#
  import numpy as np

  value = np.zeros ( n + 1 )

  if ( beta <= 0.0 ):
    print ''
    print 'MEIXNER - Fatal error!'
    print '  Parameter BETA must be positive.'

  if ( c <= 0.0 or 1.0 <= c ):
    print ''
    print 'MEIXNER - Fatal error!'
    print '  Parameter C must be strictly between 0 and 1.'

  if ( n < 0 ):
    print ''
    print 'MEIXNER - Fatal error!'
    print '  Parameter N must be nonnegative.'

  value[0] = 1.0

  if ( 0 < n ):

    value[1] = ( c - 1.0 ) * x / beta / c + 1.0

    for i in range ( 1, n ):
      value[i+1] = ( \
        ( ( c - 1.0 ) * x + ( 1.0 + c ) * float ( i ) + beta * c ) * value[i] \
        - float ( i ) * value[i-1] \
        ) / ( float ( i ) + beta )

  return value

def meixner_test ( ):

#*****************************************************************************80
#
## MEIXNER_TEST tests MEIXNER.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    24 February 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  test_num = 3
  beta_test = np.array ( [ 0.5, 1.0, 2.0 ] )
  c_test = np.array ( [ 0.125, 0.25, 0.5 ] )
 
  print ''
  print 'MEIXNER_TEST:'
  print '  MEIXNER evaluates Meixner polynomials.'
  print ''
  print '       N      BETA         C         X        M(N,BETA,C,X)'

  for test in range ( 0, test_num ):

    n = 5
    beta = beta_test[test]
    c = c_test[test]

    for j in range ( 0, 6 ):

      x = float ( j ) / 2.0

      value = meixner ( n, beta, c, x )

      print ''

      for i in range ( 0, n + 1 ):

        print '  %8d  %8g  %8g  %8g  %14g' % ( i, beta, c, x, value[i] )

  print ''
  print 'MEIXNER_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  meixner_test ( )
  timestamp ( )
