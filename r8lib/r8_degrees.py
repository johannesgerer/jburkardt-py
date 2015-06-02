#!/usr/bin/env python

def r8_degrees ( radians ):

#*****************************************************************************80
#
## R8_DEGREES converts an angle from radian to degree measure.
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
#    Input, real RADIANS, the angle measurement in radians.
#
#    Output, real VALUE, the angle measurement in degrees.
#
  pi = 3.141592653589793
  value = radians * 180.0 / pi

  return value

