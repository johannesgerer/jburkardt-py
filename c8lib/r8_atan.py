#!/usr/bin/env python
#
def r8_atan ( y, x ):

#*****************************************************************************80
#
## R8_ATAN computes the inverse tangent of the ratio Y / X.
#
#  Discussion:
#
#    R8_ATAN returns an angle whose tangent is ( Y / X ), a job which
#    the built in functions ATAN and ATAN2 already do.
#
#    However:
#
#    * R8_ATAN always returns a positive angle, between 0 and 2 PI,
#      while ATAN and ATAN2 return angles in the interval [-PI/2,+PI/2]
#      and [-PI,+PI] respectively;
#
#    * R8_ATAN accounts for the signs of X and Y, (as does ATAN2).  The ATAN
#     function by contrast always returns an angle in the first or fourth
#     quadrants.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 October 2004
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real Y, X, two quantities which represent the tangent of
#    an angle.  If Y is not zero, then the tangent is (Y/X).
#
#    Output, real VALUE, an angle between 0 and 2 * PI, whose tangent is
#    (Y/X), and which lies in the appropriate quadrant so that the signs
#    of its cosine and sine match those of X and Y.
#
  from math import atan2

  r8_pi = 3.141592653589793
#
#  Special cases:
#
  if ( x == 0.0 ):

    if ( 0.0 < y ):
      value = r8_pi / 2.0
    elif ( y < 0.0 ):
      value = 3.0 * r8_pi / 2.0
    elif ( y == 0.0 ):
      value = 0.0

  elif ( y == 0.0 ):

    if ( 0.0 < x ):
      value = 0.0
    elif ( x < 0.0 ):
      value = r8_pi
#
#  We assume that ATAN2 is correct when both arguments are positive.
#
  else:

    abs_y = abs ( y )
    abs_x = abs ( x )

    theta_0 = atan2 ( abs_y, abs_x )

    if ( 0.0 < x and 0.0 < y ):
      value = theta_0
    elif ( x < 0.0 and 0.0 < y ):
      value = r8_pi - theta_0
    elif ( x < 0.0 and y < 0.0 ):
      value = r8_pi + theta_0
    elif ( 0.0 < x and y < 0.0 ):
      value = 2.0 * r8_pi - theta_0

  return value

def r8_atan_test ( ):

#*****************************************************************************80
#
## R8_ATAN_TEST tests R8_ATAN.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    24 July 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  from math import atan2

  ntest = 8

  xtest = np.array ( [ 1.0, 1.0, 0.0, -1.0, -1.0, -1.0,  0.0,  1.0 ] )
  ytest = np.array ( [ 0.0, 1.0, 1.0,  1.0,  0.0, -1.0, -1.0, -1.0 ] )

  print ''
  print 'R8_ATAN_TEST'
  print '  R8_ATAN computes the arc-tangent given Y and X;'
  print '  ATAN2 is the system version of this routine.'
  print ''
  print '  X     Y     ATAN2(Y,X)   R8_ATAN(Y,X)'
  print '';

  for i in range ( 0, ntest ):
    x = xtest[i]
    y = ytest[i]
    print '  %12f  %12f  %12f  %12f' % ( x, y, atan2 ( y, x ), r8_atan ( y, x ) )

  print ''
  print 'R8_ATAN_TEST'
  print '  Normal end of execution'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8_atan_test ( )
  timestamp ( )
