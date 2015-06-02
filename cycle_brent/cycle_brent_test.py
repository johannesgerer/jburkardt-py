#!/usr/bin/env python

def cycle_brent_test ( ):

#*****************************************************************************80
#
## CYCLE_BRENT_TEST tests the CYCLE_BRENT library.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 May 2013
#
#  Author:
#
#    John Burkardt
#
  from cycle_brent_test01 import cycle_brent_test01
  from cycle_brent_test02 import cycle_brent_test02
  from cycle_brent_test03 import cycle_brent_test03
  from cycle_brent_test04 import cycle_brent_test04
  from cycle_brent_test05 import cycle_brent_test05

  print 'CYCLE_BRENT_TEST'
  print '  Python version'
  print '  Test the CYCLE_BRENT library.'

  cycle_brent_test01 ( )
  cycle_brent_test02 ( )
  cycle_brent_test03 ( )
  cycle_brent_test04 ( )
  cycle_brent_test05 ( )
#
#  Terminate.
#
  print
  print 'CYCLE_BRENT_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  cycle_brent_test ( )
  timestamp ( )
