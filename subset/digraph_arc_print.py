#! /usr/bin/env python

def digraph_arc_print ( nedge, inode, jnode, title ):

#*****************************************************************************80
#
## DIGRAPH_ARC_PRINT prints out a digraph from an edge list.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    29 May 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer NEDGE, the number of edges.
#
#    Input, integer INODE(NEDGE), JNODE(NEDGE), the beginning and end
#    nodes of the edges.
#
#    Input, character ( len = * ) TITLE, a title.
#
  if ( 0 < len ( title ) ):
    print ''
    print title

  print ''

  for i in range ( 0,  nedge ):
    print '  %4d    %4d  %4d' % ( i, inode[i], jnode[i] )

  return

def digraph_arc_print_test ( ):

#*****************************************************************************80
#
## DIGRAPH_ARC_PRINT_TEST calls DIGRAPH_ARC_PRINT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    29 May 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  nedge = 7
  nnode = 5

  inode = np.array ( [ 2, 1, 2, 1, 3, 5, 4 ] )
  jnode = np.array ( [ 5, 4, 3, 2, 1, 1, 2 ] )

  print ''
  print 'DIGRAPH_ARC_PRINT_TEST'
  print '  DIGRAPH_ARC_PRINT prints a digraph.'

  digraph_arc_print ( nedge, inode, jnode, '  The arc list of the digraph:' );
#
#  Terminate.
#
  print ''
  print 'DIGRAPH_ARC_PRINT_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  digraph_arc_print_test ( )
  timestamp ( )

