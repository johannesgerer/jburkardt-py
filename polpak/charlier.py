#!/usr/bin/env python
#
def charlier ( n, a, x ):

#*****************************************************************************80
#
## CHARLIER evaluates Charlier polynomials at a point.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    18 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    J Simoes Pereira,
#    Algorithm 234: Poisson-Charliers Polynomials,
#    Communications of the ACM,
#    Volume 7, Number 7, page 420, July 1964.
#
#    Walter Gautschi,
#    Orthogonal Polynomials: Computation and Approximation,
#    Oxford, 2004,
#    ISBN: 0-19-850672-4,
#    LC: QA404.5 G3555.
#
#    Gabor Szego,
#    Orthogonal Polynomials,
#    American Mathematical Society, 1975,
#    ISBN: 0821810235,
#    LC: QA3.A5.v23.
#
#    Eric Weisstein,
#    CRC Concise Encyclopedia of Mathematics,
#    CRC Press, 2002,
#    Second edition,
#    ISBN: 1584883472,
#    LC: QA5.W45.
#
#  Parameters:
#
#    Input, integer N, the maximum order of the polynomial.  
#    N must be at least 0.
#
#    Input, real A, the parameter.  A must not be 0.
#
#    Input, real X, the evaluation point.
#
#    Output, real V(0:N), the value of the polynomials at X.
#
  import numpy as np
  from sys import exit

  if ( a == 0.0 ):
    print ''
    print 'CHARLIER - Fatal error!'
    print '  Parameter A cannot be zero.'
    exit ( 'CHARLIER - Fatal error!' );

  if ( n < 0 ):
    print ''
    print 'CHARLIER - Fatal error!'
    print '  Parameter N must be nonnegative.'
    exit ( 'CHARLIER - Fatal error!' );

  v = np.zeros ( n + 1 )

  v[0] = 1.0

  if ( 0 < n ):
 
    v[1] = - x / a

    if ( 1 < n ):

      for i in range ( 2, n + 1 ):
        v[i] = ( ( i - 1 + a - x ) * v[i-1] - ( i - 1 ) * v[i-2] ) / a
 
  return v

def charlier_test ( ):

#*****************************************************************************80
#
## CHARLIER_TEST tests CHARLIER.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    18 January 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  test_num = 5
  a_test = np.array ( [ 0.25, 0.5, 1.0, 2.0, 10.0 ] )
  n = 5

  print ''
  print 'CHARLIER_TEST:'
  print '  CHARLIER evaluates Charlier polynomials.'
  print ''
  print '       N      A         X        P(N,A,X)'

  for test in range ( 0, test_num ):

    n = 5
    a = a_test[test]

    for j in range ( 0, 6 ):

      x = j / 2.0

      value = charlier ( n, a, x )

      print ''

      for i in range ( 0, n + 1 ):

        print '  %8d  %8f  %8f  %14f' % ( i, a, x, value[i] )

 
  print ''
  print 'CHARLIER_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  charlier_test ( )
  timestamp ( )
