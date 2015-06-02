#!/usr/bin/env python
#
def r8_secd ( degrees ):

#*****************************************************************************80
#
## R8_SECD returns the secant of an angle given in degrees.
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
#    Output, real VALUE, the secant of the angle.
#
  from math import cos
  from math import pi

  radians = pi * ( degrees / 180.0 )

  value = 1.0 / cos ( radians )

  return value

def r8_secd_test ( ):

#*****************************************************************************80
#
## R8_SECD_TEST tests R8_SECD.
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
  print 'R8_SECD_TEST'
  print '  R8_SECD computes the secant of an angle'
  print '  given in degrees.'
  print ''
  print '  ANGLE    R8_SECD(ANGLE)'
  print ''
 
  for i in range ( 0, 375, 15 ):
    angle = float ( i )
    if ( ( ( i + 90 ) % 180 ) == 0 ):
      print '  %8.2f    Undefined' % ( angle )
    else:
      print '  %8.2f  %14.6g' % ( angle, r8_secd ( angle ) )
#
#  Terminate.
#
  print ''
  print 'R8_SECD_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8_secd_test ( )
  timestamp ( )
