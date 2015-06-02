#!/usr/bin/env python

def tetrahedron_grid_test ( ):

#*****************************************************************************80
#
## TETRAHEDRON_GRID_TEST tests the TETRAHEDRONE_GRID library.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    15 April 2015
#
#  Author:
#
#    John Burkardt
#

  from r83col_print_part           import r83col_print_part_test
  from r8mat_write                 import r8mat_write_test
  from tetrahedron_grid_count      import tetrahedron_grid_count_test
  from tetrahedron_grid_display    import tetrahedron_grid_display_test
  from tetrahedron_grid_points     import tetrahedron_grid_points_test
  from timestamp                   import timestamp_test

  print ''
  print 'TETRAHEDRON_GRID_TEST'
  print '  Python version:'
  print '  Test the TETRAHEDRON_GRID library.'
#
#  Utilities:
#
  r83col_print_part_test ( )
  r8mat_write_test ( )
  timestamp_test ( )
#
#  Library.
#
  tetrahedron_grid_count_test ( )
  tetrahedron_grid_display_test ( )
  tetrahedron_grid_points_test ( )
#
#  Terminate.
#
  print ''
  print 'TETRAHEDRON_GRID_TEST:'
  print '  Normal end of execution.'

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  tetrahedron_grid_test ( )
  timestamp ( )
