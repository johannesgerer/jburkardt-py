#! /usr/bin/env python
#
def grid_2d ( x_num, x_lo, x_hi, y_num, y_lo, y_hi ):

#*****************************************************************************80
#
## GRID_2D returns a regular 2D grid.
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
#  Parameters:
#
#    Input, integer X_NUM, the number of X values to use.
#
#    Input, real X_LO, X_HI, the range of X values.
#
#    Input, integer Y_NUM, the number of Y values to use.
#
#    Input, real Y_LO, Y_HI, the range of Y values.
#
#    Output, real X(X_NUM*Y_NUM), Y(X_NUM*Y_NUM), the coordinates of the grid.
#
  import numpy as np

  x = np.zeros ( x_num * y_num )
  y = np.zeros ( x_num * y_num )

  if ( x_num == 1 ):
    xi = ( x_lo + x_hi ) / 2.0
    k = 0
    for j in range ( 0, y_num ):
      for i in range ( 0, x_num ):
        x[k] = xi
        k = k + 1
  else:
    k = 0
    for j in range ( 0, y_num ):
      for i in range ( 0, x_num ):
        xi = ( float ( x_num - i - 1 ) * x_lo   \
             + float (         i     ) * x_hi ) \
             / float ( x_num     - 1 )
        x[k] = xi
        k = k + 1

  if ( y_num == 1 ):
    yj = ( y_lo + y_hi ) / 2.0
    k = 0
    for j in range ( 0, y_num ):
      for i in range ( 0, x_num ):
        y[k] = yj
        k = k + 1
  else:
    k = 0
    for j in range ( 0, y_num ):
      yj = ( float ( y_num - j - 1 ) * y_lo   \
           + float (         j     ) * y_hi ) \
           / float ( y_num     - 1 )
      for i in range ( 0, x_num ):
        y[k] = yj
        k = k + 1

  return x, y

def grid_2d_test ( ):

#*****************************************************************************80
#
## GRID_2D_TEST makes a small 2D grid.
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
  print ''
  print 'GRID_2D_TEST:'
  print '  Generate a regular grid.'

  x_lo = 10.0
  x_hi = 20.0
  x_num = 5

  y_lo = 5.0
  y_hi = 6.0
  y_num = 3

  [ x, y ] = grid_2d ( x_num, x_lo, x_hi, y_num, y_lo, y_hi )

  print ''
  k = 0
  for j in range ( 0, y_num ):
    for i in range ( 0, x_num):
      print '  %2d  %2d  %2d  %14.6f  %14.6f' % ( k, i, j, x[k], y[k] )
      k = k + 1

  print ''
  print 'GRID_2D_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  grid_2d_test ( )
  timestamp ( )

