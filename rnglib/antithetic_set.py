#!/usr/bin/env python

def antithetic_set ( value ):

#*****************************************************************************80
#
## ANTITHETIC_SET sets the antithetic value for a given generator.
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
#    Input, bool VALUE, is TRUE if the current generator is to be antithetic.
#
  from antithetic_memory import antithetic_memory

  i = +1
  value = antithetic_memory ( i, value )

  return

