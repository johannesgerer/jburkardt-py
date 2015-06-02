#! /usr/bin/env python
#
def spiral_matplotlib ( header, n, x, y, u, v, s ):

#*****************************************************************************80
#
## SPIRAL_MATPLOTLIB plots the velocity vector field with MATPLOTLIB.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, string HEADER, a header to be used to name the files.
#
#    Input, integer N, the number of evaluation points.
#
#    Input, real X(N), Y(N), the coordinates of the evaluation points.
#
#    Input, real U(N), V(N), the velocity components.
#
#    Input, real S, a scale factor for the velocity vectors.
#
  import matplotlib.pyplot as plt

  myplot = plt.figure ( )
  ax = plt.gca ( )
  ax.quiver ( x, y, u, v )
  ax.set_xlabel ( '<--X-->' )
  ax.set_ylabel ( '<--Y-->' )
  ax.set_title ( header )
  ax.axis ( 'equal' )
  plt.draw ( )
  plt.show ( )

  plot_filename = header + '_matplotlib.png'
  myplot.savefig ( plot_filename )

  return

def spiral_matplotlib_test ( ):

#*****************************************************************************80
#
## SPIRAL_MATPLOTLIB_TEST generates a field on a regular grid and plots it.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    20 January 2015
#
#  Author:
#
#    John Burkardt
#
  from grid_2d import grid_2d
  from uv_spiral import uv_spiral

  print ''
  print 'SPIRAL_MATPLOTLIB_TEST:'
  print '  Generate a spiral velocity field on a regular grid.'
  print '  Display it using MATPLOTLIB'

  x_lo = 0.0
  x_hi = 1.0
  x_num = 21

  y_lo = 0.0
  y_hi = 1.0
  y_num = 21

  [ x, y ] = grid_2d ( x_num, x_lo, x_hi, y_num, y_lo, y_hi )

  n = x_num * y_num
  c = 1.0

  [ u, v ] = uv_spiral ( n, x, y, c )

  header = 'spiral'
  s = 0.05
  spiral_matplotlib ( header, n, x, y, u, v, s )

  print ''
  print 'SPIRAL_GMATPLOTLIB_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  spiral_matplotlib_test ( )
  timestamp ( )
