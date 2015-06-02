#!/usr/bin/env python

def triangle_grid_test ( ):

#*****************************************************************************80
#
## TRIANGLE_GRID_TEST tests the TRIANGLE_GRID library.
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
  from triangle_grid_display     import triangle_grid_display_test
  from triangle_grid_points      import triangle_grid_points_test
  from triangle_grid_count       import triangle_grid_count_test
  from r82col_print_part         import r82col_print_part_test
  from r8mat_print               import r8mat_print_test
  from r8mat_print_some          import r8mat_print_some_test
  from r8mat_write               import r8mat_write_test
  from timestamp                 import timestamp_test

  print ''
  print 'TRIANGLE_GRID_TEST'
  print '  Python version:'
  print '  Test the TRIANGLE_GRID library.'
#
#  Utilities:
#
  r82col_print_part_test ( )
  r8mat_print_test ( )
  r8mat_print_some_test ( )
  r8mat_write_test ( )
  timestamp_test ( )
#
#  Library.
#
  triangle_grid_display_test ( )
  triangle_grid_count_test ( )
  triangle_grid_points_test ( 15 )
#
#  Terminate.
#
  print ''
  print 'TRIANGLE_GRID_TEST:'
  print '  Normal end of execution.'

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  triangle_grid_test ( )
  timestamp ( )
