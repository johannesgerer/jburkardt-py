#!/usr/bin/env python

def cpv_test ( ):

#*****************************************************************************80
#
## CPV_TEST tests the CPV library.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    02 April 2015
#
#  Author:
#
#    John Burkardt
#
  from cpv           import cpv_test01
  from cpv           import cpv_test02
  from legendre_set  import legendre_set_test01
  from timestamp     import timestamp_test

  print ''
  print 'CPV_TEST'
  print '  Python version:'
  print '  Test the CPV library.'

  cpv_test01 ( )
  cpv_test02 ( )

  legendre_set_test01 ( )

  timestamp_test ( )
#
#  Terminate.
#
  print ''
  print 'CPV_TEST:'
  print '  Normal end of execution.'

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  cpv_test ( )
  timestamp ( )
