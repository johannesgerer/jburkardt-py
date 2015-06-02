#!/usr/bin/env python

def c4lib_test ( ):

#*****************************************************************************80
#
## C4LIB_TEST tests the C4LIB library.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    06 December 2014
#
#  Author:
#
#    John Burkardt
#
  from c4_uniform_01              import c4_uniform_01_test
  from c4mat_print                import c4mat_print_test
  from c4mat_print_some           import c4mat_print_some_test
  from c4mat_uniform_01           import c4mat_uniform_01_test

  from c4vec_print                import c4vec_print_test
  from c4vec_uniform_01           import c4vec_uniform_01_test

  from timestamp                  import timestamp_test

  print ''
  print 'C4LIB_TEST'
  print '  Python version:'
  print '  Test the C4LIB library.'

  c4_uniform_01_test ( )
  c4mat_print_test ( )
  c4mat_print_some_test ( )
  c4mat_uniform_01_test ( )
  c4vec_print_test ( )
  c4vec_uniform_01_test ( )

  timestamp_test ( )
#
#  Terminate.
#
  print ''
  print 'C4LIB_TEST:'
  print '  Normal end of execution.'

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  c4lib_test ( )
  timestamp ( )
