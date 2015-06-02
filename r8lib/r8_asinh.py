#!/usr/bin/env python
#
def r8_asinh ( x ):

#*****************************************************************************80
#
## R8_ASINH returns the inverse hyperbolic sine of a number.
#
#  Definition:
#
#    The assertion that:
#
#      Y = ASINH2(X)
#
#    implies that
#
#      X = SINH(Y) = 0.5 * ( EXP(Y) - EXP(-Y) ).
#
#  Discussion:
#
#    Since a library function ASINH may be available on some systems,
#    this routine is named ASINH2 to avoid name conflicts.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    20 July 2004
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real X, the number whose inverse hyperbolic sine is desired.
#
#    Output, real VALUE, the inverse hyperbolic sine of X.
#
  from math import log
  from math import sqrt

  value = log ( x + sqrt ( x * x + 1.0 ) );

  return value

def r8_asinh_test ( ):

#*****************************************************************************80
#
## R8_ASINH_TEST tests R8_ASINH.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    17 December 2014
#
#  Author:
#
#    John Burkardt
#
  from math import sinh

  print ''
  print 'R8_ASINH_TEST'
  print '  R8_ASINH computes the inverse hyperbolic sine.'
  print ''
  print '        X           R8_ASINH(X)   SINH(R8_SINH(X))'
  print ''

  for i in range ( 0, 10 ):
    x = 1.0 + i / 5.0
    a = r8_asinh ( x )
    x2 = sinh ( a )
    print '  %12f  %12f  %12f' % ( x, a, x2 )
#
#  Terminate.
#
  print ''
  print 'R8_ASINH_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8_asinh_test ( )
  timestamp ( )
