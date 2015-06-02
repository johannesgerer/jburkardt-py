#!/usr/bin/env python
#
def r8_aint ( x ):

#****************************************************************************80
#
## R8_AINT truncates an R8 argument to an integer.
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
#    John Burkardt.
#
#  Parameters:
#
#    Input, real X, the argument.
#
#    Output, real VALUE, the truncated version of X.
#
  from math import abs
  from math import floor

  if ( x < 0.0 ):
    value = - floor ( abs ( x ) )
  else:
    value =   floor ( abs ( x ) )

  return value

