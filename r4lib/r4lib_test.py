#!/usr/bin/env python

def r4lib_test ( ):

#*****************************************************************************80
#
## R4LIB_TEST tests the R4LIB library.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    25 December 2014
#
#  Author:
#
#    John Burkardt
#

  from r4mat_print                import r4mat_print_test
  from r4mat_print_some           import r4mat_print_some_test

  from r4vec_print                import r4vec_print_test

  from timestamp                  import timestamp_test

  print ''
  print 'R4LIB_TEST'
  print '  Python version:'
  print '  Test the R4LIB library.'

  r4mat_print_test ( )
  r4mat_print_some_test ( )

  r4vec_print_test ( )

  timestamp_test ( )
#
#  Terminate.
#
  print ''
  print 'R4LIB_TEST:'
  print '  Normal end of execution.'

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r4lib_test ( )
  timestamp ( )
