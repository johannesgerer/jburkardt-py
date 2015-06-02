#!/usr/bin/env python
#
def agud ( g ):

#*****************************************************************************80
#
## AGUD evaluates the inverse Gudermannian function.
#
#  Discussion:
#
#    The Gudermannian function relates the hyperbolic and trigonomentric
#    functions.  For any argument X, there is a corresponding value
#    G so that
#
#      SINH(X) = TAN(G).
#
#    This value G(X) is called the Gudermannian of X.  The inverse
#    Gudermannian function is given as input a value G and computes
#    the corresponding value X.
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
#    Input, real G, the value of the Gudermannian.
#
#    Output, real VALUE, the argument of the Gudermannian.
#
  from math import log
  from math import tan

  r8_pi = 3.141592653589793

  value = log ( tan ( 0.25 * r8_pi + 0.5 * g ) )

  return value

def agud_test ( ):

#*****************************************************************************80
#
## AGUD_TEST tests AGUD.
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
  from gud import gud

  print ''
  print 'AGUD_TEST'
  print '  AGUD evaluates the inverse Gudermannian function.'
  print ''
  print '        X            GUD(X)     AGUD(GUD(X))'
  print ''

  for i in range ( 0, 11 ):
    x = 1.0 + i / 5.0
    g = gud ( x )
    x2 = agud ( g )
    print '  %12f  %12f  %12f' % ( x, g, x2 )
 
  print ''
  print 'AGUD_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  agud_test ( )
  timestamp ( )
