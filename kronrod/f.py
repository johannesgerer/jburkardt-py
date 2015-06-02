#!/usr/bin/env python

def f ( x ):

#*****************************************************************************80
#
## F is a function whose integral from -1 to +1 is to be estimated.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    30 April 2013
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, double X, the argument.
#
#    Output, double F, the value.
#
  value = 1.0 / ( x * x + 1.005 )

  return value


