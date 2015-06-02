#! /usr/bin/env python
#
def polygon_grid_count ( n, nv ):

#*****************************************************************************80
#
## POLYGON_GRID_COUNT counts the grid points inside a polygon.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 May 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of subintervals on a side.
#
#    Input, integer NV, the number of vertices.
#    3 <= NV.
#
#    Output, integer NG, the number of grid points.
#
  ng = 1 + nv * ( n * ( n + 1 ) ) / 2

  return ng

def polygon_grid_count_test ( ):

#*****************************************************************************80
#
## POLYGON_GRID_COUNT_TEST tests POLYGON_GRID_COUNT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 May 2015
#
#  Author:
#
#    John Burkardt
#
  print ''
  print 'POLYGON_GRID_COUNT_TEST:'
  print '  POLYGON_GRID_COUNT counts NG, the number of points in'
  print '  a grid defined with N+1 points on each side of a'
  print '  polygon of NV vertices.'

  for nv in range ( 3, 6 ):
    print ''
    print '  Polygonal vertex count NV = %d' % ( nv )
    print ''
    print '   N     NG'
    print ''
    for n in range ( 0, 6 ):
      ng = polygon_grid_count ( n, nv )
      print '  %2d  %5d' % ( n, ng )
#
#  Terminate.
#
  print ''
  print 'POLYGON_GRID_COUNT_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  polygon_grid_count_test ( )
  timestamp ( )
