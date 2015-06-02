#!/usr/bin/env python

def r8_sign_match_strict ( r1, r2 ):

#*****************************************************************************80
#
## R8_SIGN_MATCH_STRICT is TRUE if two R8's are of the same strict sign.
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
#    Input, real R1, R2, the values to check.
#
#    Output, logical VALUE, is TRUE if the signs match.
#
  value = ( r1 <  0.0 and r2 <  0.0 ) or \
          ( r1 == 0.0 and r2 == 0.0 ) or \
          ( 0.0 <  r1 and 0.0 <  r2 )

  return value

