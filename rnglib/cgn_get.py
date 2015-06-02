#!/usr/bin/env python

def cgn_get ( ):

#*****************************************************************************80
#
## CGN_GET gets the current generator index.
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
#    Output, integer G, the current generator index.
#
  from cgn_memory import cgn_memory

  i = -1
  g = []
  g = cgn_memory ( i, g )

  return g

