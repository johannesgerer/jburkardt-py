#!/usr/bin/env python

def r8_floor ( x ):

#*****************************************************************************80
#
## R8_FLOOR rounds an R8 down to the nearest integral R8.
#
#  Example:
#
#    X         Value
#
#   -1.1      -2.0
#   -1.0      -1.0
#   -0.9      -1.0
#   -0.1      -1.0
#    0.0       0.0
#    0.1       0.0
#    0.9       0.0
#    1.0       1.0
#    1.1       1.0
#    2.9       2.0
#    3.0       3.0
#    3.14159   3.0
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
#    Input, real X, the number to be rounded down.
#
#    Output, real VALUE, the rounded value of X.
#
  from math import floor

  value = floor ( x )

  return value

