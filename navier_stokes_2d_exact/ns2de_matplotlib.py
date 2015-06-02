#! /usr/bin/env python
#
def ns2de_matplotlib ( header, n, x, y, u, v, s ):

#*****************************************************************************80
#
## NS2DE_MATPLOTLIB plots a velocity vector field with MATPLOTLIB.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    23 January 2015
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

def ns2de_matplotlib_lucas_test ( ):

#*****************************************************************************80
#
## NS2DE_MATPLOTLIB_LUCAS_TEST plots a Lucas Bystricky velocity field.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    07 March 2015
#
#  Author:
#
#    John Burkardt
#
  from grid_2d import grid_2d
  from uvp_lucas import uvp_lucas

  print ''
  print 'NS2DE_MATPLOTLIB_LUCAS_TEST:'
  print '  Generate a Lucas Bystricky Flow field on a regular grid.'
  print '  Display it using MATPLOTLIB'

  x_lo = 0.0
  x_hi = 1.0
  x_num = 21

  y_lo = 0.0
  y_hi = 1.0
  y_num = 21

  [ x, y ] = grid_2d ( x_num, x_lo, x_hi, y_num, y_lo, y_hi )

  nu = 1.0
  rho = 1.0
  n = x_num * y_num
  t = 0.0

  [ u, v, p ] = uvp_lucas ( nu, rho, n, x, y, t )

  header = 'lucas'
  s = 0.25
  ns2de_matplotlib ( header, n, x, y, u, v, s )

  print ''
  print 'NS2DE_MATPLOTLIB_LUCAS_TEST:'
  print '  Normal end of execution.'

  return

def ns2de_matplotlib_spiral_test ( ):

#*****************************************************************************80
#
## NS2DE_MATPLOTLIB_SPIRAL_TEST plots a Spiral Flow velocity field.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    31 January 2015
#
#  Author:
#
#    John Burkardt
#
  from grid_2d import grid_2d
  from uvp_spiral import uvp_spiral

  print ''
  print 'NS2DE_MATPLOTLIB_SPIRAL_TEST:'
  print '  Generate a Spiral Flow velocity field on a regular grid.'
  print '  Display it using MATPLOTLIB'

  x_lo = 0.0
  x_hi = 1.0
  x_num = 21

  y_lo = 0.0
  y_hi = 1.0
  y_num = 21

  [ x, y ] = grid_2d ( x_num, x_lo, x_hi, y_num, y_lo, y_hi )

  nu = 1.0
  rho = 1.0
  n = x_num * y_num
  t = 0.0

  [ u, v, p ] = uvp_spiral ( nu, rho, n, x, y, t )

  header = 'spiral'
  s = 5.0
  ns2de_matplotlib ( header, n, x, y, u, v, s )

  print ''
  print 'NS2DE_MATPLOTLIB_SPIRAL_TEST:'
  print '  Normal end of execution.'

  return

def ns2de_matplotlib_taylor_test ( ):

#*****************************************************************************80
#
## NS2DE_MATPLOTLIB_TAYLOR_TEST plots a Taylor Vortex Flow field.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    23 January 2015
#
#  Author:
#
#    John Burkardt
#
  from grid_2d import grid_2d
  from uvp_taylor import uvp_taylor

  print ''
  print 'NS2DE_MATPLOTLIB_TAYLOR_TEST:'
  print '  Generate a velocity field on a regular grid.'
  print '  Display it using MATPLOTLIB'

  x_lo = 0.5
  x_hi = 2.5
  x_num = 21

  y_lo = 0.5
  y_hi = 2.5
  y_num = 21

  [ x, y ] = grid_2d ( x_num, x_lo, x_hi, y_num, y_lo, y_hi )

  nu = 1.0
  rho = 1.0
  n = x_num * y_num
  t = 0.0

  [ u, v, p ] = uvp_taylor ( nu, rho, n, x, y, t )

  header = 'taylor'
  s = 0.10
  ns2de_matplotlib ( header, n, x, y, u, v, s )

  print ''
  print 'NS2DE_MATPLOTLIB_TAYLOR_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  ns2de_matplotlib_lucas_test ( )
  ns2de_matplotlib_spiral_test ( )
  ns2de_matplotlib_taylor_test ( )
  timestamp ( )
