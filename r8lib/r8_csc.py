#!/usr/bin/env python
#
def r8_csc ( theta ):

#*****************************************************************************80
#
## R8_CSC returns the cosecant of X.
#
#  Discussion:
#
#    R8_CSC ( THETA ) = 1.0 / SIN ( THETA )
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
#  Parameters:
#
#    Input, real THETA, the angle, in radians, whose cosecant is desired.
#    It must be the case that SIN ( THETA ) is not zero.
#
#    Output, real VALUE, the cosecant of THETA.
#
  from math import sin
  from sys import exit

  value = sin ( theta )

  if ( value == 0.0 )
    print ''
    print 'R8_CSC - Fatal error!'
    print '  Cosecant undefined for THETA = %g' % ( theta )
    exit ( 'R8_CSC - Fatal error!' )
  end

  value = 1.0 / value

  return value

