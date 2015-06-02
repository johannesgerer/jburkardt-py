#! /usr/bin/env python
#
def simplex_grid_count ( m, n ):

#*****************************************************************************80
#
## SIMPLEX_GRID_COUNT counts the grid points inside a simplex.
#
#  Discussion:
#
#    The size of a grid with parameters M, N is C(M+N,N).
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    21 April 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, the spatial dimension.
#
#    Input, integer N, the number of subintervals.
#
#    Output, integer NG, the number of grid points.
#
  ng = 1
  for i in range ( 1, m + 1 ):
    ng = ( ng * ( n + i ) ) / i

  return ng

def simplex_grid_count_test ( ):

#*****************************************************************************80
#
## SIMPLEX_GRID_COUNT_TEST tests SIMPLEX_GRID_COUNT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    21 April 2015
#
#  Author:
#
#    John Burkardt
#
  print ''
  print 'SIMPLEX_GRID_COUNT_TEST:'
  print '  SIMPLEX_GRID_COUNT counts the points in a regular grid'
  print '  with N+1 points on a side, in an M-dimensional simplex.'
  print ''
  print '        M:  0      1      2      3      4      5'
  print '    N:'
  for n in range ( 0, 11 ):
    print '  %3d:' % ( n ),
    for m in range ( 0, 6 ):
      print '%6d' % ( simplex_grid_count ( m, n ) ),
    print ''
#
#  Terminate.
#
  print ''
  print 'SIMPLEX_GRID_COUNT_TEST:'
  print '  Normal end of execution.'

  return
  
if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  simplex_grid_count_test ( )
  timestamp ( )
