#!/usr/bin/env python

def normal_test ( ):

#*****************************************************************************80
#
## NORMAL_TEST tests the NORMAL library.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    04 March 2015
#
#  Author:
#
#    John Burkardt
#
  from c8_normal_01      import c8_normal_01_test
  from i4_normal_ab      import i4_normal_ab_test
  from r8_normal_01      import r8_normal_01_test
  from r8_normal_ab      import r8_normal_ab_test
  from r8_uniform_01     import r8_uniform_01_test
  from r8mat_normal_01   import r8mat_normal_01_test
  from r8mat_normal_ab   import r8mat_normal_ab_test
  from r8mat_print       import r8mat_print_test
  from r8mat_print_some  import r8mat_print_some_test
  from r8vec_normal_01   import r8vec_normal_01_test
  from r8vec_normal_ab   import r8vec_normal_ab_test
  from r8vec_print       import r8vec_print_test
  from r8vec_uniform_01  import r8vec_uniform_01_test
  from timestamp         import timestamp_test
#
#  Utilities:
#
  r8_uniform_01_test ( )
  r8mat_print_test ( )
  r8mat_print_some_test ( )
  r8vec_print_test ( )
  r8vec_uniform_01_test ( )
  timestamp_test ( )
#
#  Libraries:
#
  c8_normal_01_test ( )
  i4_normal_ab_test ( )
  r8_normal_01_test ( )
  r8_normal_ab_test ( )
  r8mat_normal_01_test ( )
  r8mat_normal_ab_test ( )
  r8vec_normal_01_test ( )
  r8vec_normal_ab_test ( )
#
#  Terminate.
#
  print ''
  print 'NORMAL_TEST:'
  print '  Normal end of execution.'

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  normal_test ( )
  timestamp ( )
