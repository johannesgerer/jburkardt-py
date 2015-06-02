#!/usr/bin/env python

def r8_radians ( degrees ):

#*****************************************************************************80
#
## R8_RADIANS converts an angle from degree to radian measure.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    31 May 2013
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real DEGREES, the angle measurement in degrees.
#
#    Output, real VALUE, the angle measurement in radians.
#
  pi = 3.141592653589793
  value = degrees * pi / 180.0

  return value

