#! /usr/bin/env python
#
def disk_grid_display ( n, r, c, ng, cg, filename ):

#*****************************************************************************80
#
## DISK_GRID_DISPLAY displays grid points inside a disk.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    05 September 2010
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of subintervals.
#
#    Input, real R, the radius of the disk.
#
#    Input, real C(2), the coordinates of the center of the disk.
#
#    Input, integer NG, the number of grid points inside the disk.
#
#    Input, real CG(2,NG), the grid points.
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
  for i in range ( 0, 51 ):
    t = 2.0 * np.pi * float ( i ) / 50.0
    cx[i] = c[0] + r * np.cos ( t )
    cy[i] = c[1] + r * np.sin ( t )

  plt.plot ( cx, cy, linewidth = 2.0, color = 'r' )
#
#  Plot the gridpoints.
#
  plt.plot ( cg[0,0:ng], cg[1,0:ng], 'bs' )
#
#  Cleanup and annotate.
#
  plt.xlabel ( '<---X--->' )
  plt.ylabel ( '<---Y--->' )
  plt.title ( 'Grid points in circle' )
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

def disk_grid_display_test ( ):

#*****************************************************************************80
#
## DISK_GRID_DISPLAY displays grid points inside a disk.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    07 April 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ''
  print 'DISK_GRID_DISPLAY_TEST:'
  print '  DISK_GRID_DISPLAY can display a grid of points in a disk.'

  n = 1
  r = 2.0
  c = np.array ( [ 0.0, 0.0 ] )
  ng = 9
  cg = np.array ( [ \
    [ -1.0,  1.0 ], \
    [  0.0,  1.0 ], \
    [  1.0,  1.0 ], \
    [ -1.0,  0.0 ], \
    [  0.0,  0.0 ], \
    [  1.0,  0.0 ], \
    [ -1.0, -1.0 ], \
    [  0.0, -1.0 ], \
    [  1.0, -1.0 ] ] )

  cg = np.transpose ( cg )
  filename = 'disk_grid_display.png'

  disk_grid_display ( n, r, c, ng, cg, filename )
#
#  Terminate.
#
  print ''
  print 'DISK_GRID_DISPLAY_TEST:'
  print '  Normal end of execution.'

  return
  
if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  disk_grid_display_test ( )
  timestamp ( )
