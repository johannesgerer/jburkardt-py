#!/usr/bin/env python

def i4_log_r8 ( x, b ):

#*****************************************************************************80
#
## I4_LOG_R8 returns the integer part of the logarithm base ABS(B) of ABS(X).
#
#  Example:
#
#    If B is greater than 1, and X is positive:
#
#    if 1/B^2  <  X <= 1/B   I4_LOG_R8(X) = -1,
#    if 1/B    <  X <= 1     I4_LOG_R8(X) = 0,
#    if 1      <= X <  B,    I4_LOG_R8(X) = 0,
#    if B      <= X <  B^2   I4_LOG_R8(X) = 1,
#    if B^2    <= X <  B^3   I4_LOG_R8(X) = 2.
#
#    For positive I4_LOG_R8(X), it should be true that
#
#      ABS(B)^I4_LOG_R8(X) <= ABS(X) < ABS(B)^(I4_LOG_R8(X)+1).
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
#    Input, integer X, the number whose logarithm base B is desired.
#    If X is 0, then I4_LOG_R8 is returned as -HUGE().
#
#    Input, real B, the absolute value of the base of the
#    logarithms.  B must not be -1, 0, or 1.
#
#    Output, integer VALUE, the integer part of the logarithm
#    base abs(B) of X.
#
  from math import floor

  i4_huge = 2147483647

  x = floor ( x )

  if ( x == 0 ):
    value = - i4_huge
    return value

  b = abs ( b )
  value = 0

  if ( b == 1.0 ):
    return value

  if ( b == 0.0 ):
    return value

  x = abs ( x )

  if ( b < 1.0 ):
    value_sign = -1
    b = 1.0 / b
  else:
    value_sign = +1

  if ( 1.0 <= x and x < b ):
    value = value_sign * value
    return value

  while ( b < x ):
    x = x / b
    value = value + 1

  while ( x * b <= 1.0 ):
    x = x * b
    value = value - 1
#
#  If the absolute value of the base was less than 1, we inverted
#  earlier.  Now negate the logarithm to account for that.
#
  value = value_sign * value

  return value

def i4_log_r8_test ( ):

#*****************************************************************************80
#
## I4_LOG_R8_TEST tests I4_LOG_R8.
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
  test_num = 10

  b_test = [ 2.0, 3.0,  4.0,  5.0,   6.0, 7.0, 8.0, 16.0, 32.0, 256.0 ]

  x = 16
 
  print ''
  print 'I4_LOG_R8_TEST'
  print '  I4_LOG_R8: whole part of log base B,'
  print ''
  print '  X    B   I4_LOG_R8'
  print ''

  for test in range ( 0, test_num ):
 
    b = b_test[test]
    j = i4_log_r8 ( x, b )

    print '  %6d  %12f  %12d' % ( x, b, j )
#
#  Terminate.
#
  print ''
  print 'I4_LOG_R8_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  i4_log_r8_test ( )
  timestamp ( )
