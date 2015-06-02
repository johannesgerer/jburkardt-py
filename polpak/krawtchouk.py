#!/usr/bin/env python
#
def krawtchouk ( n, p, x, m ):

#*****************************************************************************80
#
## KRAWTCHOUK evaluates the Krawtchouk polynomials at X.
#
#  Discussion:
#
#    The polynomial has a parameter P, which must be strictly between
#    0 and 1, and a parameter M which must be a nonnegative integer.
#
#    The Krawtchouk polynomial of order N, with parameters P and M,
#    evaluated at X, may be written K(N,P,X,M).
#
#    The first two terms are:
#
#      K(0,P,X,M) = 1
#      K(1,P,X,M) = X - P * M
#
#    and the recursion, for fixed P and M is
#
#                             ( N + 1 ) * K(N+1,P,X,M) =
#        ( X - ( N + P * ( M - 2 * N))) * K(N,  P,X,M)
#       - ( M - N + 1 ) * P * ( 1 - P ) * K(N-1,P,X,M)
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    17 February 2015
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
#    Input, integer N, the highest order polynomial to evaluate.
#    0 <= N.
#
#    Input, real P, the parameter.  0 < P < 1.
#
#    Input, real X, the evaluation parameter.
#
#    Input, integer M, the parameter.  0 <= M.
#
#    Output, real V[0:N], the values of the Krawtchouk polynomials
#    of orders 0 through N at X.
#
  import numpy as np

  v = []

  if ( n < 0 ):
    print ''
    print 'KRAWTCHOUK - Fatal error!'
    print '  0 <= N is required.'
    return v

  if ( p <= 0.0 or 1.0 <= p ):
    print ''
    print 'KRAWTCHOUK - Fatal error!'
    print '  0 < P < 1 is required.'
    return v

  if ( m < 0 ):
    print ''
    print 'KRAWTCHOUK - Fatal error!'
    print '  0 <= M is required.'
    return v

  v = np.zeros ( n + 1 )

  v[0] = 1.0

  if ( 1 <= n ):

    v[1] = x - p * m

    for i in range ( 1, n ):
      v[i+1] = ( ( x - float ( i + p * ( m - 2 * i ) ) )       * v[i] \
                     - float ( ( m - i + 1 ) * p * ( 1 - p ) ) * v[i-1]  ) \
                     / float ( i + 1 )

  return v

def krawtchouk_test ( ):

#*****************************************************************************80
#
## KRAWTCHOUK_TEST tests KRAWTCHOUK.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    17 February 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  test_num = 2
  p_test = np.array ( ( 0.25, 0.5 ) )
  m = 5

  print ''
  print 'KRAWTCHOUK_TEST'
  print '  KRAWTCHOUK computes Krawtchouk polynomials;'
  print ''
  print '         N      P         X          M     K(N,P,X,M)'

  for test in range ( 0, test_num ):

    n = 5
    p = p_test[test]

    print ''

    for j in range ( 0, 6 ):

      x = float ( j ) / 2.0

      value = krawtchouk ( n, p, x, m )

      print ''

      for i in range ( 0, n + 1 ):

        print '  %8d  %8f  %8f  %8d  %14f' % ( i, p, x, m, value[i] )

  print ''
  print 'KRAWTCHOUK_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  krawtchouk_test ( )
  timestamp ( )
