#!/usr/bin/env python

def ellipse_grid_test ( ):

#*****************************************************************************80
#
## ELLIPSE_GRID_TEST tests the ELLIPSE_GRID library.
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
  from ellipse_grid_display      import ellipse_grid_display_test
  from ellipse_grid_points       import ellipse_grid_points_test
  from ellipse_grid_count        import ellipse_grid_count_test
  from r82vec_print_part         import r82vec_print_part_test
  from r8mat_transpose_write     import r8mat_transpose_write_test
  from timestamp                 import timestamp_test

  print ''
  print 'ELLIPSE_GRID_TEST'
  print '  Python version:'
  print '  Test the ELLIPSE_GRID library.'
#
#  Utilities:
#
  r82vec_print_part_test ( )
  r8mat_transpose_write_test ( )
  timestamp_test ( )
#
#  Library.
#
  ellipse_grid_display_test ( )
  ellipse_grid_count_test ( )
  ellipse_grid_points_test ( )
#
#  Terminate.
#
  print ''
  print 'ELLIPSE_GRID_TEST:'
  print '  Normal end of execution.'

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  ellipse_grid_test ( )
  timestamp ( )
