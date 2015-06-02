#! /usr/bin/env python
#
def fd1d_heat_implicit_test ( ):

#*****************************************************************************80
#
## FD1D_HEAT_IMPLICIT_TEST tests the FD1D_HEAT_IMPLICIT library.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    17 November 2014
#
#  Author:
#
#    John Burkardt
#
  from fd1d_heat_implicit_test01 import fd1d_heat_implicit_test01
  from fd1d_heat_implicit_test02 import fd1d_heat_implicit_test02
  from fd1d_heat_implicit_test03 import fd1d_heat_implicit_test03

  print ''
  print 'FD1D_HEAT_IMPLICIT_TEST:'
  print '  Python version.'
  print '  Test the FD1D_HEAT_IMPLICIT library.'

  fd1d_heat_implicit_test01 ( )
  fd1d_heat_implicit_test02 ( )
  fd1d_heat_implicit_test03 ( )
#
#  Terminate.
#
  print ''
  print 'FD1D_HEAT_IMPLICIT_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  fd1d_heat_implicit_test ( )
  timestamp ( )
