#!/usr/bin/env python

def r8_sign_char ( r8 ):

#*****************************************************************************80
#
## R8_SIGN_CHAR returns the sign of an R8 as a character.
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
#    Input, real R8, the value whose sign is of interest.
#
#    Output, character C, is '-', '0', or '+'.

  if ( r8 < 0.0 ):
    c = '-'
  elif ( r8 == 0.0 ):
    c = '0'
  else:
    c = '+'

  return c
