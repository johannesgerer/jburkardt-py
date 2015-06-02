#!/usr/bin/env python

def pyramid_grid_test ( ):

#*****************************************************************************80
#
## PYRAMID_GRID_TEST tests the PYRAMIDE_GRID library.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    14 April 2015
#
#  Author:
#
#    John Burkardt
#
  from pyramid_grid_count          import pyramid_grid_count_test
  from pyramid_grid_display        import pyramid_grid_display_test
  from pyramid_grid_points         import pyramid_grid_points_test
  from r83col_print_part           import r83col_print_part_test
  from r8mat_write                 import r8mat_write_test
  from timestamp                   import timestamp_test

  print ''
  print 'PYRAMID_GRID_TEST'
  print '  Python version:'
  print '  Test the PYRAMID_GRID library.'
#
#  Utilities:
#
  r83col_print_part_test ( )
  r8mat_write_test ( )
  timestamp_test ( )
#
#  Library.
#
  pyramid_grid_count_test ( )
  pyramid_grid_display_test ( )
  pyramid_grid_points_test ( )
#
#  Terminate.
#
  print ''
  print 'PYRAMID_GRID_TEST:'
  print '  Normal end of execution.'

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  pyramid_grid_test ( )
  timestamp ( )
