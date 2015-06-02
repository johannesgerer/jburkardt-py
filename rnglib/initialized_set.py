#!/usr/bin/env python

def initialized_set ( ):

#*****************************************************************************80
#
## INITIALIZED_SET sets the INITIALIZED value to true.
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
#    None.
#
  from initialized_memory import initialized_memory

  i = +1
  initialized = True
  initialized = initialized_memory ( i, initialized )

