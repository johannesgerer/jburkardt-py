#!/usr/bin/env python

def hypercube_grid_test ( ):

#*****************************************************************************80
#
## HYPERCUBE_GRID_TEST tests the HYPERCUBE_GRID library.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    20 April 2015
#
#  Author:
#
#    John Burkardt
#
  from hypercube_grid_points       import hypercube_grid_points_test01
  from hypercube_grid_points       import hypercube_grid_points_test02
  from hypercube_grid_points       import hypercube_grid_points_test03
  from r8mat_print                 import r8mat_print_test
  from r8mat_print_some            import r8mat_print_some_test
  from r8mat_write                 import r8mat_write_test
  from timestamp                   import timestamp_test

  print ''
  print 'HYPERCUBE_GRID_TEST'
  print '  Python version:'
  print '  Test the HYPERCUBE_GRID library.'
#
#  Utilities:
#
  r8mat_print_test ( )
  r8mat_print_some_test ( )
  r8mat_write_test ( )
  timestamp_test ( )
#
#  Library.
#
  hypercube_grid_points_test01 ( )
  hypercube_grid_points_test02 ( )
  hypercube_grid_points_test03 ( )
#
#  Terminate.
#
  print ''
  print 'HYPERCUBE_GRID_TEST:'
  print '  Normal end of execution.'

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  hypercube_grid_test ( )
  timestamp ( )
