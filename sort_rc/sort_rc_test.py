#!/usr/bin/env python

def sort_rc_test ( ):

#*****************************************************************************80
#
## SORT_RC_TEST tests the SORT_RC library.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    11 March 2015
#
#  Author:
#
#    John Burkardt
#
  from i4vec_print         import i4vec_print_test
  from i4vec_uniform_ab    import i4vec_uniform_ab_test
  from sort_safe_rc        import sort_safe_rc_i4vec_test
  from timestamp           import timestamp_test

  print ''
  print 'SORT_RC_TEST'
  print '  Python version:'
  print '  Test the SORT_RC library.'

  i4vec_print_test ( )
  i4vec_uniform_ab_test ( )
  sort_safe_rc_i4vec_test ( )
  timestamp_test ( )
#
#  Terminate.
#
  print ''
  print 'SORT_RC_TEST:'
  print '  Normal end of execution.'

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  sort_rc_test ( )
  timestamp ( )
