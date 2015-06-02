#! /usr/bin/env python
#
def circle_arc_grid_points ( r, c, a, n ):

#*****************************************************************************80
#
#% CIRCLE_ARC_GRID_POINTS computes grid points along a circular arc.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    17 April 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real R, the radius of the circle.
#
#    Input, real C(2), the coordinates of the center.
#
#    Input, real A(2), the angle of the first and last
#    points, in DEGREES.
#
#    Input, integer N, the number of points.
#
#    Output, real XY[N,2], the grid points.
#
  import numpy as np

  xy = np.zeros ( ( n, 2 ) )

  angle = np.linspace ( a[0] * np.pi / 180.0, a[1] * np.pi / 180.0, n )

  for i in range ( 0, n ):
    xy[i,0] = c[0] + r * np.cos ( angle[i] )
    xy[i,1] = c[1] + r * np.sin ( angle[i] )

  return xy

def circle_arc_grid_points_test ( ):

#*****************************************************************************80
#
## CIRCLE_ARC_GRID_POINTS_TEST demonstrates the use of CIRCLE_ARC_GRID.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    17 April 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  from circle_arc_grid_display import circle_arc_grid_display
  from r82col_print_part import r82col_print_part
  from r8mat_write import r8mat_write

  print ''
  print 'CIRCLE_ARC_GRID_POINTS_TEST'
  print '  CIRCLE_ARC_GRID_POINTS returns points along a circular arc.'
  print '  In this example, we compute points on a 90 degree arc.'

  r = 2.0
  c = np.array ( [ 5.0, 5.0 ] )
  a = np.array ( [ 0.0, 90.0 ] )
  n = 20;
#
#  Echo the input.
#
  print ''
  print '  Radius =           %g' % ( r )
  print '  Center =           %g  %g\n' % ( c[0], c[1] )
  print '  Angle 1 =          %g' % ( a[0] )
  print '  Angle 2 =          %g' % ( a[1] )
  print '  Number of points = %d' % ( n )
#
#  Compute the data.
#
  xy = circle_arc_grid_points ( r, c, a, n )
#
#  Print a little of the data.
#
  r82col_print_part ( n, xy, 10, '  Some points on the arc:' )
#
#  Write the data.
#
  filename = 'circle_arc_grid_points.xy'
  r8mat_write ( filename, n, 2, xy )
  print ''
  print '  Data written to "%s"' % ( filename )
#
#  Plot the data.
#
  filename = 'circle_arc_grid_points.png'
  circle_arc_grid_display ( r, c, a, n, xy, filename )
  print ''
  print '  Plot saved in file "%s"' % ( filename )
#
#  Terminate.
#
  print ''
  print 'CIRCLE_ARC_GRID_POINTS_TEST:'
  print '  Normal end of execution.'

  return
  
if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  circle_arc_grid_points_test ( )
  timestamp ( )
