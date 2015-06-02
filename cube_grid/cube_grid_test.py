#!/usr/bin/env python

def cube_grid_test ( ):

#*****************************************************************************80
#
## CUBE_GRID_TEST tests the CUBEE_GRID library.
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
  from cube_grid_display           import cube_grid_display_test
  from cube_grid_points            import cube_grid_points_test
  from cube_grid_count             import cube_grid_count_test
  from r83col_print_part           import r83col_print_part_test
  from r8mat_write                 import r8mat_write_test
  from timestamp                   import timestamp_test

  print ''
  print 'CUBE_GRID_TEST'
  print '  Python version:'
  print '  Test the CUBE_GRID library.'
#
#  Utilities:
#
  r83col_print_part_test ( )
  r8mat_write_test ( )
  timestamp_test ( )
#
#  Library.
#
  cube_grid_display_test ( )
  cube_grid_count_test ( )
  cube_grid_points_test ( )
#
#  Terminate.
#
  print ''
  print 'CUBE_GRID_TEST:'
  print '  Normal end of execution.'

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  cube_grid_test ( )
  timestamp ( )
