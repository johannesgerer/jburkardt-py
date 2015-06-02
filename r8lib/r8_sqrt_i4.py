#!/usr/bin/env python

def r8_sqrt_i4 ( i ):

#*****************************************************************************80
#
## R8_SQRT_I4 returns the square root of an I4 as an R8.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    25 July 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer I, the number whose square root is desired.
#
#    Output, real R8_SQRT_I4, the value of sqrt(I).
#
  from math import sqrt

  value = sqrt ( float ( i ) )

  return value

