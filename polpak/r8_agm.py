#!/usr/bin/env python
#
def r8_agm ( a, b ):

#*****************************************************************************80
#
## R8_AGM computes the arithmetic-geometric mean of A and B.
#
#  Discussion:
#
#    The AGM is defined for nonnegative A and B.
#
#    The AGM of numbers A and B is defined by setting
#
#      A(0) = A,
#      B(0) = B
#
#      A(N+1) = ( A(N) + B(N) ) / 2
#      B(N+1) = sqrt ( A(N) * B(N) )
#
#    The two sequences both converge to AGM(A,B).
#
#    In Mathematica, the AGM can be evaluated by
#
#      ArithmeticGeometricMean [ a, b ]
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 July 2014
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
#    Input, real A, B, the arguments whose AGM is to be computed.
#    0 <= A, 0 <= B.
#
#    Output, real VALUE, the arithmetic-geometric mean of A and B.
#
  from math import sqrt
  from sys import exit

  it_max = 1000
  eps = 2.220446049250313E-016

  if ( a < 0.0 ):
    print ''
    print 'R8_AGM - Fatal error!'
    print '  Argument A < 0.'
    exit ( 'R8_AGM - Fatal error!' )

  if ( b < 0.0 ):
    print ''
    print 'R8_AGM - Fatal error!'
    print '  Argument B < 0.'
    exit ( 'R8_AGM - Fatal error!' )

  if ( a == 0.0 or b == 0.0 ):
    value = 0.0
    return value

  it = 0
  tol = 100.0 * eps

  a1 = a
  b1 = b

  while ( True ):

    it = it + 1

    a2 = ( a1 + b1 ) / 2.0
    b2 = sqrt ( a1 * b1 )

    if ( abs ( a2 - b2 ) <= tol * ( a2 + b2 ) ):
      break

    if ( it_max < it ):
      print ''
      print 'R8_AGM - Warning!'
      print '  No convergence.'
      break

    a1 = a2
    b1 = b2

  value = a2

  return value

def r8_agm_test ( ):

#*****************************************************************************80
#
## R8_AGM_TEST tests R8_AGM.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 December 2014
#
#  Author:
#
#    John Burkardt
#
  from agm_values import agm_values

  print ''
  print 'R8_AGM_TEST'
  print '  R8_AGM computes the arithmetic geometric mean.'
  print ''
  print '      A           B          ',
  print '   AGM                       AGM                   Diff'
  print '                             ',
  print '  (Tabulated)             R8_AGM(A,B)'
  print ''

  n_data = 0

  while ( True ):

    n_data, a, b, fx = agm_values ( n_data )

    if ( n_data == 0 ):
      break

    fx2 = r8_agm ( a, b )

    print '  %10.6f  %10.6f  %24.16f  %24.16f  %10.4g' % (
      a, b, fx, fx2, abs ( fx - fx2 ) )
 
  print ''
  print 'R8_AGM_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8_agm_test ( )
  timestamp ( )
