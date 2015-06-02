#!/usr/bin/env python

def r8_sind ( degrees ):

#*****************************************************************************80
#
## R8_SIND returns the sine of an angle given in degrees.
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
#    Output, real VALUE, the sine of the angle.
#
  from math import pi
  from math import sin

  radians = pi * ( degrees / 180.0 )

  value = sin ( radians )

  return value

def r8_sind_test ( ):

#*****************************************************************************80
#
## R8_SIND_TEST tests R8_SIND.
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
  print 'R8_SIND_TEST'
  print '  R8_SIND computes the sine of an angle'
  print '  given in degrees.'
  print ''
  print '  ANGLE    R8_SIND(ANGLE)'
  print ''
 
  for i in range ( 0, 375, 15 ):
    angle = float ( i )
    print '  %8.2f  %14.6g' % ( angle, r8_sind ( angle ) )
#
#  Terminate.
#
  print ''
  print 'R8_SIND_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8_sind_test ( )
  timestamp ( )
