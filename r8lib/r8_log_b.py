#!/usr/bin/env python

def r8_log_b ( x, b ):

#*****************************************************************************80
#
## R8_LOG_B returns the logarithm base B of |X|.
#
#  Discussion:
#
#    value = log ( |X| ) / log ( |B| )
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    07 June 2013
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real X, the number whose base B logarithm is desired.
#    X should not be 0.
#
#    Input, real B, the base, which should not be 0, 1 or -1.
#
#    Output, real VALUE, the logarithm base B of the absolute
#    value of X.  It should be true that |X| = |B|**D_LOG_B.
#
  from math import log

  value = log ( abs ( x ), b )

  return value

def r8_log_b_test ( ):

#*****************************************************************************80
#
## R8_LOG_B_TEST tests R8_LOG_B.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 July 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  test_num = 10

  b_test = np.array ( [ \
    2.0, 3.0, 4.0, 5.0, 6.0, \
    7.0, 8.0, 16.0, 32.0, 256.0 ] )

  x = 16.0

  print ''
  print 'R8_LOG_B_TEST'
  print '  R8_LOG_B computes the logarithm base B.'
  print ''
  print '        X             B             R8_LOG_B'
  print ''

  for test in range ( 0, test_num ):

    b = b_test[test]

    print '  %12f  %12f  %12f' % ( x, b, r8_log_b ( x, b ) )
#
#  Terminate.
#
  print ''
  print 'R8_LOG_B_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8_log_b_test ( )
  timestamp ( )
