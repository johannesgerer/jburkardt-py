#!/usr/bin/env python

def circle_arc_grid_test ( ):

#*****************************************************************************80
#
## CIRCLE_ARC_GRID_TEST tests the CIRCLE_ARCE_GRID library.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    17 April 2015
#
#  Author:
#
#    John Burkardt
#
  from circle_arc_grid_display     import circle_arc_grid_display_test
  from circle_arc_grid_points      import circle_arc_grid_points_test
  from r82col_print_part           import r82col_print_part_test
  from r8mat_write                 import r8mat_write_test
  from timestamp                   import timestamp_test

  print ''
  print 'CIRCLE_ARC_GRID_TEST'
  print '  Python version:'
  print '  Test the CIRCLE_ARC_GRID library.'
#
#  Utilities:
#
  r82col_print_part_test ( )
  r8mat_write_test ( )
  timestamp_test ( )
#
#  Library.
#
  circle_arc_grid_display_test ( )
  circle_arc_grid_points_test ( )
#
#  Terminate.
#
  print ''
  print 'CIRCLE_ARC_GRID_TEST:'
  print '  Normal end of execution.'

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  circle_arc_grid_test ( )
  timestamp ( )
