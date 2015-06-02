#!/usr/bin/env python

def rnglib_test ( ):

#*****************************************************************************80
#
## MAIN is the main program for RNGLIB_TEST.
#
#  Discussion:
#
#    RNGLIB_TEST calls sample problems for the RNGLIB library.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    27 May 2013
#
#  Author:
#
#    John Burkardt
#
  from timestamp import timestamp
  from rnglib_test01 import rnglib_test01
  from rnglib_test02 import rnglib_test02
  from rnglib_test03 import rnglib_test03
  from rnglib_test04 import rnglib_test04

  timestamp ( )

  print ''
  print 'RNGLIB_TEST'
  print '  PYTHON version'
  print '  Test the RNGLIB library.'
#
#  Call tests.
#
  rnglib_test01 ( )
  rnglib_test02 ( )
  rnglib_test03 ( )
  rnglib_test04 ( )
#
#  Terminate.
#
  print ''
  print 'RNGLIB_TEST'
  print '  Normal end of execution.'
  print ''
  timestamp ( )

if ( __name__ == '__main__' ):
  rnglib_test ( )
