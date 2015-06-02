#!/usr/bin/env python

def i4_to_angle ( i ) :

#*****************************************************************************80
#
## I4_TO_ANGLE maps integers to points on a circle.
#
#  Discussion:
#
#    The angles are intended to be used to select colors on a color
#    hexagon whose 6 vertices are red, yellow, green, cyan, blue,
#    magenta.
#
#  Example:
#
#     I   X      ANGLE
#
#     0   0/3      0
#     1   1/3    120
#     2   2/3    240
#
#     3   1/6     60
#     4   3/6    180
#     5   5/6    300
#
#     6   1/12    30
#     7   3/12    90
#     8   5/12   150
#     9   7/12   210
#    10   9/12   270
#    11  11/12   330
#
#    12   1/24    15
#    13   3/24    45
#    14   5/24    75
#    etc
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 May 2013
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer I, the index of the desired color.
#
#    Output, real ANGLE, an angle, measured in degrees, 
#    between 0 and 360.
#
  from i4_log_2 import i4_log_2
  from math import floor

  if ( 0 <= abs ( i ) and abs ( i ) <= 2 ):

    angle = 120.0 * abs ( i )

  else:

    i1 = i4_log_2 ( floor ( abs ( i ) / 3 ) )
    i2 = abs ( i ) + 1 - 3 * ( 2 ** i1 )
    i3 = 2 * ( i2 - 1 ) + 1
    i4 = 3 * ( 2 ** ( i1 + 1 ) )

    angle = ( 360.0 * i3 ) / i4

  return angle

def i4_to_angle_test ( ):

#*****************************************************************************80
#
## I4_TO_ANGLE_TEST tests I4_TO_ANGLE. 
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 May 2015
#
#  Author:
#
#    John Burkardt
#
  print ''
  print 'I4_TO_ANGLE_TEST'
  print '  I4_TO_ANGLE converts an I4 to an angle in degrees.'
  print '  The angles sample the circle at finer levels.'
  print ''
  print '  I4   ANGLE'
  print ''

  for i4 in range ( 0, 16 ):

    angle = i4_to_angle ( i4 )
    print '  %2d  %14.6g' % ( i4, angle )
#
#  Terminate.
#
  print ''
  print 'I4_TO_ANGLE_TEST'
  print '  Normal end of execution.'

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  i4_to_angle_test ( )
  timestamp ( )
