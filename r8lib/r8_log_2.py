#!/usr/bin/env python

def r8_log_2 ( x ):

#*****************************************************************************80
#
## R8_LOG_2 returns the logarithm base 2 of |X|.
#
#  Discussion:
#
#    R8_LOG_2 ( X ) = Log ( |X| ) / Log ( 2.0 )
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    24 July 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real X, the number whose base 2 logarithm is desired.
#    X should not be 0.
#
#    Output, real VALUE, the logarithm base 2 of the absolute
#    value of X.  It should be true that |X| = 2**R8_LOG_2.
#
  from math import log

  if ( x == 0 ):
    value = float ( '-inf' )
  else:
    value = log ( abs ( x ) ) / log ( 2.0 )

  return value

def r8_log_2_test ( ):

#*****************************************************************************80
#
## R8_LOG_2_TEST tests R8_LOG_2.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 July 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  test_num = 18

  x_test = np.array ( [ \
    0.0,  1.0,  2.0,   3.0,  9.0, \
   10.0, 11.0, 99.0, 101.0, -1.0, \
   -2.0, -3.0, -9.0,   0.5,  0.33, \
    0.25, 0.20, 0.01 ] )

  print ''
  print 'R8_LOG_2_TEST'
  print '  R8_LOG_2 computes the logarithm base 2.'
  print ''
  print '      X      R8_LOG_2'
  print ''

  for test in range ( 0, test_num ):
    x = x_test[test]
    print '  %12f  %12f' % ( x, r8_log_2 ( x ) )
#
#  Terminate.
#
  print ''
  print 'R8_LOG_2_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( ) 
  r8_log_2_test ( )
  timestamp ( )
