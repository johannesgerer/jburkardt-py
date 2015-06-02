#!/usr/bin/env python
#
def r8_atanh ( x ):

#*****************************************************************************80
#
## R8_ATANH returns the inverse hyperbolic tangent of a number.
#
#  Discussion:
#
#    Y = R8_ATANH ( X )
#
#    implies that
#
#    X = TANH(Y) = ( EXP(Y) - EXP(-Y) ) / ( EXP(Y) + EXP(-Y) )
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    18 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real X, the number whose inverse hyperbolic
#    tangent is desired.  The absolute value of X should be less than
#    or equal to 1.
#
#    Output, real R8_ATANH, the inverse hyperbolic tangent of X.
#
  from math import log
  from sys import exit

  if ( 1.0 <= abs ( x ) ):
    print ''
    print 'R8_ATANH - Fatal error!'
    print '  ABS(X) must be < 1.'
    print '  Your input is X = %f' % ( x )
    exit ( 'R8_ATANH - Fatal error!' )

  value = 0.5 * log ( ( 1.0 + x ) / ( 1.0 - x ) )

  return value

def r8_atanh_test ( ):

#*****************************************************************************80
#
## R8_ATANH_TEST tests R8_ATANH.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    18 December 2014
#
#  Author:
#
#    John Burkardt
#
  from math import tanh

  print ''
  print 'R8_ATANH_TEST'
  print '  R8_ATANH computes the inverse hyperbolic tangent.'
  print ''
  print '        X           R8_ATANH(X)   TANH(R8_TANH(X))'
  print ''

  for i in range ( -2, 10 ):
    x = i / 10.0
    a = r8_atanh ( x )
    x2 = tanh ( a )
    print '  %12f  %12f  %12f' % ( x, a, x2 )
#
#  Terminate.
#
  print ''
  print 'R8_ATANH_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8_atanh_test ( )
  timestamp ( )
