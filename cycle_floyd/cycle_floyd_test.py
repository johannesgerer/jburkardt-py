#! /usr/bin/env python

def cycle_floyd_test ( ):

#*****************************************************************************80
#
## CYCLE_FLOYD_TEST tests the CYCLE_FLOYD library.
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
  from cycle_floyd_test01 import cycle_floyd_test01
  from cycle_floyd_test02 import cycle_floyd_test02
  from cycle_floyd_test03 import cycle_floyd_test03
  from cycle_floyd_test04 import cycle_floyd_test04
  from cycle_floyd_test05 import cycle_floyd_test05

  print ''
  print 'CYCLE_FLOYD_TEST'
  print '  MATLAB version'
  print '  Test the CYCLE_FLOYD library.'

  cycle_floyd_test01 ( )
  cycle_floyd_test02 ( )
  cycle_floyd_test03 ( )
  cycle_floyd_test04 ( )
  cycle_floyd_test05 ( )
#
#  Terminate.
#
  print ''
  print 'CYCLE_FLOYD_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  cycle_floyd_test ( )
  timestamp ( )

