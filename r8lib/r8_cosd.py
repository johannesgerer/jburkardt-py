#!/usr/bin/env python
#
def r8_cosd ( degrees ):

#*****************************************************************************80
#
## R8_COSD returns the cosine of an angle given in degrees.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    11 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real DEGREES, the angle in degrees.
#
#    Output, real VALUE, the cosine of the angle.
#
  from math import cos

  r8_pi = 3.141592653589793
  radians = r8_pi * ( degrees / 180.0 )

  value = cos ( radians )

  return value

def r8_cosd_test ( ):

#*****************************************************************************80
#
## R8_COSD_TEST tests R8_COSD.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    11 January 2015
#
#  Author:
#
#    John Burkardt
#
  print ''
  print 'R8_COSD_TEST'
  print '  R8_COSD computes the cosine of an angle'
  print '  given in degrees.'
  print ''
  print '  ANGLE    R8_COSD(ANGLE)'
  print ''
 
  for i in range ( 0, 375, 15 ):
    angle = float ( i )
    print '  %8.2f  %14.6g' % ( angle, r8_cosd ( angle ) )
#
#  Terminate.
#
  print ''
  print 'R8_COSD_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8_cosd_test ( )
  timestamp ( )
