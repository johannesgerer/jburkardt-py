#!/usr/bin/env python
#
def triangle_grid_points ( n, t ):

#*****************************************************************************80
#
## TRIANGLE_GRID_POINTS computes points on a triangular grid.
#
#  Discussion:
#
#    The grid is defined by specifying the coordinates of an enclosing
#    triangle T, and the number of subintervals each side of the triangle
#    should be divided into.
#
#    Choosing N = 10, for instance, breaks each side into 10 subintervals,
#    and produces a grid of ((10+1)*(10+2))/2 = 66 points.
#
#              X
#             9 X
#            8 9 X
#           7 8 9 X
#          6 7 8 9 X
#         5 6 7 8 9 X
#        4 5 6 7 8 9 X
#       3 4 5 6 7 8 9 X
#      2 3 4 5 6 7 8 9 X
#     1 2 3 4 5 6 7 8 9 X
#    0 1 2 3 4 5 6 7 8 9 X
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 April 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of subintervals.
#
#    Input, real T[3,2], the coordinates of the points
#    defining the triangle.
#
#    Output, real TG[NG,2], the coordinates
#    of the points in the triangle.
#
  import numpy as np

  ng = ( ( n + 1 ) * ( n + 2 ) ) / 2
  tg = np.zeros ( ( ng, 2 ) )

  p = 0

  for i in range ( 0, n + 1 ):
    for j in range ( 0, n + 1 - i ):

      tg[p,0] = ( float (     i     ) * t[0,0]   \
                + float (         j ) * t[1,0]   \
                + float ( n - i - j ) * t[2,0] ) \
                / float ( n )

      tg[p,1] = ( float (     i     ) * t[0,1]   \
                + float (         j ) * t[1,1]   \
                + float ( n - i - j ) * t[2,1] ) \
                / float ( n )
      p = p + 1

  return tg

def triangle_grid_points_test ( n ):

#*****************************************************************************80
#
## TRIANGLE_GRID_POINTS_TEST tests TRIANGLE_GRID_POINTS.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 April 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  from r82col_print_part import r82col_print_part
  from r8mat_print import r8mat_print
  from r8mat_write import r8mat_write
  from triangle_grid_count import triangle_grid_count
  from triangle_grid_display import triangle_grid_display

  print ''
  print 'TRIANGLE_GRID_POINTS_TEST:'
  print '  TRIANGLE_GRID_POINTS defines a triangular grid'
  print '  with N+1 points on a side, based on any triangle.'

  print ''
  print '  Input value of N is %d' % ( n )

  ng = triangle_grid_count ( n )
  print '  Number of grid points will be %d' % ( ng )

  t = np.array ( [ \
    [ 0.0, 0.0 ], \
    [ 1.0, 0.0 ], \
    [ 0.5, 0.86602540378443860 ] ] )

  r8mat_print ( 3, 2, t, '  Triangle vertices:' )

  tg = triangle_grid_points ( n, t )

  r82col_print_part ( ng, tg, 20, '  Part of the grid point array:' );
#
#  Write the data to a file.
#
  filename = 'triangle_grid_points.xy'

  r8mat_write ( filename, ng, 2, tg )
#
#  Plot the data.
#
  print ''
  print '  Data written to the file "%s".' % ( filename )

  filename = 'triangle_grid_points.png'
  triangle_grid_display ( t, ng, tg, filename )

  print ''
  print 'TRIANGLE_GRID_POINTS_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  triangle_grid_points_test ( 10 )
  timestamp ( )
