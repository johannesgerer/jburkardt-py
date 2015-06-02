#!/usr/bin/env python

def cg_memory ( i, g, cg1, cg2 ):

#*****************************************************************************80
#
## CG_MEMORY stores the CG values for all generators.
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
#    Input, integer G, for I = -1 or +1, the index of
#    the generator, with 1 <= G <= 32.
#
#    Input/output, integer CG1, CG2.  For I = -1,
#    these are output, for I = +1, these are input, for I = 0,
#    these arguments are ignored.  When used, the arguments are
#    old or new values of the CG parameter for generator G.
#
  from sys import exit

  g_max = 32

  if ( g < 1 or g_max < g ):
    print ''
    print 'CG_MEMORY - Fatal error!'
    print '  Input generator index G is out of bounds.'
    exit ( 'CG_MEMORY - Fatal error!' )

  if ( i < 0 ):
    cg1 = cg_memory.cg1_save[g-1]
    cg2 = cg_memory.cg2_save[g-1]
  elif ( i == 0 ):
    for i in range ( 1, g_max + 1 ):
      cg_memory.cg1_save[i-1] = 0
      cg_memory.cg2_save[i-1] = 0
    cg1 = 0
    cg2 = 0
  elif ( 0 < i ):
    cg_memory.cg1_save[g-1] = cg1
    cg_memory.cg2_save[g-1] = cg2

  return cg1, cg2

cg_memory.cg1_save = [ \
  0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0 ]
cg_memory.cg2_save = [ \
  0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0 ]

