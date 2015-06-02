#!/usr/bin/env python
#
def gud ( x ):

#*****************************************************************************80
#
## GUD evaluates the Gudermannian function.
#
#  Discussion:
#
#    The Gudermannian function relates the hyperbolic and trigonometric
#    functions.  For any argument X, there is a corresponding value
#    G so that
#
#      sinh(x) = tan(g).
#
#    The value G is called the Gudermannian of X.
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
#    Input, real X, the argument of the Gudermannian.
#
#    Output, real VALUE, the value of the Gudermannian.
#
  from math import atan
  from math import tanh

  value = 2.0 * atan ( tanh ( 0.5 * x ) )

  return value

def gud_test ( ):

#*****************************************************************************80
#
## GUD_TEST tests GUD.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    16 December 2014
#
#  Author:
#
#    John Burkardt
#
  from gud_values import gud_values

  print ''
  print 'GUD_TEST'
  print '  GUD evaluates the Gudermannian function.'
  print ''
  print '     X      Exact F       GUD(X)'
  print ''

  n_data = 0

  while ( True ):

    n_data, x, fx = gud_values ( n_data )

    if ( n_data == 0 ):
      break

    fx2 = gud ( x )

    print '  %10.6f  %24.16f  %24.16f  %10.4g' % (
      x, fx, fx2, abs ( fx - fx2 ) )
 
  print ''
  print 'GUD_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  gud_test ( )
  timestamp ( )
