#!/usr/bin/env python
#
def r8_cotd ( degrees ):

#*****************************************************************************80
#
## R8_COTD returns the cotangent of an angle given in degrees.
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
#  Parameters:
#
#    Input, real DEGREES, the angle in degrees.
#
#    Output, real VALUE, the cotangent of the angle.
#
  from math import cos
  from math import pi
  from math import sin

  radians = pi * ( degrees / 180.0 )

  value = cos ( radians ) / sin ( radians )

  return value

def r8_cotd_test ( ):

#*****************************************************************************80
#
## R8_COTD_TEST tests R8_COTD.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    12 January 2015
#
#  Author:
#
#    John Burkardt
#
  print ''
  print 'R8_COTD_TEST'
  print '  R8_COTD computes the cotangent of an angle'
  print '  given in degrees.'
  print ''
  print '  ANGLE    R8_COTD(ANGLE)'
  print ''
 
  for i in range ( 0, 375, 15 ):
    angle = float ( i )
    if ( ( i % 180 ) == 0 ):
      print '  %8.2f    Undefined' % ( angle )
    else:
      print '  %8.2f  %14.6g' % ( angle, r8_cotd ( angle ) )
#
#  Terminate.
#
  print ''
  print 'R8_COTD_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8_cotd_test ( )
  timestamp ( )
