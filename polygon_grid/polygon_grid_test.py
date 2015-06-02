def polygon_grid_test ( ):

#*****************************************************************************80
#
## POLYGON_GRID_TEST tests the POLYGON_GRID library.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 May 2015
#
#  Author:
#
#    John Burkardt
#
  from polygon_grid_count    import polygon_grid_count_test
  from polygon_grid_display  import polygon_grid_display_test
  from polygon_grid_points   import polygon_grid_points_test01
  from polygon_grid_points   import polygon_grid_points_test02
  from polygon_grid_points   import polygon_grid_points_test03
  from r8mat_print           import r8mat_print_test
  from r8mat_print_some      import r8mat_print_some_test
  from r8mat_write           import r8mat_write_test

  print ''
  print 'POLYGON_GRID_TEST:'
  print '  Python version'
  print '  Test the POLYGON_GRID library.'
#
#  Utilities.
#
  r8mat_print_test ( )
  r8mat_print_some_test ( )
  r8mat_write_test ( )
#
#  Library.
#
  polygon_grid_count_test ( )

  polygon_grid_display_test ( )

  polygon_grid_points_test01 ( )
  polygon_grid_points_test02 ( )
  polygon_grid_points_test03 ( )
#
#  Terminate.
#
  print ''
  print 'POLYGON_GRID_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  polygon_grid_test ( )
  timestamp ( )
