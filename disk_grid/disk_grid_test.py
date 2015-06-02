#!/usr/bin/env python

def disk_grid_test ( ):

#*****************************************************************************80
#
## DISK_GRID_TEST tests the DISK_GRID library.
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
  from disk_grid_display         import disk_grid_display_test
  from disk_grid_fibonacci       import disk_grid_fibonacci_test
  from disk_grid_regular         import disk_grid_regular_test
  from disk_grid_regular_count   import disk_grid_regular_count_test
  from r82vec_print_part         import r82vec_print_part_test
  from r8mat_transpose_write     import r8mat_transpose_write_test
  from timestamp                 import timestamp_test

  print ''
  print 'DISK_GRID_TEST'
  print '  Python version:'
  print '  Test the DISK_GRID library.'
#
#  Utilities:
#
  r82vec_print_part_test ( )
  r8mat_transpose_write_test ( )
  timestamp_test ( )
#
#  Library.
#
  disk_grid_display_test ( )
  disk_grid_regular_count_test ( )
  disk_grid_regular_test ( )
  disk_grid_fibonacci_test ( )
#
#  Terminate.
#
  print ''
  print 'DISK_GRID_TEST:'
  print '  Normal end of execution.'

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  disk_grid_test ( )
  timestamp ( )
