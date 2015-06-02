#! /usr/bin/env python
#
def ellipse_grid_points ( n, r, c, ng ):

#*****************************************************************************80
#
## ELLIPSE_GRID_POINTS generates grid points inside an ellipse.
#
#  Discussion:
#
#    The ellipse is specified as
#
#      ( ( X - C1 ) / R1 )^2 + ( ( Y - C2 ) / R2 )^2 = 1
#
#    The user supplies a number N.  There will be N+1 grid points along
#    the shorter axis.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 April 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of subintervals.
#
#    Input, real R(2), the half axis lengths.
#
#    Input, real C(2), the center of the ellipse.
#
#    Input, integer NG, the number of grid points inside the ellipse.
#
#    Output, real XY(2,NG), the grid points.
#
  import numpy as np

  if ( r[0] < r[1] ):
    h = 2.0 * r[0] / float ( 2 * n + 1 )
    ni = n
    nj = np.ceil ( r[1] / r[0] ) * n
  else:
    h = 2.0 * r[1] / float ( 2 * n + 1 )
    nj = n
    ni = np.ceil ( r[0] / r[1] ) * n

  p = 0
  xy = np.zeros ( [ 2, ng ] )

  for j in range ( 0, nj + 1 ):
    i = 0
    x = c[0]
    y = c[1] + float ( j ) * h

    xy[0,p] = x
    xy[1,p] = y
    p = p + 1
    if ( 0 < j ):
      xy[0,p] = x
      xy[1,p] = 2.0 * c[1] - y
      p = p + 1

    while ( True ):
      i = i + 1
      x = c[0] + float ( i ) * h
      if ( 1.0 < ( ( x - c[0] ) / r[0] ) ** 2 + ( ( y - c[1] ) / r[1] ) ** 2 ):
        break

      xy[0,p] = x
      xy[1,p] = y
      p = p + 1
      xy[0,p] = 2.0 * c[0] - x
      xy[1,p] = y
      p = p + 1
      if ( 0 < j ):
        xy[0,p] = x
        xy[1,p] = 2.0 * c[1] - y
        p = p + 1
        xy[0,p] = 2.0 * c[0] - x
        xy[1,p] = 2.0 * c[1] - y
        p = p + 1

  return xy

def ellipse_grid_points_test ( ):

#*****************************************************************************80
#
#% ELLIPSE_GRID_POINTS_TEST tests ELLIPSE_GRID_POINTS.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 April 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  from ellipse_grid_count import ellipse_grid_count
  from ellipse_grid_display import ellipse_grid_display
  from r82vec_print_part import r82vec_print_part
  from r8mat_transpose_write import r8mat_transpose_write

  print ''
  print 'ELLIPSE_GRID_POINTS_TEST:'
  print '  ELLIPSE_GRID_POINTS can define a grid of points'
  print '  with N+1 points on the minor half axis,'
  print '  based on any ellipse.'

  n = 8
  r = np.array ( [ 2.0, 1.0 ] )
  c = np.array ( [ 1.0, 2.0 ] )

  print ''
  print '  We use N = %d' % ( n )
  print '  Radius R = (%g,%g)' % ( r[0], r[1] )
  print '  Center C = (%g,%g)' % ( c[0], c[1] )

  ng = ellipse_grid_count ( n, r, c )

  print ''
  print '  Number of grid points will be %d' % ( ng )

  cg = ellipse_grid_points ( n, r, c, ng )

  r82vec_print_part ( ng, cg, 20, '  Part of the grid point array:' )
#
#  Write grid points to a file.
#
  filename = 'ellipse_grid.xy'

  r8mat_transpose_write ( filename, 2, ng, cg );

  print ''
  print '  Data written to the file "%s".' % ( filename )
#
#  Plot the grid, and save the plot in a file.
#
  filename = 'ellipse_grid.png'
  ellipse_grid_display ( n, r, c, ng, cg, filename )
#
#  Terminate.
#
  print ''
  print 'ELLIPSE_GRID_POINTS_TEST:'
  print '  Normal end of execution.'

  return
  
if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  ellipse_grid_points_test ( )
  timestamp ( )
