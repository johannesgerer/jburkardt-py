#!/usr/bin/env python

def initialized_memory ( i, initialized ):

#*****************************************************************************80
#
## INITIALIZED_MEMORY stores the INITIALIZED value.
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
#    Input/output, bool INITIALIZED.  For I = -1, an output quantity, 
#    if I = +1, an input quantity, and if I = 0 the value is ignored.
#
  if ( i < 0 ):
    initialized = initialized_memory.initialized_save
  elif ( i == 0 ):
    initialized_memory.initialized_save = False
    initialized = False
  elif ( 0 < i ):
    initialized_memory.initialized_save = initialized

  return initialized

initialized_memory.initialized_save = False

