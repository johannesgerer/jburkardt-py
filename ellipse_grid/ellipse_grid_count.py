#! /usr/bin/env python
#
def ellipse_grid_count ( n, r, c ):

#*****************************************************************************80
#
## ELLIPSE_GRID_COUNT counts the grid points inside an ellipse.
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
#    Output, integer NG, the number of grid points inside the ellipse.
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

  ng = 0

  for j in range ( 0, nj + 1 ):
    i = 0
    x = c[0]
    y = c[1] + float ( j ) * h
    ng = ng + 1
    if ( 0 < j ):
      ng = ng + 1

    while ( True ):
      i = i + 1
      x = c[0] + float ( i ) * h
      if ( 1 < ( ( x - c[0] ) / r[0] ) ** 2 + ( ( y - c[1] ) / r[1] ) ** 2 ):
        break
      ng = ng + 1
      ng = ng + 1
      if ( 0 < j ):
        ng = ng + 1
        ng = ng + 1

  return ng

def ellipse_grid_count_test ( ):

#*****************************************************************************80
#
## ELLIPSE_GRID_COUNT_TEST tests ELLIPSE_GRID_COUNT.
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

  print ''
  print 'ELLIPSE_GRID_COUNT_TEST:'
  print '  ELLIPSE_GRID_COUNT can count the points in a grid,'
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

  print ''
  print 'ELLIPSE_GRID_COUNT_TEST:'
  print '  Normal end of execution.'

  return
  
if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  ellipse_grid_count_test ( )
  timestamp ( )
