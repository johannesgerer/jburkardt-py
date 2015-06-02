#! /usr/bin/env python
#
def disk_grid_fibonacci ( n, r, c ):

#*****************************************************************************80
#
#% DISK_GRID_FIBONACCI computes Fibonacci grid points inside a disk.
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
#  Reference:
#
#    Richard Swinbank, James Purser,
#    Fibonacci grids: A novel approach to global modelling,
#    Quarterly Journal of the Royal Meteorological Society,
#    Volume 132, Number 619, July 2006 Part B, pages 1769-1793.
#
#  Parameters:
#
#    Input, integer N, the number of points desired.
#
#    Input, real R, the radius of the disk.
#
#    Input, real C(2), the coordinates of the center of the disk.
#
#    Output, real CG(2,N), the grid points.
#
  import numpy as np

  r0 = r / np.sqrt ( float ( n ) - 0.5 )
  phi = ( 1.0 + np.sqrt ( 5.0 ) ) / 2.0

  gr = np.zeros ( n )
  gt = np.zeros ( n )
  for i in range ( 0, n ):
    gr[i] = r0 * np.sqrt ( i + 0.5 );
    gt[i] = 2.0 * np.pi * float ( i + 1 ) / phi

  cg = np.zeros ( ( 2, n ) )

  for i in range ( 0, n ):
    cg[0,i] = c[0] + gr[i] * np.cos ( gt[i] )
    cg[1,i] = c[1] + gr[i] * np.sin ( gt[i] )

  return cg

def disk_grid_fibonacci_test ( ):

#*****************************************************************************80
#
#% DISK_GRID_FIBONACCI_TEST tests DISK_GRID_FIBONACCI.
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

  from disk_grid_regular_count import disk_grid_regular_count
  from disk_grid_display import disk_grid_display
  from r82vec_print_part import r82vec_print_part
  from r8mat_transpose_write import r8mat_transpose_write

  print ''
  print 'DISK_GRID_FIBONACCI_TEST:'
  print '  DISK_GRID_FIBONACCI can define a grid of N points'
  print ''

  n = 1000
  r = 2.0
  c = np.array ( [ 1.0, 5.0 ] )

  print ''
  print '  We use N = %d' % ( n )
  print '  Radius R = %g' % ( r )
  print '  Center C = (%g,%g)' % ( c[0], c[1] )

  ng = n
  cg = disk_grid_fibonacci ( n, r, c );

  r82vec_print_part ( n, cg, 20, '  Part of the grid point array:' );
#
#  Write grid points to a file.
#
  filename = 'disk_grid_fibonacci.xy'

  r8mat_transpose_write ( filename, 2, ng, cg )

  print ''
  print '  Data written to the file "%s".' % ( filename )
#
#  Plot the grid, and save the plot in a file.
#
  filename = 'disk_grid_fibonacci.png'
  disk_grid_display ( n, r, c, ng, cg, filename )
#
#  Terminate.
#
  print ''
  print 'DISK_GRID_FIBONACCI_TEST:'
  print '  Normal end of execution.'

  return
  
if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  disk_grid_fibonacci_test ( )
  timestamp ( )
