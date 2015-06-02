#!/usr/bin/env python

def ellipsoid_grid_test ( ):

#*****************************************************************************80
#
## ELLIPSOID_GRID_TEST tests the ELLIPSOIDE_GRID library.
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
  from ellipsoid_grid_count        import ellipsoid_grid_count_test
  from ellipsoid_grid_display      import ellipsoid_grid_display_test
  from ellipsoid_grid_points       import ellipsoid_grid_points_test
  from r83col_print_part           import r83col_print_part_test
  from r8mat_write                 import r8mat_write_test
  from timestamp                   import timestamp_test

  print ''
  print 'ELLIPSOID_GRID_TEST'
  print '  Python version:'
  print '  Test the ELLIPSOID_GRID library.'
#
#  Utilities:
#
  r83col_print_part_test ( )
  r8mat_write_test ( )
  timestamp_test ( )
#
#  Library.
#
  ellipsoid_grid_count_test ( )
  ellipsoid_grid_display_test ( )
  ellipsoid_grid_points_test ( )
#
#  Terminate.
#
  print ''
  print 'ELLIPSOID_GRID_TEST:'
  print '  Normal end of execution.'

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  ellipsoid_grid_test ( )
  timestamp ( )
