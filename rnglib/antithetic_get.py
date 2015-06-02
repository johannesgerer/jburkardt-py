#!/usr/bin/env python

def antithetic_get ( ):

#*****************************************************************************80
#
## ANTITHETIC_GET queries the antithetic value for a given generator.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 May 2013
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, bool VALUE, is TRUE if generator G is antithetic.
#
  from antithetic_memory import antithetic_memory

  i = -1
  value = []
  value = antithetic_memory ( i, value )

  return value

