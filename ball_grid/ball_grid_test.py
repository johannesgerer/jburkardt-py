#!/usr/bin/env python

def ball_grid_test ( ):

#*****************************************************************************80
#
## BALL_GRID_TEST tests the BALLE_GRID library.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    11 April 2015
#
#  Author:
#
#    John Burkardt
#
  from ball_grid_display           import ball_grid_display_test
  from ball_grid_points            import ball_grid_points_test
  from ball_grid_count             import ball_grid_count_test
  from r83col_print_part           import r83col_print_part_test
  from r8mat_write                 import r8mat_write_test
  from timestamp                   import timestamp_test

  print ''
  print 'BALL_GRID_TEST'
  print '  Python version:'
  print '  Test the BALL_GRID library.'
#
#  Utilities:
#
  r83col_print_part_test ( )
  r8mat_write_test ( )
  timestamp_test ( )
#
#  Library.
#
  ball_grid_display_test ( )
  ball_grid_count_test ( )
  ball_grid_points_test ( )
#
#  Terminate.
#
  print ''
  print 'BALL_GRID_TEST:'
  print '  Normal end of execution.'

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  ball_grid_test ( )
  timestamp ( )
