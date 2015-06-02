#!/usr/bin/env python
#
def ball_grid_display ( r, c, ng, xg, filename ):

#*****************************************************************************80
#
## BALL_GRID_DISPLAY displays grid points inside a ball.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    11 April 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real R, the radius of the disk.
#
#    Input, real C(3), the coordinates of the center of the disk.
#
#    Input, integer NG, the number of grid points inside the ball.
#
#    Input, real XG(NG,3), the grid points.
#
#    Input, real R, the radius of the disk.
#
#    Input, string FILENAME, the name of the plotfile to be created.
#
  import matplotlib.pyplot as plt
  from mpl_toolkits.mplot3d import Axes3D

  fig = plt.figure ( )
  ax = fig.add_subplot ( 111, projection = '3d' )
  ax.scatter ( xg[:,0], xg[:,1], xg[:,2], 'b' );

  ax.set_xlabel ( '<---X--->' )
  ax.set_ylabel ( '<---Y--->' )
  ax.set_zlabel ( '<---Z--->' )
  ax.set_title ( 'Grid points in ball' )
  ax.grid ( True )
  ax.axis ( 'equal' )
# plt.show ( )
  plt.savefig ( filename )

  plt.clf ( )

  return

def ball_grid_display_test ( ):

#*****************************************************************************80
#
## BALL_GRID_DISPLAY displays grid points inside a ball.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    11 April 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ''
  print 'BALL_GRID_DISPLAY_TEST:'
  print '  BALL_GRID_DISPLAY can display a grid of points in a ball.'

  r = 2.0
  c = np.array ( [ 0.0, 0.0, 0.0 ] )
  ng = 25
  xg = np.array ( [ \
    [  0.0,  0.0,  0.0 ], \
    [  1.0,  0.0,  0.0 ], \
    [ -1.0,  0.0,  0.0 ], \
    [  0.0,  1.0,  0.0 ], \
    [  0.0, -1.0,  0.0 ], \
    [  0.0,  0.0,  1.0 ], \
    [  0.0,  0.0, -1.0 ], \
    [  1.0,  1.0,  0.0 ], \
    [  1.0, -1.0,  0.0 ], \
    [  1.0,  0.0,  1.0 ], \
    [  1.0,  0.0, -1.0 ], \
    [ -1.0,  1.0,  0.0 ], \
    [ -1.0, -1.0,  0.0 ], \
    [ -1.0,  0.0,  1.0 ], \
    [ -1.0,  0.0, -1.0 ], \
    [  0.0,  1.0,  1.0 ], \
    [  0.0,  1.0, -1.0 ], \
    [  0.0, -1.0,  1.0 ], \
    [  0.0, -1.0, -1.0 ], \
    [  2.0,  0.0,  0.0 ], \
    [ -2.0,  0.0,  0.0 ], \
    [  0.0,  2.0,  0.0 ], \
    [  0.0, -2.0,  0.0 ], \
    [  0.0,  0.0,  2.0 ], \
    [  0.0,  0.0, -2.0 ] ] )

  filename = 'ball_grid_display.png'

  ball_grid_display ( r, c, ng, xg, filename )
#
#  Terminate.
#
  print ''
  print 'BALL_GRID_DISPLAY_TEST:'
  print '  Normal end of execution.'

  return
  
if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  ball_grid_display_test ( )
  timestamp ( )

