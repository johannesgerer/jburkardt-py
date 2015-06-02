#! /usr/bin/env python
#
def simplex_grid_index_sample ( m, n, ng, seed ):

#*****************************************************************************80
#
## SIMPLEX_GRID_INDEX_SAMPLE returns a random simplex grid index.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 April 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, the spatial dimension.
#
#    Input, integer N, the number of subintervals in each dimension.
#
#    Input, ingeger L, the number of indices to return.
#
#    Input, integer SEED, a seed for the random number generator.
#
#    Output, integer G(NG,M+1), randomly selected indices in the simplex grid.
#
#    Output, integer SEED, the updated random number seed.
#
  import numpy as np
  from comp_random import comp_random

  g = np.zeros ( ( ng, m + 1 ) )

  for i in range ( 0, ng ):
    grow, seed = comp_random ( n, m + 1, seed )
    for j in range ( 0, m + 1 ):
      g[i,j] = grow[j]

  return g, seed

def simplex_grid_index_sample_test ( ):

#*****************************************************************************80
#
## SIMPLEX_GRID_INDEX_SAMPLE_TEST tests SIMPLEX_GRID_INDEX_SAMPLE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 April 2015
#
#  Author:
#
#    John Burkardt
#
  print ''
  print 'SIMPLEX_GRID_INDEX_SAMPLE_TEST:'
  print '  SIMPLEX_GRID_INDEX_SAMPLE returns a randomly selected'
  print '  index of a simplex grid that uses N+1 points on a side,'
  print '  in an M-dimensional simplex.'
  print ''
  print '   #:  1  2  3  (*)'
  print ''

  m = 3
  n = 3
  ng = 20
  seed = 123456789

  g, seed = simplex_grid_index_sample ( m, n, ng, seed )

  for i in range ( 0, ng ):
    print '  %2d:' % ( i ),
    for j in range ( 0, m ):
      print ' %2d' % ( g[i,j] ),
    print ' (%2d)' % ( g[i,m] )
#
#  Terminate.
#
  print ''
  print 'SIMPLEX_GRID_INDEX_SAMPLE_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  simplex_grid_index_sample_test ( )
  timestamp ( )
