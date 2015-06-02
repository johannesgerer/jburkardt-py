#! /usr/bin/env python
#
def stokes_gnuplot ( header, n, x, y, u, v, s ):

#*****************************************************************************80
#
## STOKES_GNUPLOT writes the Stokes velocity vector field to files for GNUPLOT.
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
  command_unit.write ( 'set title "Stokes velocity field"\n' )
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

def stokes1_gnuplot_test ( ):

#*****************************************************************************80
#
## STOKES1_GNUPLOT_TEST generates a field on a regular grid and plots it.
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
  print 'STOKES1_GNUPLOT_TEST:'
  print '  Exact solution #1.'
  print '  Generate a Stokes velocity field on a regular grid.'
  print '  Store in GNUPLOT data and command files.'

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
  stokes_gnuplot ( header, n, x, y, u, v, s )

  print ''
  print 'STOKES1_GNUPLOT_TEST:'
  print '  Normal end of execution.'

  return

def stokes2_gnuplot_test ( ):

#*****************************************************************************80
#
## STOKES2_GNUPLOT_TEST generates a field on a regular grid and plots it.
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
  print 'STOKES2_GNUPLOT_TEST:'
  print '  Exact solution #2.'
  print '  Generate a Stokes velocity field on a regular grid.'
  print '  Store in GNUPLOT data and command files.'

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
  stokes_gnuplot ( header, n, x, y, u, v, s )

  print ''
  print 'STOKES2_GNUPLOT_TEST:'
  print '  Normal end of execution.'

  return

def stokes3_gnuplot_test ( ):

#*****************************************************************************80
#
## STOKES3_GNUPLOT_TEST generates a field on a regular grid and plots it.
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
  print 'STOKES3_GNUPLOT_TEST:'
  print '  Exact solution #3.'
  print '  Generate a Stokes velocity field on a regular grid.'
  print '  Store in GNUPLOT data and command files.'

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
  stokes_gnuplot ( header, n, x, y, u, v, s )

  print ''
  print 'STOKES3_GNUPLOT_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  stokes1_gnuplot_test ( )
  stokes2_gnuplot_test ( )
  stokes3_gnuplot_test ( )
  timestamp ( )
