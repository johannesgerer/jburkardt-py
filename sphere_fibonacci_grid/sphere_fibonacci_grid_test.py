#!/usr/bin/env python

def sphere_fibonacci_grid_test ( ):

#*****************************************************************************80
#
## SPHERE_FIBONACCI_GRID_TEST tests the SPHERE_FIBONACCI_GRID library.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    15 May 2015
#
#  Author:
#
#    John Burkardt
#
  from sphere_fibonacci_grid_display  import sphere_fibonacci_grid_display_test
  from sphere_fibonacci_grid_points   import sphere_fibonacci_grid_points_test
  from r8mat_print                    import r8mat_print_test
  from r8mat_print_some               import r8mat_print_some_test
  from r8mat_write                    import r8mat_write_test
  from timestamp                      import timestamp_test

  print ''
  print 'SPHERE_FIBONACCI_GRID_TEST'
  print '  Python version:'
  print '  Test the SPHERE_FIBONACCI_GRID library.'
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
  sphere_fibonacci_grid_points_test ( )
  sphere_fibonacci_grid_display_test ( )
#
#  Terminate.
#
  print ''
  print 'SPHERE_FIBONACCI_GRID_TEST:'
  print '  Normal end of execution.'

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  sphere_fibonacci_grid_test ( )
  timestamp ( )
