#! /usr/bin/env python
#
def simplex_grid_index_next ( m, n, g ):

#*****************************************************************************80
#
## SIMPLEX_GRID_INDEX_NEXT returns the next simplex grid index.
#
#  Discussion:
#
#    The vector G has dimension M+1.  The first M entries may be regarded
#    as grid coordinates.  These coordinates must have a sum between 0 and N.
#    The M+1 entry contains the remainder, that is N minus the sum of the
#    first M coordinates.
#
#    Each time the function is called, it is given a current grid index, and
#    computes the next one.  The very first index is all zero except for a 
#    final value of N, and the very last index has all zero except for an'
#    intial value of N.
#
#    For example, here are the coordinates in order for M = 3, N = 3:
#
#     0  0 0 0 3
#     1  0 0 1 2
#     2  0 0 2 1
#     3  0 0 3 0
#     4  0 1 0 2
#     5  0 1 1 1
#     6  0 1 2 0
#     7  0 2 0 1
#     8  0 2 1 0
#     9  0 3 0 0
#    10  1 0 0 2
#    11  1 0 1 1
#    12  1 0 2 0
#    13  1 1 0 1
#    14  1 1 1 0
#    15  1 2 0 0
#    16  2 0 0 1
#    17  2 0 1 0
#    18  2 1 0 0
#    19  3 0 0 0
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    21 April 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, the spatial dimension.
#
#    Input, integer N, the number of subintervals.
#
#    Input/output, integer G(M+1), the current, and then the next, grid index.
#
  from comp_next_grlex import comp_next_grlex

  g = comp_next_grlex ( m + 1, g )

  return g

def simplex_grid_index_next_test ( ):

#*****************************************************************************80
#
## SIMPLEX_GRID_INDEX_NEXT_TEST tests SIMPLEX_GRID_INDEX_NEXT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    21 April 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ''
  print 'SIMPLEX_GRID_INDEX_NEXT_TEST:'
  print '  SIMPLEX_GRID_INDEX_NEXT lists, one by one, the indices'
  print '  of a simplex grid that uses N+1 points on a side,'
  print '  in an M-dimensional simplex.'
  print ''
  print '   #:  1  2  3  (*)'
  print ''

  m = 3
  n = 3

  j = 0
  g = np.zeros ( m + 1 )
  g[m] = n
  
  while ( True ):

    print '  %2d:' % ( j ),
    for i in range ( 0, m ):
      print ' %2d' % ( g[i] ),
    print ' (%2d)' % ( g[m] )

    if ( g[0] == n ):
      break

    g = simplex_grid_index_next ( m, n, g )

    j = j + 1
#
#  Terminate.
#
  print ''
  print 'SIMPLEX_GRID_INDEX_NEXT_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  simplex_grid_index_next_test ( )
  timestamp ( )
