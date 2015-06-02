#!/usr/bin/env python

def square_grid_test ( ):

#*****************************************************************************80
#
## SQUARE_GRID_TEST tests the SQUARE_GRID library.
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
  from square_grid_display         import square_grid_display_test
  from square_grid_points          import square_grid_points_test
  from square_grid_count           import square_grid_count_test
  from r82col_print_part           import r82col_print_part_test
  from r8mat_print                 import r8mat_print_test
  from r8mat_print_some            import r8mat_print_some_test
  from r8mat_write                 import r8mat_write_test
  from timestamp                   import timestamp_test

  print ''
  print 'SQUARE_GRID_TEST'
  print '  Python version:'
  print '  Test the SQUARE_GRID library.'
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
  square_grid_display_test ( )
  square_grid_count_test ( )
  square_grid_points_test ( 10, 8 )
#
#  Terminate.
#
  print ''
  print 'SQUARE_GRID_TEST:'
  print '  Normal end of execution.'

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  square_grid_test ( )
  timestamp ( )
