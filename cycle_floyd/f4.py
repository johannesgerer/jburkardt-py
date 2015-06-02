#!/usr/bin/env python

def f4 ( i ) :

#*****************************************************************************80
#
## F4 is the iteration function for example 4.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 May 2013
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer I, the argument of the function.
#
#    Output, integer VALUE, the value of the function.
#
  value = ( ( 31421 * i + 6927 ) % 65536 );

  return value

