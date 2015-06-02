#! /usr/bin/env python
#
def fem1d_bvp_linear_test ( ):

#*****************************************************************************80
#
## FEM1D_BVP_LINEAR_TEST tests the FEM1D_BVP_LINEAR library.
#
#  Location:
#
#    http://people.sc.fsu.edu/~jburkardt/py_src/fem1d_bvp_linear/fem1d_bvp_linear_test.py
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 January 2015
#
#  Author:
#
#    John Burkardt
#
  from fem1d_bvp_linear         import fem1d_bvp_linear_test
  from fem1d_bvp_linear_test01  import fem1d_bvp_linear_test01
  from fem1d_bvp_linear_test02  import fem1d_bvp_linear_test02
  from fem1d_bvp_linear_test03  import fem1d_bvp_linear_test03
  from fem1d_bvp_linear_test04  import fem1d_bvp_linear_test04
  from fem1d_bvp_linear_test05  import fem1d_bvp_linear_test05
  from fem1d_bvp_linear_test06  import fem1d_bvp_linear_test06
  from fem1d_bvp_linear_test07  import fem1d_bvp_linear_test07
  from fem1d_bvp_linear_test08  import fem1d_bvp_linear_test08
  from fem1d_bvp_linear_test09  import fem1d_bvp_linear_test09
  from h1s_error_linear         import h1s_error_linear_test
  from l1_error                 import l1_error_test
  from l2_error_linear          import l2_error_linear_test

  print ''
  print 'FEM1D_BVP_LINEAR_TEST'
  print '  Python version'
  print '  Test the FEM1D_BVP_LINEAR library.'

  h1s_error_linear_test ( )
  l1_error_test ( )
  l2_error_linear_test ( )

  fem1d_bvp_linear_test ( )
  fem1d_bvp_linear_test01 ( )
  fem1d_bvp_linear_test02 ( )
  fem1d_bvp_linear_test03 ( )
  fem1d_bvp_linear_test04 ( )
  fem1d_bvp_linear_test05 ( )
  fem1d_bvp_linear_test06 ( )
  fem1d_bvp_linear_test07 ( )
  fem1d_bvp_linear_test08 ( )
  fem1d_bvp_linear_test09 ( )
#
#  Terminate.
#
  print ''
  print 'FEM1D_BVP_LINEAR_TEST:'
  print '  Normal end of execution.'

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  fem1d_bvp_linear_test ( )
  timestamp ( )
