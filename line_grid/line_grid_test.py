#!/usr/bin/env python

def line_grid_test ( ):

#*****************************************************************************80
#
## LINE_GRID_TEST tests the LINE_GRID library.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    24 April 2015
#
#  Author:
#
#    John Burkardt
#
  from line_grid                    import line_grid_test01
  from line_grid                    import line_grid_test02
  from line_grid                    import line_grid_test03
  from r8vec_print                  import r8vec_print_test
  from timestamp                    import timestamp_test

  print ''
  print 'LINE_GRID_TEST'
  print '  Python version:'
  print '  Test the LINE_GRID library.'
#
#  Utilities:
#
  r8vec_print_test ( )
  timestamp_test ( )
#
#  Library.
#
  line_grid_test01 ( )
  line_grid_test02 ( )
  line_grid_test03 ( )
#
#  Terminate.
#
  print ''
  print 'LINE_GRID_TEST:'
  print '  Normal end of execution.'

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  line_grid_test ( )
  timestamp ( )
