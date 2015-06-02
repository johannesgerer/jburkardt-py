#!/usr/bin/env python
#
def triangle_grid_count ( n ):

#*****************************************************************************80
#
## TRIANGLE_GRID_COUNT counts the grid points inside a triangle.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 April 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of subintervals.
#
#    Output, integer NG, the number of grid points inside the triangle.
#
  ng = ( ( n + 1 ) * ( n + 2 ) ) / 2;

  return ng

def triangle_grid_count_test ( ):

#*****************************************************************************80
#
## TRIANGLE_GRID_COUNT_TEST tests TRIANGLE_GRID_COUNT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 April 2015
#
#  Author:
#
#    John Burkardt
#
  print ''
  print 'TRIANGLE_GRID_COUNT_TEST:'
  print '  TRIANGLE_GRID_COUNT can count the points in a triangular grid'
  print '  with N+1 points on a side, based on any triangle.'

  print ''
  print '     N        NG'
  print ''

  for n in [ 1, 2, 3, 4, 5, 10, 15, 20, 25, 50, 100 ]:
    ng = triangle_grid_count ( n )
    print '  %4d  %8d' % ( n, ng )

  print ''
  print 'TRIANGLE_GRID_COUNT_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  triangle_grid_count_test ( )
  timestamp ( )
