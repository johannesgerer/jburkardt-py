#!/usr/bin/env python

def wathen_test ( ):

#*****************************************************************************80
#
## WATHEN_TEST tests the WATHEN library.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    31 August 2014
#
#  Author:
#
#    John Burkardt
#
  from timestamp import timestamp
  from wathen_test01 import wathen_test01
  from wathen_test02 import wathen_test02
  from wathen_test03 import wathen_test03
  from wathen_test04 import wathen_test04
  from wathen_test05 import wathen_test05
  from wathen_test06 import wathen_test06
  from wathen_test07 import wathen_test07
  from wathen_test08 import wathen_test08
  from wathen_test09 import wathen_test09

  timestamp ( )
  print ''
  print 'WATHEN_TEST'
  print '  Python version:'
  print '  Test the WATHEN library.'
#
#  Direct Solve
#
  wathen_test01 ( )
  wathen_test02 ( )
#
#  Timings.
#
  wathen_test03 ( )
  wathen_test04 ( )
  wathen_test05 ( )
#
#  CG Solve
#
  wathen_test06 ( )
  wathen_test07 ( )
  wathen_test08 ( )
#
#  Use SPY to display the sparsity of the matrix.
#
  wathen_test09 ( )
#
#  Terminate.
#
  print ''
  print 'WATHEN_TEST:'
  print '  Normal end of execution.'
  print ''
  timestamp ( )

  return

if ( __name__ == '__main__' ):
  wathen_test ( )
