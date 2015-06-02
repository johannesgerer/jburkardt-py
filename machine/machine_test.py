#!/usr/bin/env python
#
def machine_test ( ):

#*****************************************************************************80
#
## MACHINE_TEST tests the MACHINE library.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    04 April 2015
#
#  Author:
#
#    John Burkardt
#
  from d1mach    import d1mach_test
  from i1mach    import i1mach_test
  from r1mach    import r1mach_test
  from timestamp import timestamp

  timestamp ( )
  print ''
  print 'MACHINE_TEST:'
  print '  Python version'
  print '  Test the MACHINE library.'

  d1mach_test ( )
  i1mach_test ( )
  r1mach_test ( )
#
#  Terminate.
#
  print ''
  print 'MACHINE_TEST:'
  print '  Normal end of execution.'
  print ''
  timestamp ( )

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  machine_test ( )
  timestamp ( )
