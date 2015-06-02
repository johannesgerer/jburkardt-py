#! /usr/bin/env python

def sphere_llt_grid_lines ( nlat, nlong, line_num ):

#*****************************************************************************80
#
## SPHERE_LLT_GRID_LINES returns lines for an LLT grid on a sphere.
#
#  Discussion:
#
#    A SPHERE LLT grid imposes a grid of triangles on a sphere,
#    using latitude and longitude lines.
#
#    The point numbering system is the same used in SPHERE_LLT_GRID_POINTS,
#    and that routine may be used to compute the coordinates of the points.
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
#    Input, integer NLAT, NLONG, the number of latitude and longitude
#    lines to draw.  The latitudes do not include the North and South
#    poles, which will be included automatically, so NLAT = 5, for instance,
#    will result in points along 7 lines of latitude.
#
#    Input, integer LINE_NUM, the number of grid lines.
#
#    Output, integer LINE(LINE_NUM,2), contains pairs of point indices for
#    line segments that make up the grid.
#
  import numpy as np

  l = 0
  line = np.zeros ( [ line_num, 2 ] )
#
#  "Vertical" lines.
#
  for j in range ( 0, nlong ):

    old = 0
    new = j + 1
    line[l,0] = old
    line[l,1] = new
    l = l + 1

    for i in range ( 0, nlat - 1 ):

      old = new
      new = old + nlong
      line[l,0] = old
      line[l,1] = new
      l = l + 1

    old = new
    line[l,0] = old
    line[l,1] = 1 + nlat * nlong
    l = l + 1
#
#  "Horizontal" lines.
#
  for i in range ( 0, nlat ):

    new = 1 + i * nlong

    for j in range ( 0, nlong - 1 ):
      old = new
      new = old + 1
      line[l,0] = old
      line[l,1] = new
      l = l + 1

    old = new
    new = 1 + i * nlong
    line[l,0] = old
    line[l,1] = new
    l = l + 1
#
#  "Diagonal" lines.
#
  for j in range ( 0, nlong ):

    old = 0
    next = j + 1
    newcol = j

    for i in range ( 1, nlat ):

      old = next
      next = old + nlong + 1
      newcol = newcol + 1

      if ( nlong - 1 < newcol ):
        newcol = 0
        next = next - nlong

      line[l,0] = old
      line[l,1] = next
      l = l + 1

  return line

def sphere_llt_grid_lines_test ( ):

#*****************************************************************************80
#
## SPHERE_LLT_GRID_LINES_TEST tests SPHERE_LLT_GRID_LINES.
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
  from i4mat_print import i4mat_print
  from sphere_llt_grid_line_count import sphere_llt_grid_line_count

  lat_num = 3
  long_num = 4

  print ''
  print 'SPHERE_LLT_GRID_LINES_TEST'
  print '  SPHERE_LLT_GRID_LINES computes grid lines'
  print '  on a sphere in 3D.'
  print ''
  print '  Number of latitudes is  %d' % ( lat_num )
  print '  Number of longitudes is %d' % ( long_num )

  line_num = sphere_llt_grid_line_count ( lat_num, long_num )

  print ''
  print '  Number of line segments is %d' % ( line_num )

  line = sphere_llt_grid_lines ( lat_num, long_num, line_num )

  i4mat_print ( line_num, 2, line, '  Grid line vertices:' )
#
#  Terminate.
#
  print ''
  print 'SPHERE_LLT_GRID_LINES_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  sphere_llt_grid_lines_test ( )
  timestamp ( )

