#!/usr/bin/env python

def cgn_set ( g ):

#*****************************************************************************80
#
## CGN_SET sets the current generator index.
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
#    Input, integer G, the current generator index.
#    1 <= G <= 32.
#
  from cgn_memory import cgn_memory

  i = +1
  g = cgn_memory ( i, g )

  return

