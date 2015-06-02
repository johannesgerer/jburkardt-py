#!/usr/bin/env python

def i4_log_2 ( i ):

#*****************************************************************************80
#
## I4_LOG_2 returns the integer part of the logarithm base 2 of |I|.
#
#  Discussion:
#
#    For positive I4_LOG_2(I), it should be true that
#      2^I4_LOG_2(X) <= |I| < 2^(I4_LOG_2(I)+1).
#    The special case of I4_LOG_2(0) returns -HUGE().
#
#  Example:
#
#     I  Value
#
#     0  -1
#     1,  0
#     2,  1
#     3,  1
#     4,  2
#     5,  2
#     6,  2
#     7,  2
#     8,  3
#     9,  3
#    10,  3
#   127,  6
#   128,  7
#   129,  7
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 May 2013
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer I, the number whose logarithm base 2 is desired.
#
#    Output, integer VALUE, the integer part of the logarithm base 2 of
#    the absolute value of I.
#
  from math import floor

  i = floor ( i )

  if ( i == 0 ):

    value = 0

  else:

    value = 0

    i = abs ( i )

    while ( 2 <= i ):
      i = floor ( i / 2 )
      value = value + 1

  return value

def i4_log_2_test ( ):

#*****************************************************************************80
#
## I4_LOG_2_TEST tests I4_LOG_2.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 May 2013
#
#  Author:
#
#    John Burkardt
#
  test_num = 17

  x_test = [ 0, 1, 2, 3, 9, 10, 11, 99, 101, -1, -2, \
    -3, -9, 1000, 1023, 1024, 1025 ]
 
  print ''
  print 'I4_LOG_2_TEST'
  print '  I4_LOG_2: whole part of log base 2.'
  print ''
  print '       X     I4_LOG_2'
  print ''

  for test in range ( 0, test_num ):
    x = x_test[test]
    j = i4_log_2 ( x )
    print '  %6d  %12d' % ( x, j )
#
#  Terminate.
#
  print ''
  print 'I4_LOG_2_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  i4_log_2_test ( )
  timestamp ( )
