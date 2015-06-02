#!/usr/bin/env python

def r8_in_01 ( x ):

#*****************************************************************************80
#
## R8_IN_01 is TRUE if the value is in the range [0,1].
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    01 June 2013
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real X, the value.
#
#    Output, boolean VALUE, is TRUE if 0 <= X <= 1.
#
  value = ( 0.0 <= x and x <= 1.0 )

  return value

