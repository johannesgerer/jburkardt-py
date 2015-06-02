#!/usr/bin/env python

def r8_pi ( ):

#*****************************************************************************80
#
## R8_PI returns the value of pi as an R8.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    04 June 2013
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, real VALUE, the value of pi.
#
  value = 3.141592653589793

  return value

def r8_pi_test ( ):

#*****************************************************************************80
#
## R8_PI_TEST tests R8_PI.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 July 2014
#
#  Author:
#
#    John Burkardt
#
  from math import atan
  from math import pi

  print ''
  print 'R8_PI_TEST'
  print '  R8_PI returns the value of PI.'
  print ''
  v1 = r8_pi ( )
  print '  R8_PI =       %24.16f' % ( v1 )
  v2 = 4.0 * atan ( 1.0 )
  print '  4 * Atan(1) = %24.16f' % ( v2 )
  v3 = pi
  print '  PI    =       %24.16f' % ( v3 )
#
#  Terminate.
#
  print ''
  print 'R8_PI_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8_pi_test ( )
  timestamp ( )
