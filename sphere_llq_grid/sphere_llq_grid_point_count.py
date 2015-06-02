#! /usr/bin/env python
#
def sphere_llq_grid_point_count ( lat_num, long_num ):

#*****************************************************************************80
#
## SPHERE_LLQ_GRID_POINT_COUNT counts points for a SPHERE LLQ grid.
#
#  Discussion:
#
#    A SPHERE LLQ grid imposes a grid of quadrilaterals on a sphere,
#    using latitude and longitude lines.
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
#    Input, integer LAT_NUM, LONG_NUM, the number of latitude 
#    and longitude lines to draw.  The latitudes do not include the North and 
#    South poles, which will be included automatically, so LAT_NUM = 5, for 
#    instance, will result in points along 7 lines of latitude.
#
#    Output, integer POINT_NUM, the number of grid points.
#
  point_num = 2 + lat_num * long_num;

  return point_num

def sphere_llq_grid_point_count_test ( ):

#*****************************************************************************80
#
## SPHERE_LLQ_GRID_POINT_COUNT_TEST tests SPHERE_LLQ_GRID_POINT_COUNT.
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
  lat_num = 3
  long_num = 4

  print ''
  print 'SPHERE_LLQ_GRID_POINT_COUNT_TEST'
  print '  SPHERE_LLQ_GRID_POINT_COUNT counts the points used for a'
  print '  grid based on quadrilaterals defined by latitude and longitude'
  print '  lines on a sphere in 3D.'
  print ''
  print '     LAT_NUM    LONG_NUM   POINT_NUM'

  for lat_num in range ( 1, 19, 2 ):
    print ''
    long_num = 1
    for long_log in range ( 1, 5 ):
      long_num = long_num * 2
      point_num = sphere_llq_grid_point_count ( lat_num, long_num )
      print '  %8d  %8d  %8d' % ( lat_num, long_num, point_num )
#
#  Terminate.
#
  print ''
  print 'SPHERE_LLQ_GRID_POINT_COUNT_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  sphere_llq_grid_point_count_test ( )
  timestamp ( )

