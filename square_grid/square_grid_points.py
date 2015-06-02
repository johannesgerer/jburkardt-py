#!/usr/bin/env python
#
def square_grid_points ( ns, xv, ng ):

#*****************************************************************************80
#
## SQUARE_GRID_POINTS: grid points over a quadrilateral.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    10 April 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer NS[2], the number of points along each dimension.
#
#    Input, real XV[4,2], the vertices, in counter clockwise order.
#
#    Input, integer NG, the number of points.
#    NG = NS[0] * NS[1].
#
#    Output, real XG[NG,2], the grid points.
#
  import numpy as np
#
#  Create the 1D grids in each dimension.
#
  xg = np.zeros ( ( ng, 2 ) )

  m = ns[0]
  n = ns[1]

  ig = 0
  for j in range ( 0, n + 1 ):
    for i in range ( 0, m + 1 ):
      a0 = float ( ( m - i ) * ( n - j ) ) / float ( m * n )
      a1 = float ( (     i ) * ( n - j ) ) / float ( m * n )
      a2 = float ( (     i ) * (     j ) ) / float ( m * n )
      a3 = float ( ( m - i ) * (     j ) ) / float ( m * n )
      xg[ig,0] = a0 * xv[0,0] + a1 * xv[1,0] + a2 * xv[2,0] + a3 * xv[3,0]
      xg[ig,1] = a0 * xv[0,1] + a1 * xv[1,1] + a2 * xv[2,1] + a3 * xv[3,1]
      ig = ig + 1

  return xg

def square_grid_points_test ( m, n ):

#*****************************************************************************80
#
## SQUARE_GRID_POINTS_TEST tests SQUARE_GRID_POINTS.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 April 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  from r82col_print_part import r82col_print_part
  from r8mat_print import r8mat_print
  from r8mat_write import r8mat_write
  from square_grid_count import square_grid_count
  from square_grid_display import square_grid_display

  print ''
  print 'SQUARE_GRID_POINTS_TEST:'
  print '  SQUARE_GRID_POINTS defines a grid'
  print '  with M*N points on a side, based on a quadrilateral.'

  print ''
  print '  Input value of M is %d' % ( m )
  print '  Input value of N is %d' % ( n )

  ns = np.zeros ( 2, dtype = np.int32 );
  ns[0] = m
  ns[1] = n

  ng = square_grid_count ( ns )
  print ''
  print '  Number of grid points will be %d' % ( ng )

  xv = np.array ( [ \
    [ 0.0, 1.0 ], \
    [ 3.0, 2.0 ], \
    [ 4.0, 5.0 ], \
    [ 1.0, 3.0 ] ] )

  r8mat_print ( 4, 2, xv, '  Quadrilateral vertices:' )

  xg = square_grid_points ( ns, xv, ng )

  r82col_print_part ( ng, xg, 20, '  Part of the grid point array:' );
#
#  Write the data to a file.
#
  filename = 'square_grid_points.xy'
  r8mat_write ( filename, ng, 2, xg )
  print ''
  print '  Data written to the file "%s".' % ( filename )
#
#  Plot the data.
#
  filename = 'square_grid_points.png'
  square_grid_display ( xv, ng, xg, filename )
#
#  Terminate.
#
  print ''
  print 'SQUARE_GRID_POINTS_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  square_grid_points_test ( 6, 4 )
  timestamp ( )

