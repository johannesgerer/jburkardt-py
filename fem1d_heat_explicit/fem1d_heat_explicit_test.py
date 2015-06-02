#!/usr/bin/env python

#*****************************************************************************80

def fem1d_heat_explicit_test ( ):

#*****************************************************************************80
#
## FEM1D_HEAT_EXPLICIT_TEST tests the FEM1D_HEAT_EXPLICIT library.
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
  from fem1d_heat_explicit_test01 import fem1d_heat_explicit_test01 
  from fem1d_heat_explicit_test02 import fem1d_heat_explicit_test02
  from fem1d_heat_explicit_test03 import fem1d_heat_explicit_test03

  print ''
  print 'FEM1D_HEAT_EXPLICIT_TEST'
  print '  Python version.'
  print '  Test the FEM1D_HEAT_EXPLICIT library.'

  fem1d_heat_explicit_test01 ( )
  fem1d_heat_explicit_test02 ( )
  fem1d_heat_explicit_test03 ( )
#
#  Terminate.
#
  print ''
  print 'FEM1D_HEAT_EXPLICIT_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  fem1d_heat_explicit_test ( )
  timestamp ( )





