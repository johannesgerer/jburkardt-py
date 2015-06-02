#! /usr/bin/env python
#
def polygon_grid_display ( n, nv, v, ng, xg, filename ):

#*****************************************************************************80
#
## POLYGON_GRID_DISPLAY displays grid points inside a polygon.
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
#    Input, real XG[NG,2], the grid points.
#
#    Input, string FILENAME, the name of the plotfile to be created.
#
  import matplotlib.pyplot as plt
  import numpy as np
#
#  Determine the centroid.
#
  vcx = 0.0
  vcy = 0.0
  for i in range ( 0, nv ):
    vcx = vcx + v[i,0]
    vcy = vcy + v[i,1]
  vcx = vcx / float ( nv )
  vcy = vcy / float ( nv )
#
#  Plot the outline of the polygon.
#
  plt.plot ( v[0:nv,0], v[0:nv,1], linewidth = 2.0, color = 'r' )
  plt.plot ( [ v[nv-1,0], v[0,0] ], [ v[nv-1,1], v[0,1] ], linewidth = 2.0, color = 'r' )
#
#  Plot the internal "ribs"
#
  for i in range ( 0, nv ):
    plt.plot ( [ v[i,0], vcx ], [ v[i,1], vcy ], linewidth = 2.0, color = 'k' )
#
#  Plot the gridpoints.
#
  plt.plot ( xg[0:ng,0], xg[0:ng,1], 'bs' )
#
#  Cleanup and annotate.
#
  plt.xlabel ( '<---X--->' )
  plt.ylabel ( '<---Y--->' )
  plt.title ( 'Grid points in polygon' )
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

def polygon_grid_display_test ( ):

#*****************************************************************************80
#
## POLYGON_GRID_DISPLAY_TEST tests POLYGON_GRID_DISPLAY.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 May 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ''
  print 'POLYGON_GRID_DISPLAY_TEST:'
  print '  POLYGON_GRID_DISPLAY displays a grid of points in a polygon.'

  n = 2

  nv = 4
  v = np.array ( [ \
    [ 0.0, 0.0 ], \
    [ 1.0, 0.0 ], \
    [ 2.0, 1.0 ], \
    [ 1.0, 1.0 ] ] )

  ng = 13
  xg = np.array ( [ \
    [ 0.0, 0.0 ], \
    [ 0.5, 0.0 ], \
    [ 1.0, 0.0 ], \
    [ 0.5, 0.25 ], \
    [ 1.0, 0.25 ], \
    [ 0.5, 0.5 ], \
    [ 1.0, 0.5 ], \
    [ 1.5, 0.5 ], \
    [ 1.0, 0.75 ], \
    [ 1.5, 0.75 ], \
    [ 1.0, 1.0 ], \
    [ 1.5, 1.0 ], \
    [ 2.0, 1.0 ] ] )

  filename = 'polygon_grid_display_test.png'

  polygon_grid_display ( n, nv, v, ng, xg, filename )
#
#  Terminate.
#
  print ''
  print 'POLYGON_GRID_DISPLAY_TEST:'
  print '  Normal end of execution.'

  return
  
if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  polygon_grid_display_test ( )
  timestamp ( )

