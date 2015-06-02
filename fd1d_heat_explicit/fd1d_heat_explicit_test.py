#!/usr/bin/env python

#*****************************************************************************80

def fd1d_heat_explicit_test ( ):

#*****************************************************************************80
#
## FD1D_HEAT_EXPLICIT_TEST tests the FD1D_HEAT_EXPLICIT library.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    06 November 2014
#
#  Author:
#
#    John Burkardt
#
  from fd1d_heat_explicit_test01 import fd1d_heat_explicit_test01 
  from fd1d_heat_explicit_test02 import fd1d_heat_explicit_test02
  from fd1d_heat_explicit_test03 import fd1d_heat_explicit_test03

  print ''
  print 'FD1D_HEAT_EXPLICIT_TEST:'
  print '  Python version.'
  print '  Test the FD1D_HEAT_EXPLICIT library.'

  fd1d_heat_explicit_test01 ( )
  fd1d_heat_explicit_test02 ( )
  fd1d_heat_explicit_test03 ( )
#
#  Terminate.
#
  print ''
  print 'FD1D_HEAT_EXPLICIT_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  fd1d_heat_explicit_test ( )
  timestamp ( )

