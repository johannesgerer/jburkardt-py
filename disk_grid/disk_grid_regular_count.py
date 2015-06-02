#! /usr/bin/env python
#
def disk_grid_regular_count ( n, r, c ):

#*****************************************************************************80
#
#% DISK_GRID_REGULAR_COUNT counts the grid points inside a disk.
#
#  Discussion:
#
#    The grid is defined by specifying the radius and center of the disk,
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
#    07 April 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of subintervals.
#
#    Input, real R, the radius of the disk.
#
#    Input, real C(2), the coordinates of the center of the disk.
#
#    Output, integer NG, the number of grid points inside the disk.
#
  ng = 0

  for j in range ( 0, n + 1 ):

    i = 0
    x = c[0]
    y = c[1] + r * float ( 2 * j ) / float ( 2 * n + 1 )
    ng = ng + 1
    if ( 0 < j ):
      ng = ng + 1

    while ( True ):

      i = i + 1
      x = c[0] + r * float ( 2 * i ) / float ( 2 * n + 1 )

      if ( r * r < ( x - c[0] ) ** 2 + ( y - c[1] ) ** 2 ):
        break

      ng = ng + 1
      ng = ng + 1

      if ( 0 < j ):
        ng = ng + 1
        ng = ng + 1

  return ng

def disk_grid_regular_count_test ( ):

#*****************************************************************************80
#
## DISK_GRID_REGULAR_COUNT counts the grid points inside a disk.
#
#  Discussion:
#
#    The grid is defined by specifying the radius and center of the disk,
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
#    07 April 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ''
  print 'DISK_GRID_REGULAR_COUNT_TEST:'
  print '  DISK_GRID_REGULAR_COUNT counts the number of grid points needed'
  print '  for a regular grid of points in a disk.'

  print ''
  print '  N = number of subintervals of the horizontal radius.'
  print '  NG = resulting number of grid points.'
  print ''
  print '     N        NG'
  print ''

  for n in [ 1, 2, 4, 8, 16  ]:
    r = 1.0
    c = np.array ( [ 0.0, 0.0 ] )
    ng = disk_grid_regular_count ( n, r, c )
    print '  %4d  %8d' % ( n, ng )

  print ''
  print 'DISK_GRID_REGULAR_COUNT_TEST:'
  print '  Normal end of execution.'

  return
  
if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  disk_grid_regular_count_test ( )
  timestamp ( )
