#! /usr/bin/env python
#
def stokes_matplotlib ( header, n, x, y, u, v, s ):

#*****************************************************************************80
#
## STOKES_MATPLOTLIB plots the Stokes velocity vector field with MATPLOTLIB.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 January 2015
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

def stokes1_matplotlib_test ( ):

#*****************************************************************************80
#
## STOKES1_MATPLOTLIB_TEST generates a field on a regular grid and plots it.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 January 2015
#
#  Author:
#
#    John Burkardt
#
  from grid_2d import grid_2d
  from uvp_stokes1 import uvp_stokes1

  print ''
  print 'STOKES1_MATPLOTLIB_TEST:'
  print '  Exact flow #1.'
  print '  Generate a Stokes velocity field on a regular grid.'
  print '  Display it using MATPLOTLIB'

  x_lo = 0.0
  x_hi = 1.0
  x_num = 21

  y_lo = 0.0
  y_hi = 1.0
  y_num = 21

  [ x, y ] = grid_2d ( x_num, x_lo, x_hi, y_num, y_lo, y_hi )

  n = x_num * y_num
 
  [ u, v, p ] = uvp_stokes1 ( n, x, y )

  header = 'stokes1'
  s = 4.0
  stokes_matplotlib ( header, n, x, y, u, v, s )

  print ''
  print 'STOKES1_MATPLOTLIB_TEST:'
  print '  Normal end of execution.'

  return

def stokes2_matplotlib_test ( ):

#*****************************************************************************80
#
## STOKES2_MATPLOTLIB_TEST generates a field on a regular grid and plots it.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 January 2015
#
#  Author:
#
#    John Burkardt
#
  from grid_2d import grid_2d
  from uvp_stokes2 import uvp_stokes2

  print ''
  print 'STOKES2_MATPLOTLIB_TEST:'
  print '  Exact flow #2.'
  print '  Generate a Stokes velocity field on a regular grid.'
  print '  Display it using MATPLOTLIB'

  x_lo = 0.0
  x_hi = 1.0
  x_num = 21

  y_lo = 0.0
  y_hi = 1.0
  y_num = 21

  [ x, y ] = grid_2d ( x_num, x_lo, x_hi, y_num, y_lo, y_hi )

  n = x_num * y_num
 
  [ u, v, p ] = uvp_stokes2 ( n, x, y )

  header = 'stokes2'
  s = 0.05
  stokes_matplotlib ( header, n, x, y, u, v, s )

  print ''
  print 'STOKES2_MATPLOTLIB_TEST:'
  print '  Normal end of execution.'

  return

def stokes3_matplotlib_test ( ):

#*****************************************************************************80
#
## STOKES3_MATPLOTLIB_TEST generates a field on a regular grid and plots it.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    12 February 2015
#
#  Author:
#
#    John Burkardt
#
  from grid_2d import grid_2d
  from uvp_stokes3 import uvp_stokes3

  print ''
  print 'STOKES3_MATPLOTLIB_TEST:'
  print '  Exact flow #3.'
  print '  Generate a Stokes velocity field on a regular grid.'
  print '  Display it using MATPLOTLIB'

  x_lo = -1.0
  x_hi = +1.0
  x_num = 21

  y_lo = -1.0
  y_hi = +1.0
  y_num = 21

  [ x, y ] = grid_2d ( x_num, x_lo, x_hi, y_num, y_lo, y_hi )

  n = x_num * y_num
 
  [ u, v, p ] = uvp_stokes3 ( n, x, y )

  header = 'stokes3'
  s = 0.05
  stokes_matplotlib ( header, n, x, y, u, v, s )

  print ''
  print 'STOKES3_MATPLOTLIB_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  stokes1_matplotlib_test ( )
  stokes2_matplotlib_test ( )
  stokes3_matplotlib_test ( )
  timestamp ( )
