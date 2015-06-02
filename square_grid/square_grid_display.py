#!/usr/bin/env python
#
def square_grid_display ( xv, ng, xg, filename ):

#*****************************************************************************80
#
## SQUARE_GRID_DISPLAY displays grid points inside a quadrilateral.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#   10 April 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real XV(4,2), the coordinates of the vertices.
#
#    Input, integer NG, the number of grid points.
#
#    Input, real XG(NG,2), the grid points.
#
#    Input, string FILENAME, the name of the plotfile to be created.
#
  import matplotlib.pyplot as plt
  import numpy as np
#
#  Plot the outline.
#
  qx = np.zeros ( 5 )
  qy = np.zeros ( 5 )

  qx[0] = xv[0,0];
  qx[1] = xv[1,0];
  qx[2] = xv[2,0];
  qx[3] = xv[3,0];
  qx[4] = xv[0,0];

  qy[0] = xv[0,1];
  qy[1] = xv[1,1];
  qy[2] = xv[2,1];
  qy[3] = xv[3,1];
  qy[4] = xv[0,1];

  plt.plot ( qx, qy, linewidth = 2.0, color = 'r' )
#
#  Plot the gridpoints.
#
  plt.plot ( xg[0:ng,0], xg[0:ng,1], 'bs' )
#
#  Cleanup and annotate.
#
  plt.xlabel ( '<---X--->' )
  plt.ylabel ( '<---Y--->' )
  plt.title ( 'Grid points in quadrilateral' )
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

def square_grid_display_test ( ):

#*****************************************************************************80
#
## SQUARE_GRID_DISPLAY displays grid points inside a quadrilateral.
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
  print 'SQUARE_GRID_DISPLAY_TEST:'
  print '  SQUARE_GRID_DISPLAY displays a grid of points in a quadrilateral.'

  xv = np.array ( [ \
    [ 2.0, 1.0 ], \
    [ 5.0, 4.0 ], \
    [ 3.0, 6.0 ], \
    [ 0.0, 3.0 ] ] )

  ng = 18
  xg = np.array ( [ \
    [ 2.0, 1.0 ], \
    [ 1.0, 2.0 ], \
    [ 2.0, 2.0 ], \
    [ 3.0, 2.0 ], \
    [ 0.0, 3.0 ], \
    [ 1.0, 3.0 ], \
    [ 2.0, 3.0 ], \
    [ 3.0, 3.0 ], \
    [ 4.0, 3.0 ], \
    [ 1.0, 4.0 ], \
    [ 2.0, 4.0 ], \
    [ 3.0, 4.0 ], \
    [ 4.0, 4.0 ], \
    [ 5.0, 4.0 ], \
    [ 2.0, 5.0 ], \
    [ 3.0, 5.0 ], \
    [ 4.0, 5.0 ], \
    [ 3.0, 6.0 ] ] )

  filename = 'square_grid_display.png'

  square_grid_display ( xv, ng, xg, filename )
#
#  Terminate.
#
  print ''
  print 'SQUARE_GRID_DISPLAY_TEST:'
  print '  Normal end of execution.'

  return
  
if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  square_grid_display_test ( )
  timestamp ( )
