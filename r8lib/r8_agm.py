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
  from r8_epsilon import r8_epsilon
  from sys import exit

  it_max = 1000

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

  if ( a == b ):
    value = a
    return value

  it = 0
  tol = 100.0 * r8_epsilon ( )

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
#    14 May 2015
#
#  Author:
#
#    John Burkardt
#
  from agm_values import agm_values

  print ''
  print 'R8_AGM_TEST:'
  print '  R8_AGM computes the arithmetic geometric mean.'
  print ''
  print '             X              Y              AGM           AGM'
  print '                                           Exact         Computed'
  print ''

  n_data = 0

  while ( True ):

    n_data, x, y, fx1 = agm_values ( n_data )

    if ( n_data == 0 ):
      break
 
    fx2 = r8_agm ( x, y )

    print '  %14.6f  %14.6f  %24.16g  %24.16g' % ( x, y, fx1, fx2 )

#
#  Terminate.
#
  print ''
  print 'R8_AGM_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8_agm_test ( )
  timestamp ( )
