#!/usr/bin/env python

def lg_set ( g, lg1, lg2 ):

#*****************************************************************************80
#
## LG_SET sets the LG values for a given generator.
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
#    Input, integer G, the index of the generator.
#    1 <= G <= 32.
#
#    Input, integer LG1, LG2, the LG values for generator G.
#
  from lg_memory import lg_memory

  i = +1
  lg_memory ( i, g, lg1, lg2 )

  return

