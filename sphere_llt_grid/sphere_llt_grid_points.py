#! /usr/bin/env python
#
def sphere_llt_grid_points ( r, pc, lat_num, long_num, point_num ):

#*****************************************************************************80
#
## SPHERE_LLT_GRID_POINTS produces points on an LLT grid on a sphere.
#
#  Discussion:
#
#    A SPHERE LLT grid imposes a grid of triangles on a sphere,
#    using latitude and longitude lines.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    21 May 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real R, the radius of the sphere.
#
#    Input, real PC(1,3), the center of the sphere.
#
#    Input, integer LAT_NUM, LONG_NUM, the number of latitude and longitude
#    lines to draw.  The latitudes do not include the North and South
#    poles, which will be included automatically, so LAT_NUM = 5, for instance,
#    will result in points along 7 lines of latitude.
#
#    Input, integer POINT_NUM, the number of grid points.
#
#    Output, real P(POINT_NUM,3), the grid points.
#
  import numpy as np

  n = 0
  p = np.zeros ( [ point_num, 3 ] )
#
#  The north pole.
#
  theta = 0.0
  phi = 0.0
  p[n,0] = pc[0] + r * np.sin ( phi ) * np.cos ( theta )
  p[n,1] = pc[1] + r * np.sin ( phi ) * np.sin ( theta )
  p[n,2] = pc[2] + r * np.cos ( phi )
  n = n + 1
#
#  Do each intermediate ring of latitude.
#
  for lat in range ( 1, lat_num + 1 ):

    phi = np.pi * float ( lat ) / float ( lat_num + 1 )
#
#  Along that ring of latitude, compute points at various longitudes.
#
    for lon in range ( 0, long_num ):

      theta = 2.0 * np.pi * float ( lon ) / float ( long_num );

      p[n,0] = pc[0] + r * np.sin ( phi ) * np.cos ( theta )
      p[n,1] = pc[1] + r * np.sin ( phi ) * np.sin ( theta )
      p[n,2] = pc[2] + r * np.cos ( phi )
      n = n + 1;
#
#  The south pole.
#
  theta = 0.0
  phi = np.pi
  p[n,0] = pc[0] + r * np.sin ( phi ) * np.cos ( theta )
  p[n,1] = pc[1] + r * np.sin ( phi ) * np.sin ( theta )
  p[n,2] = pc[2] + r * np.cos ( phi )
  n = n + 1

  return p

def sphere_llt_grid_points_test ( ):

#*****************************************************************************80
#
## SPHERE_LLT_GRID_POINTS_TEST tests SPHERE_LLT_GRID_POINTS.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    21 May 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  from r8vec_print import r8vec_print
  from sphere_llt_grid_point_count import sphere_llt_grid_point_count

  lat_num = 3
  long_num = 4

  pc = np.array ( [ 0.0, 0.0, 0.0 ] )
  r = 10.0

  print ''
  print 'SPHERE_LLT_GRID_POINTS_TEST'
  print '  SPHERE_LLT_POINTS produces latitude/longitude'
  print '  points on a sphere in 3D.'

  print ''
  print '  Radius = %g' % ( r )

  r8vec_print ( 3, pc, '  Center:' )

  print ''
  print '  The number of latitudes =  %d' % ( lat_num )
  print '  The number of longitudes = %d' % ( long_num )

  node_num = sphere_llt_grid_point_count ( lat_num, long_num )

  print ''
  print '  The number of grid points is %d' % ( node_num )

  node_xyz = sphere_llt_grid_points ( r, pc, lat_num, long_num, node_num )

  print ''

  k = 0
  print '  %8d' % ( k ),
  for i in range ( 0, 3 ):
    print '  %12f' % ( node_xyz[k,i] ),

  print ''

  for lat in range ( 0, lat_num ):
    print ''
    for lon in range ( 0, long_num ):
      k = k + 1
      print '  %8d' % ( k ),
      for i in range ( 0, 3 ):
        print '  %12f' % ( node_xyz[k,i] ),
      print ''

  print ''

  k = k + 1
  print '  %8d' % ( k ),
  for i in range ( 0, 3 ):
    print '  %12f' % ( node_xyz[k,i] ),
  print ''
#
#  Terminate.
#
  print ''
  print 'SPHERE_LLT_GRID_POINTS_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  sphere_llt_grid_points_test ( )
  timestamp ( )

