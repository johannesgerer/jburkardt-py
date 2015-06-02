#!/usr/bin/env python

def antithetic_memory ( i, value ):

#*****************************************************************************80
#
## ANTITHETIC_MEMORY stores the antithetic value for all generators.
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
#    Input, integer I, the desired action.
#    -1, get a value.
#    0, initialize all values.
#    1, set a value.
#
#    Input/output, bool VALUE.  For I = -1, VALUE is an output
#    quantity, for I = +1, VALUE is an input quantity.
#
  from cgn_get import cgn_get

  g_max = 32

  if ( i < 0 ):
    g = cgn_get ( )
    value = antithetic_memory.a_save[g-1]
  elif ( i == 0 ):
    antithetic_memory.a_save = [];
    for i in range ( 1, g_max + 1 ):
      antithetic_memory.a_save.append ( False )
    value = false
  elif ( 0 < i ):
    g = cgn_get ( )
    antithetic_memory.a_save[g-1] = value

  return value

antithetic_memory.a_save = [ \
  False, False, False, False, False, False, False, False, \
  False, False, False, False, False, False, False, False, \
  False, False, False, False, False, False, False, False, \
  False, False, False, False, False, False, False, False ];

