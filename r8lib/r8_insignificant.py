#!/usr/bin/env python

def r8_insignificant ( r, s ):

#*****************************************************************************80
#
## R8_INSIGNIFICANT determines if an R8 is insignificant.
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
#    Input, real R, the number to be compared against.
#
#    Input, real S, the number to be compared.
#
#    Output, logical R8_INSIGNIFICANT, is TRUE if S is insignificant
#    compared to R.
#
  value = True
  r8_epsilon = 2.220446049250313E-016

  t = r + s
  tol = r8_epsilon * abs ( r )

  if ( tol < abs ( r - t ) ):
    value = False
  
  return

