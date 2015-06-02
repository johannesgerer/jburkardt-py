#!/usr/bin/env python
#
def ball_grid_count ( n, r, c ):

#*****************************************************************************80
#
## BALL_GRID computes grid points inside a ball.
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
#    Output, integer NG, the number of grid points inside the ball.
#
  ng = 0

  for i in range ( 0, n + 1 ):

    x = c[0] + r * float ( 2 * i ) / float (  2 * n + 1 )
    
    for j in range ( 0, n + 1 ):

      y = c[1] + r * float ( 2 * j ) / float (  2 * n + 1 )
      
      for k in range ( 0, n + 1 ):

        z = c[2] + r * float ( 2 * k ) / float (  2 * n + 1 )

        if ( r * r < ( x - c[0] ) ** 2 \
                   + ( y - c[1] ) ** 2 \
                   + ( z - c[2] ) ** 2 ):
          break

        ng = ng + 1

        if ( 0 < i ):
          ng = ng + 1

        if ( 0 < j ):
          ng = ng + 1

        if ( 0 < k ):
          ng = ng + 1

        if ( 0 < i and 0 < j ):
          ng = ng + 1

        if ( 0 < i and 0 < k ):
          ng = ng + 1

        if ( 0 < j and 0 < k ):
          ng = ng + 1

        if ( 0 < i and 0 < j and 0 < k ):
          ng = ng + 1

  return ng

def ball_grid_count_test ( ):

#*****************************************************************************80
#
## BALL_GRID_REGULAR_COUNT counts the grid points inside a ball.
#
#  Discussion:
#
#    The grid is defined by specifying the radius and center of the ball,
#    and the number of subintervals N into which the radius
#    should be divided.
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
  print 'BALL_GRID_COUNT_TEST:'
  print '  BALL_GRID_COUNT counts the number of grid points needed'
  print '  for a grid of points inside a ball of radius R and center C.'

  print ''
  print '  N = number of subintervals of the horizontal radius.'
  print '  NG = resulting number of grid points.'
  print ''
  print '     N        NG'
  print ''

  for n in [ 1, 2, 4, 8, 16  ]:
    r = 1.0
    c = np.array ( [ 0.0, 0.0, 0.0 ] )
    ng = ball_grid_count ( n, r, c )
    print '  %4d  %8d' % ( n, ng )

  print ''
  print 'BALL_GRID_COUNT_TEST:'
  print '  Normal end of execution.'

  return
  
if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  ball_grid_count_test ( )
  timestamp ( )
