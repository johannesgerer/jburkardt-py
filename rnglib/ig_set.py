#!/usr/bin/env python

def ig_set ( g, ig1, ig2 ):

#*****************************************************************************80
#
## IG_SET sets the IG values for a given generator.
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
#    Input, integer IG1, IG2, the IG values for generator G.
#
  from ig_memory import ig_memory

  i = +1
  [ ig1, ig2 ] = ig_memory ( i, g, ig1, ig2 )

  return
