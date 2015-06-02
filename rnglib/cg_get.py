#!/usr/bin/env python

def cg_get ( g ):

#*****************************************************************************80
#
## CG_GET queries the CG values for a given generator.
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
#    Output, integer CG1, CG2, the CG values for generator G.
#
  from cg_memory import cg_memory

  i = -1
  cg1 = []
  cg2 = []
  [ cg1, cg2 ] = cg_memory ( i, g, cg1, cg2 )

  return cg1, cg2

