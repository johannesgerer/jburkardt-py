#! /usr/bin/env python
#
def polygon_grid_points ( n, nv, v, ng ):

#*****************************************************************************80
#
## POLYGON_GRID_POINTS computes points on a polygonal grid.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 May 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of subintervals.
#
#    Input, integer NV, the number of vertices in the polygon.
#
#    Input, real V[NV,2], the coordinates of the vertices.
#
#    Input, integer NG, the number of grid points.
#
#    Output, real XG[NG,2], the coordinates of the grid points.
#
  import numpy as np

  xg = np.zeros ( [ ng, 2 ] )
  p = 0
#
#  Determine the centroid.
#
  vc = np.zeros ( 2 )
  for i in range ( 0, nv ):
    vc[0] = vc[0] + v[i,0]
    vc[1] = vc[1] + v[i,1]
  vc[0] = vc[0] / float ( nv )
  vc[1] = vc[1] / float ( nv )
#
#  Use the centroid as the first grid point.
#
  xg[p,0] = vc[0]
  xg[p,1] = vc[1]
  p = p + 1
#
#  Consider each triangle formed by two consecutive vertices and the centroid,
#  but skip the first line of points.
#
  for l in range ( 0, nv ):
    lp1 = ( l % nv )
    for i in range ( 1, n + 1 ):
      for j in range ( 0, n - i + 1 ):
        k = n - i - j
        xg[p,0] = ( float ( i ) * v[l,0] \
                  + float ( j ) * v[lp1,0] \
                  + float ( k ) * vc[0] ) \
                  / float ( n )
        xg[p,1] = ( float ( i ) * v[l,1] \
                  + float ( j ) * v[lp1,1] \
                  + float ( k ) * vc[1] ) \
                  / float ( n )
        p = p + 1

  return xg

def polygon_grid_points_test01 ( ):

#*****************************************************************************80
#
## POLYGON_GRID_POINTS_TEST01 tests POLYGON_GRID_POINTS
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 May 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  from polygon_grid_count import polygon_grid_count
  from polygon_grid_display import polygon_grid_display
  from r8mat_print import r8mat_print
  from r8mat_write import r8mat_write

  print ''
  print 'POLYGON_GRID_POINTS_TEST01:'
  print '  POLYGON_GRID_POINTS returns grid points for a polygon'
  print '  of NV vertices, with N+1 points on a side'
  print ''
  print '  For this test, the polygon is a triangle.'
#
#  Define the polygon.
#
  nv = 3
  v = np.array ( [ \
    [ 0.0, 0.0 ], \
    [ 1.0, 0.0 ], \
    [ 0.5, 0.86602540378443860 ] ] )

  r8mat_print ( nv, 2, v, '  Polygon vertices:' )
#
#  Count the grid points.
#
  n = 5
  ng = polygon_grid_count ( n, nv )

  print ''
  print '  N = %d' % ( n )
  print '  Number of grid points will be NG = %d' % ( ng )
#
#  Compute the grid points.
#
  xg = polygon_grid_points ( n, nv, v, ng )

  r8mat_print ( ng, 2, xg, '  The grid point array:' )
#
#  Display the points.
#
  filename = 'triangle.png'

  polygon_grid_display ( n, nv, v, ng, xg, filename )
#
#  Write the points to a file.
#
  filename = 'triangle.xy'

  r8mat_write ( filename, ng, 2, xg )

  print ''
  print '  Data written to the file "%s"' % ( filename )
#
#  Terminate.
#
  print ''
  print 'POLYGON_GRID_POINTS_TEST01:'
  print '  Normal end of execution.'

  return

def polygon_grid_points_test02 ( ):

#*****************************************************************************80
#
## POLYGON_GRID_POINTS_TEST02 tests POLYGON_GRID_POINTS
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 May 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  from polygon_grid_count import polygon_grid_count
  from polygon_grid_display import polygon_grid_display
  from r8mat_print import r8mat_print
  from r8mat_write import r8mat_write

  print ''
  print 'POLYGON_GRID_POINTS_TEST02:'
  print '  POLYGON_GRID_POINTS returns grid points for a polygon'
  print '  of NV vertices, with N+1 points on a side'
  print ''
  print '  For this test, the polygon is a convex quadrilateral'
  print '  with sides of varying length.'
#
#  Define the polygon.
#
  nv = 4
  v = np.array ( [ \
    [ 1.0, 1.0 ], \
    [ 2.0, 0.0 ], \
    [ 4.0, 3.0 ], \
    [ 0.0, 5.0 ] ] )

  r8mat_print ( nv, 2, v, '  Polygon vertices:' )
#
#  Count the grid points.
#
  n = 7
  ng = polygon_grid_count ( n, nv )

  print ''
  print '  N = %d' % ( n )
  print '  Number of grid points will be NG = %d' % ( ng )
#
#  Compute the grid points.
#
  xg = polygon_grid_points ( n, nv, v, ng )

  r8mat_print ( ng, 2, xg, '  The grid point array:' )
#
#  Display the points.
#
  filename = 'quad.png'

  polygon_grid_display ( n, nv, v, ng, xg, filename )
#
#  Write the points to a file.
#
  filename = 'quad.xy'

  r8mat_write ( filename, ng, 2, xg )

  print ''
  print '  Data written to the file "%s"' % ( filename )
#
#  Terminate.
#
  print ''
  print 'POLYGON_GRID_POINTS_TEST02:'
  print '  Normal end of execution.'

  return

def polygon_grid_points_test03 ( ):

#*****************************************************************************80
#
## POLYGON_GRID_POINTS_TEST03 tests POLYGON_GRID_POINTS
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 May 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  from polygon_grid_count import polygon_grid_count
  from polygon_grid_display import polygon_grid_display
  from r8mat_print import r8mat_print
  from r8mat_write import r8mat_write

  print ''
  print 'POLYGON_GRID_POINTS_TEST03:'
  print '  POLYGON_GRID_POINTS returns grid points for a polygon'
  print '  of NV vertices, with N+1 points on a side'
  print ''
  print '  For this test, the polygon is nonconvex and six sided.'
  print '  Two degenerate triangles are created, and some grid points'
  print '  are generated several times.'
#
#  Define the polygon.
#
  nv = 6
  v = np.array ( [ \
    [ 0.0, 0.0 ], \
    [ 2.0, 0.0 ], \
    [ 2.0, 1.0 ], \
    [ 1.0, 1.0 ], \
    [ 1.0, 2.0 ], \
    [ 0.0, 2.0 ] ] )

  r8mat_print ( nv, 2, v, '  Polygon vertices:' )
#
#  Count the grid points.
#
  n = 5
  ng = polygon_grid_count ( n, nv )

  print ''
  print '  N = %d' % ( n )
  print '  Number of grid points will be NG = %d' % ( ng )
#
#  Compute the grid points.
#
  xg = polygon_grid_points ( n, nv, v, ng )

  r8mat_print ( ng, 2, xg, '  The grid point array:' )
#
#  Display the points.
#
  filename = 'ell.png'

  polygon_grid_display ( n, nv, v, ng, xg, filename )
#
#  Write the points to a file.
#
  filename = 'ell.xy'

  r8mat_write ( filename, ng, 2, xg )

  print ''
  print '  Data written to the file "%s"' % ( filename )
#
#  Terminate.
#
  print ''
  print 'POLYGON_GRID_POINTS_TEST03:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  polygon_grid_points_test01 ( )
  polygon_grid_points_test02 ( )
  polygon_grid_points_test03 ( )
  timestamp ( )
