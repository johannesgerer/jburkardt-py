#! /usr/bin/env python
#
def sphere_llq_grid_display ( r, pc, lat_num, long_num, node_num, node_xyz, \
    line_num, line_data, filename ):

#*****************************************************************************80
#
## SPHERE_LLQ_GRID_DISPLAY displays points and lines of an LLQ grid on a sphere.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    18 May 2015
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
#    Input, integer NODE_NUM, the number of grid points.
#
#    Input, real NODE_XYZ(NODE_NUM,3), the grid points.
#
#    Input, integer LINE_NUM, the number of grid lines.
#
#    Input, integer LINE_DATA(LINE_NUM,2), contains pairs of point indices for
#    line segments that make up the grid.
#
#    Input, string FILENAME, the name of a file in which to store a copy 
#    of the plot.
#
  import matplotlib.pyplot as plt
  import numpy as np
  from mpl_toolkits.mplot3d import Axes3D

  fig = plt.figure ( )
  ax = fig.add_subplot ( 111, projection = '3d' )
#
#  Draw the grid points.
#
  ax.scatter ( node_xyz[:,0], node_xyz[:,1], node_xyz[:,2], 'b' )

  for i in range ( 0, line_num ):
    i1 = line_data[i,0]
    i2 = line_data[i,1]
    ax.plot ( [ node_xyz[i1,0], node_xyz[i2,0] ], 
              [ node_xyz[i1,1], node_xyz[i2,1] ],
              [ node_xyz[i1,2], node_xyz[i2,2] ], 'r' )

  ax.set_xlabel ( '<---X--->' )
  ax.set_ylabel ( '<---Y--->' )
  ax.set_zlabel ( '<---Z--->' )
  ax.set_title ( 'LLQ grid on sphere' )
  ax.grid ( True )
  ax.axis ( 'equal' )

# plt.show ( )
  plt.savefig ( filename )

  plt.clf ( )

  return

def sphere_llq_grid_display_test ( ):

#*****************************************************************************80
#
## SPHERE_LLQ_GRID_DISPLAY_TEST tests SPHERE_LLQ_GRID_DISPLAY.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    18 May 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  from sphere_llq_grid_point_count import sphere_llq_grid_point_count
  from sphere_llq_grid_points import sphere_llq_grid_points
  from sphere_llq_grid_line_count import sphere_llq_grid_line_count
  from sphere_llq_grid_lines import sphere_llq_grid_lines

  lat_num = 10
  long_num = 12
  pc = np.array ( [ 0.0, 0.0, 0.0 ] )
  r = 10.0

  print ''
  print 'SPHERE_LLQ_GRID_DISPLAY_TEST'
  print '  SPHERE_LLQ_GRID_DISPLAY displays an LLQ grid on a sphere.'
  print ''
  print '  Number of latitudes is  %d' % ( lat_num )
  print '  Number of longitudes is %d' % ( long_num )
#
#  Get points.
#
  node_num = sphere_llq_grid_point_count ( lat_num, long_num )

  print ''
  print '  The number of grid points is %d' % ( node_num )

  node_xyz = sphere_llq_grid_points ( r, pc, lat_num, long_num, node_num )
#
#  Get lines.
#
  line_num = sphere_llq_grid_line_count ( lat_num, long_num )

  print ''
  print '  Number of line segments is %d' % ( line_num )

  line_data = sphere_llq_grid_lines ( lat_num, long_num, line_num )

  filename = 'sphere_llq_grid.png'

  sphere_llq_grid_display ( r, pc, lat_num, long_num, node_num, node_xyz, \
    line_num, line_data, filename )
#
#  Terminate.
#
  print ''
  print 'SPHERE_LLQ_GRID_DISPLAY_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  sphere_llq_grid_display_test ( )
  timestamp ( )
