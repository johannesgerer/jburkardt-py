#! /usr/bin/env python
#
def ns2de_gnuplot ( header, n, x, y, u, v, s ):

#*****************************************************************************80
#
## NS2DE_GNUPLOT writes the Navier-Stokes velocity field to files for GNUPLOT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    21 January 2015
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

#
#  Write the data file.
#
  data_filename = header + '_data.txt'

  data_unit = open ( data_filename, 'w' )

  for i in range ( 0, n ):
    st = '  %g' % ( x[i] )
    data_unit.write ( st )
    st = '  %g' % ( y[i] )
    data_unit.write ( st )
    st = '  %g' % ( s * u[i] )
    data_unit.write ( st )
    st = '  %g' % ( s * v[i] )
    data_unit.write ( st )
    data_unit.write ( '\n' );

  data_unit.close ( )

  print ''
  print '  Data written to "%s".' % ( data_filename )
#
#  Write the command file.
#
  command_filename = header + '_commands.txt'
  plot_filename = header + '.png'

  command_unit = open ( command_filename, 'w' )

  command_unit.write ( '#  %s\n' % ( command_filename ) )
  command_unit.write ( '#\n' )
  command_unit.write ( 'set term png\n' )
  command_unit.write ( 'set output "%s"\n' % ( plot_filename ) )
  command_unit.write ( '#\n' )
  command_unit.write ( '#  Add titles and labels.\n' )
  command_unit.write ( '#\n' )
  command_unit.write ( 'set xlabel "<--- X --->"\n' )
  command_unit.write ( 'set ylabel "<--- Y --->"\n' )
  command_unit.write ( 'set title "Navier-Stokes velocity field"\n' )
  command_unit.write ( 'unset key\n' )
  command_unit.write ( '#\n' )
  command_unit.write ( '#  Add grid lines.\n' )
  command_unit.write ( '#\n' )
  command_unit.write ( 'set grid\n' )
  command_unit.write ( 'set size ratio -1\n' )
  command_unit.write ( '#\n' )
  command_unit.write ( '#  Timestamp the plot.\n' )
  command_unit.write ( '#\n' )
  command_unit.write ( 'set timestamp\n' )
  command_unit.write ( 'plot "%s" using 1:2:3:4 with vectors \\\n' % ( data_filename ) )
  command_unit.write ( '  head filled lt 2 linecolor rgb "blue"\n' )
  command_unit.write ( 'quit\n' )

  data_unit.close ( )

  print '  Commands written to "%s".' % ( command_filename )

  return

def ns2de_gnuplot_lucas_test ( ):

#*****************************************************************************80
#
## NS2DE_GNUPLOT_LUCAS_TEST plots the Lucas Bystricky flow field.
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
  print 'NS2DE_GNUPLOT_LUCAS_TEST:'
  print '  Generate the Lucas Bystricky velocity field on a regular grid.'
  print '  Store in GNUPLOT data and command files.'

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
  ns2de_gnuplot ( header, n, x, y, u, v, s )

  print 'NS2DE_GNUPLOT_LUCAS_TEST:'
  print '  Normal end of execution.'

  return
def ns2de_gnuplot_spiral_test ( ):

#*****************************************************************************80
#
## NS2DE_GNUPLOT_SPIRAL_TEST plots a Spiral Flow velocity field.
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
  print 'NS2DE_GNUPLOT_SPIRAL_TEST:'
  print '  Generate a Spiral Flow velocity field on a regular grid.'
  print '  Store in GNUPLOT data and command files.'

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
  ns2de_gnuplot ( header, n, x, y, u, v, s )

  print 'NS2DE_GNUPLOT_SPIRAL_TEST:'
  print '  Normal end of execution.'

  return

def ns2de_gnuplot_taylor_test ( ):

#*****************************************************************************80
#
## NS2DE_GNUPLOT_TAYLOR_TEST generates a velocity field on a regular grid and plots it.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    21 January 2015
#
#  Author:
#
#    John Burkardt
#
  from grid_2d import grid_2d
  from uvp_taylor import uvp_taylor

  print ''
  print 'NS2DE_GNUPLOT_TAYLOR_TEST:'
  print '  Generate a Taylor Vortex velocity field on a regular grid.'
  print '  Store in GNUPLOT data and command files.'

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
  ns2de_gnuplot ( header, n, x, y, u, v, s )

  print ''
  print 'NS2DE_GNUPLOT_TAYLOR_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  ns2de_gnuplot_lucas_test ( )
  ns2de_gnuplot_spiral_test ( )
  ns2de_gnuplot_taylor_test ( )
  timestamp ( )
