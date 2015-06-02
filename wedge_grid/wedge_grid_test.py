#!/usr/bin/env python

def wedge_grid_test ( ):

#*****************************************************************************80
#
## WEDGE_GRID_TEST tests the WEDGEE_GRID library.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    16 April 2015
#
#  Author:
#
#    John Burkardt
#
  from wedge_grid_count            import wedge_grid_count_test
  from wedge_grid_display          import wedge_grid_display_test
  from wedge_grid_points           import wedge_grid_points_test
  from r83col_print_part           import r83col_print_part_test
  from r8mat_write                 import r8mat_write_test
  from timestamp                   import timestamp_test

  print ''
  print 'WEDGE_GRID_TEST'
  print '  Python version:'
  print '  Test the WEDGE_GRID library.'
#
#  Utilities:
#
  r83col_print_part_test ( )
  r8mat_write_test ( )
  timestamp_test ( )
#
#  Library.
#
  wedge_grid_count_test ( )
  wedge_grid_display_test ( )
  wedge_grid_points_test ( )
#
#  Terminate.
#
  print ''
  print 'WEDGE_GRID_TEST:'
  print '  Normal end of execution.'

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  wedge_grid_test ( )
  timestamp ( )
