#!/usr/bin/env python

def r8_tand ( degrees ):

#*****************************************************************************80
#
## R8_TAND returns the tangent of an angle given in degrees.
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
#    Output, real VALUE, the tangent of the angle.
#
  from math import cos
  from math import pi
  from math import sin

  radians = pi * ( degrees / 180.0 )

  value = sin ( radians ) / cos ( radians )

  return value

def r8_tand_test ( ):

#*****************************************************************************80
#
## R8_TAND_TEST tests R8_TAND.
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
  print 'R8_TAND_TEST'
  print '  R8_TAND computes the tangent of an angle'
  print '  given in degrees.'
  print ''
  print '  ANGLE    R8_TAND(ANGLE)'
  print ''
 
  for i in range ( 0, 375, 15 ):
    angle = float ( i )
    if ( ( ( i + 90 ) % 180 ) == 0 ):
      print '  %8.2f    Undefined' % ( angle )
    else:
      print '  %8.2f  %14.6g' % ( angle, r8_tand ( angle ) )
#
#  Terminate.
#
  print ''
  print 'R8_TAND_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8_tand_test ( )
  timestamp ( )
