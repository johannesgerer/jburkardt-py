#! /usr/bin/env python
#
def circle_arc_grid_display ( r, c, a, ng, cg, filename ):

#*****************************************************************************80
#
## CIRCLE_ARC_GRID_DISPLAY displays grid points along a circular arc.
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
#    Input, real R, the radius of the disk.
#
#    Input, real C(2), the coordinates of the center of the disk.
#
#    Input, real A(2), the initial and final angles, in degrees.
#
#    Input, integer NG, the number of grid points inside the disk.
#
#    Input, real CG[NG,2], the grid points.
#
#    Input, string FILENAME, the name of the plotfile to be created.
#
  import matplotlib.pyplot as plt
  import numpy as np
#
#  Make points on the circumference and plot them.
#
  cx = np.zeros ( 51 )
  cy = np.zeros ( 51 )
  angle = np.linspace ( a[0] * np.pi / 180.0, a[1] * np.pi / 180.0, 51 )

  for i in range ( 0, 51 ):
    cx[i] = c[0] + r * np.cos ( angle[i] )
    cy[i] = c[1] + r * np.sin ( angle[i] )

  plt.plot ( cx, cy, linewidth = 2.0, color = 'r' )
#
#  Plot the gridpoints.
#
  plt.plot ( cg[0:ng,0], cg[0:ng,1], 'bs' )
#
#  Cleanup and annotate.
#
  plt.xlabel ( '<---X--->' )
  plt.ylabel ( '<---Y--->' )
  plt.title ( 'Grid points along circular arc' )
  plt.grid ( True )
  plt.axis ( 'equal' )
# plt.show ( )
#
#  Save plot to file.
#
  plt.savefig ( filename )

  plt.clf ( )

  print ''
  print '  Graphics data saved in file "%s"' % (filename )

  return

def circle_arc_grid_display_test ( ):

#*****************************************************************************80
#
## CIRCLE_ARC_GRID_DISPLAY displays grid points along a circular arc.
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
  from circle_arc_grid_points import circle_arc_grid_points

  print ''
  print 'CIRCLE_ARC_GRID_DISPLAY_TEST:'
  print '  CIRCLE_ARC_GRID_DISPLAY can display a grid of points along a circular arc.'

  r = 3.0
  c = np.array ( [ 4.0, 6.0 ] )
  a = np.array ( [ -30.0, 120.0 ] )
  n = 20
#
#  Compute the data.
#
  xy = circle_arc_grid_points ( r, c, a, n )
#
#  Plot the data.
#
  filename = 'circle_arc_grid_display.png'
  circle_arc_grid_display ( r, c, a, n, xy, filename )
#
#  Terminate.
#
  print ''
  print 'CIRCLE_ARC_GRID_DISPLAY_TEST:'
  print '  Normal end of execution.'

  return
  
if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  circle_arc_grid_display_test ( )
  timestamp ( )
