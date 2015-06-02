#!/usr/bin/env python

def i4_log_10 ( i ):

#*****************************************************************************80
#
## I4_LOG_10 returns the integer part of the logarithm base 10 of ABS(X).
#
#  Example:
#
#        I  VALUE
#    -----  --------
#        0    0
#        1    0
#        2    0
#        9    0
#       10    1
#       11    1
#       99    1
#      100    2
#      101    2
#      999    2
#     1000    3
#     1001    3
#     9999    3
#    10000    4
#
#  Discussion:
#
#    I4_LOG_10 ( I ) + 1 is the number of decimal digits in I.
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
#    Input, integer I, the number whose logarithm base 10 is desired.
#
#    Output, integer VALUE, the integer part of the logarithm base 10 of
#    the absolute value of X.
#
  from math import floor

  i = floor ( i )

  if ( i == 0 ):

    value = 0

  else:

    value = 0
    ten_pow = 10

    i_abs = abs ( i )

    while ( ten_pow <= i_abs ):
      value = value + 1
      ten_pow = ten_pow * 10

  return value

def i4_log_10_test ( ) :

#*****************************************************************************80
#
## I4_LOG_10_TEST tests I4_LOG_10.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 May 2013
#
#  Author:
#
#    John Burkardt
#
  n = 13

  x = [ 0, 1, 2, 3, 9, 10, 11, 99, 101, -1, -2, -3, -9 ]

  print ''
  print 'I4_LOG_10_TEST'
  print '  I4_LOG_10: whole part of log base 10,'
  print ''
  print '  X, I4_LOG_10'
  print ''

  for i in range ( 0, n ):
    j = i4_log_10 ( x[i] )
    print '%6d  %12d' % ( x[i], j );
#
#  Terminate.
#
  print ''
  print 'I4_LOG_10_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  i4_log_10_test ( )
  timestamp ( )
