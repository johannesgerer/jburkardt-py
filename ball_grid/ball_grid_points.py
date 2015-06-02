#!/usr/bin/env python
#
def ball_grid_points ( n, r, c, ng ):

#*****************************************************************************80
#
#% BALL_GRID_POINTS computes grid points inside a ball.
#
#  Discussion:
#
#    The grid is defined by specifying the radius and center of the ball,
#    and the number of subintervals N into which the horizontal radius
#    should be divided.  Thus, a value of N = 2 will result in 5 points
#    along that horizontal line.
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
#    Input, integer N, the number of subintervals.
#
#    Input, real R, the radius of the ball.
#
#    Input, real C(3), the coordinates of the center of the ball.
#
#    Input, integer NG, the number of grid points, as determined by
#    BALL_GRID_COUNT.
#
#    Output, real BG(3,NG), the grid points inside the ball.
#
  import numpy as np

  bg = np.zeros ( ( ng, 3 ) )

  p = 0

  for i in range ( 0, n + 1 ):

    x = c[0] + r * float ( i ) / float ( n )

    for j in range ( 0, n + 1 ):

      y = c[1] + r * float ( j ) / float ( n )

      for k in range ( 0, n + 1 ):

        z = c[2] + r * float ( k ) / float ( n )

        if ( r * r < ( x - c[0] ) ** 2 \
                   + ( y - c[1] ) ** 2 \
                   + ( z - c[2] ) ** 2 ):
          break

        bg[p,0] = x
        bg[p,1] = y
        bg[p,2] = z
        p = p + 1

        if ( 0 < i ):
          bg[p,0] = 2.0 * c[0] - x
          bg[p,1] = y
          bg[p,2] = z
          p = p + 1

        if ( 0 < j ):
          bg[p,0] = x
          bg[p,1] = 2.0 * c[1] - y
          bg[p,2] = z
          p = p + 1

        if ( 0 < k ):
          bg[p,0] = x
          bg[p,1] = y
          bg[p,2] = 2.0 * c[2] - z
          p = p + 1

        if ( 0 < i and 0 < j ):
          bg[p,0] = 2.0 * c[0] - x
          bg[p,1] = 2.0 * c[1] - y
          bg[p,2] = z
          p = p + 1

        if ( 0 < i and 0 < k ):
          bg[p,0] = 2.0 * c[0] - x
          bg[p,1] = y
          bg[p,2] = 2.0 * c[2] - z
          p = p + 1

        if ( 0 < j and 0 < k ):
          bg[p,0] = x
          bg[p,1] = 2.0 * c[1] - y
          bg[p,2] = 2.0 * c[2] - z
          p = p + 1

        if ( 0 < i and 0 < j and 0 < k ):
          bg[p,0] = 2.0 * c[0] - x
          bg[p,1] = 2.0 * c[1] - y
          bg[p,2] = 2.0 * c[2] - z
          p = p + 1

  return bg

def ball_grid_points_test ( ):

#*****************************************************************************80
#
#% BALL_GRID_POINTS_TEST tests BALL_GRID_POINTS.
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
  from ball_grid_count import ball_grid_count
  from ball_grid_display import ball_grid_display
  from r83col_print_part import r83col_print_part
  from r8mat_write import r8mat_write

  print ''
  print 'BALL_GRID_POINTS_TEST:'
  print '  BALL_GRID_POINTS can define a grid of points'
  print '  with N+1 points on a horizontal or vertical radius,'
  print '  based on any ball.'

  n = 4
  r = 2.0
  c = np.array ( [ 1.0, 5.0, 2.0 ] )

  print ''
  print '  We use N = %d' % ( n )
  print '  Radius R = %g' % ( r )
  print '  Center C = (%g,%g,%g)' % ( c[0], c[1], c[2] )

  ng = ball_grid_count ( n, r, c )

  print ''
  print '  Number of grid points will be %d' % ( ng )

  xg = ball_grid_points ( n, r, c, ng )

  r83col_print_part ( ng, xg, 20, '  Part of the grid point array:' )

  filename = 'ball_grid_points.xyz'

  r8mat_write ( filename, ng, 3, xg )

  print ''
  print '  Data written to the file "%s".' % ( filename )
#
#  Plot the grid.
#
  filename = 'ball_grid_points.png'

  ball_grid_display ( r, c, ng, xg, filename )

  print ''
  print '  Plot written to the file "%s".' % ( filename )
#
#  Terminate.
#
  print ''
  print 'BALL_GRID_POINTS_TEST:'
  print '  Normal end of execution.'

  return
  
if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  ball_grid_points_test ( )
  timestamp ( )
