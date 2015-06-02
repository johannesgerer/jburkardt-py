#!/usr/bin/env python
#
def square_grid_count ( ns ):

#*****************************************************************************80
#
## SQUARE_GRID_COUNT counts grid points in a quadrilateral.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    31 August 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer NS(2), the number of intervals along 
#    each dimension.
#
#    Output, integer NG, the number of grid points.
#
  ng = ( ns[0] + 1 ) * ( ns[1] + 1 )

  return ng

def square_grid_count_test ( ):

#*****************************************************************************80
#
## SQUARE_GRID_COUNT_TEST tests SQUARE_GRID_COUNT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 April 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ''
  print 'SQUARE_GRID_COUNT_TEST:'
  print '  SQUARE_GRID_COUNT can count the points in a grid'
  print '  over a quadrilateral with NS(I) grid points in the I-th direction.'

  ns = np.zeros ( 2 )

  print ''
  print '       NS              NG'
  print '  --------------'
  print ''

  for i in [ 1, 2, 4, 8 ]:
    ns[0] = i
    for j in [ 1, 2, 3, 5 ]:
      ns[1] = j
      ng = square_grid_count ( ns )
      print '  ( %4d, %4d ) %8d' % ( ns[0], ns[1], ng )

  print ''
  print 'SQUARE_GRID_COUNT_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  square_grid_count_test ( )
  timestamp ( )
