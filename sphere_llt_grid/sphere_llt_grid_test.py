#!/usr/bin/env python

def sphere_llt_grid_test ( ):

#*****************************************************************************80
#
## SPHERE_LLT_GRID_TEST tests the SPHERE_LLT_GRID library.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    21 May 2015
#
#  Author:
#
#    John Burkardt
#
  from sphere_llt_grid_display        import sphere_llt_grid_display_test
  from sphere_llt_grid_line_count     import sphere_llt_grid_line_count_test
  from sphere_llt_grid_lines          import sphere_llt_grid_lines_test
  from sphere_llt_grid_point_count    import sphere_llt_grid_point_count_test
  from sphere_llt_grid_points         import sphere_llt_grid_points_test
  from i4mat_print                    import i4mat_print_test
  from i4mat_print_some               import i4mat_print_some_test
  from r8vec_print                    import r8vec_print_test
  from timestamp                      import timestamp_test

  print ''
  print 'SPHERE_LLT_GRID_TEST'
  print '  Python version:'
  print '  Test the SPHERE_LLT_GRID library.'
#
#  Utilities:
#
  i4mat_print_test ( )
  i4mat_print_some_test ( )
  r8vec_print_test ( )
  timestamp_test ( )
#
#  Library.
#
  sphere_llt_grid_point_count_test ( )
  sphere_llt_grid_points_test ( )
  sphere_llt_grid_line_count_test ( )
  sphere_llt_grid_lines_test ( )
  sphere_llt_grid_display_test ( )
#
#  Terminate.
#
  print ''
  print 'SPHERE_LLT_GRID_TEST:'
  print '  Normal end of execution.'

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  sphere_llt_grid_test ( )
  timestamp ( )
