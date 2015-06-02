#!/usr/bin/env python
#
def triangle_grid_display ( t, ng, tg, filename ):

#*****************************************************************************80
#
## TRIANGLE_GRID_DISPLAY displays grid points inside a triangle.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#   09 April 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real T(3,2), the coordinates of the vertices of the triangle.
#
#    Input, integer NG, the number of grid points inside the triangle.
#
#    Input, real TG(NG,2), the grid points.
#
#    Input, string FILENAME, the name of the plotfile to be created.
#
  import matplotlib.pyplot as plt
  import numpy as np
#
#  Plot the outline of the triangle.
#
  tx = np.zeros ( 4 )
  ty = np.zeros ( 4 )

  tx[0] = t[0,0];
  tx[1] = t[1,0];
  tx[2] = t[2,0];
  tx[3] = t[0,0];
  ty[0] = t[0,1];
  ty[1] = t[1,1];
  ty[2] = t[2,1];
  ty[3] = t[0,1];

  plt.plot ( tx, ty, linewidth = 2.0, color = 'r' )
#
#  Plot the gridpoints.
#
  plt.plot ( tg[0:ng,0], tg[0:ng,1], 'bs' )
#
#  Cleanup and annotate.
#
  plt.xlabel ( '<---X--->' )
  plt.ylabel ( '<---Y--->' )
  plt.title ( 'Grid points in triangle' )
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

def triangle_grid_display_test ( ):

#*****************************************************************************80
#
## TRIANGLE_GRID_DISPLAY displays grid points inside a triangle.
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
  import numpy as np

  print ''
  print 'TRIANGLE_GRID_DISPLAY_TEST:'
  print '  TRIANGLE_GRID_DISPLAY displays a grid of points in a triangle.'

  t = np.array ( [ \
    [ 1.0, 3.0 ], \
    [ 6.0, 4.0 ], \
    [ 3.0, 8.0 ] ] )

  ng = 11
  tg = np.array ( [ \
    [ 2.0, 4.0 ], \
    [ 3.0, 4.0 ], \
    [ 4.0, 4.0 ], \
    [ 5.0, 4.0 ], \
    [ 2.0, 5.0 ], \
    [ 3.0, 5.0 ], \
    [ 4.0, 5.0 ], \
    [ 5.0, 5.0 ], \
    [ 3.0, 6.0 ], \
    [ 4.0, 6.0 ], \
    [ 3.0, 7.0 ] ] )

  filename = 'triangle_grid_display.png'

  triangle_grid_display ( t, ng, tg, filename )
#
#  Terminate.
#
  print ''
  print 'TRIANGLE_GRID_DISPLAY_TEST:'
  print '  Normal end of execution.'

  return
  
if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  triangle_grid_display_test ( )
  timestamp ( )
