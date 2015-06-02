#!/usr/bin/env python
#
def r8_asin ( x ):

#*****************************************************************************80
#
## R8_ASIN computes the arc sine function, with argument truncation.
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
#    Original FORTRAN77 version by Wayne Fullerton.
#    Python version by John Burkardt.
#
#  Parameters:
#
#    Input, real C, the argument.
#
#    Output, real VALUE, the arc-sine of C.
#
  from math import asin
 
  c2 = max ( c,  - 1.0 )
  c2 = min ( c2, +1.0 )
  
  value = asin ( c2 )

  return value
