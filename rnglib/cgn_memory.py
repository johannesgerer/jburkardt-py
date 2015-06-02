#!/usr/bin/env python

def cgn_memory ( i, g ):

#*****************************************************************************80
#
## CGN_MEMORY stores the current generator index.
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
#    -1, get the value.
#    0, initialize the value.
#    1, set the value.
#
#    Input/output, integer G.  For I = -1 or 0, an output quantity.
#    For I = +1, an input quantity.
#
  from sys import exit

  g_max = 32

  if ( i < 0 ):

    g = cgn_memory.g_save

  elif ( i == 0 ):

    cgn_memory.g_save = 1
    g = cgn_memory.g_save

  elif ( 0 < i ):

    if ( g < 1 or g_max < g ):
      print ''
      print 'CGN_MEMORY - Fatal error!'
      print '  Input generator index G is out of bounds.'
      exit ( 'CGN_MEMORY - Fatal error!' )

    cgn_memory.g_save = g


  return g

cgn_memory.g_save = 1

