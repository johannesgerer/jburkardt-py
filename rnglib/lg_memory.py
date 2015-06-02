#!/usr/bin/env python

def lg_memory ( i, g, lg1, lg2 ):

#*****************************************************************************80
#
## LG_MEMORY stores the LG values for all generators.
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
#    Input/output, integer LG1, LG2.  For I = -1,
#    these are output, for I = +1, these are input, for I = 0,
#    these arguments are ignored.  When used, the arguments are
#    old or new values of the LG parameter for generator G.
#
  from sys import exit

  g_max = 32

  if ( g < 1 or g_max < g ):
    print ''
    print 'LG_MEMORY - Fatal error!'
    print '  Input generator index G is out of bounds.'
    exit ( 'LG_MEMORY - Fatal error!' )

  if ( i < 0 ):
    lg1 = lg_memory.lg1_save[g-1]
    lg2 = lg_memory.lg2_save[g-1]
  elif ( i == 0 ):
    for j in range ( 1, g_max + 1 ):
      lg_memory.lg1_save[j-1] = 0
      lg_memory.lg2_save[j-1] = 0
    lg1 = 0
    lg2 = 0
  elif ( 0 < i ):
    lg_memory.lg1_save[g-1] = lg1
    lg_memory.lg2_save[g-1] = lg2

  return lg1, lg2

lg_memory.lg1_save = [ \
  0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0 ]
lg_memory.lg2_save = [ \
  0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0 ]

