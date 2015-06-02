#!/usr/bin/env python

def i4_log_i4 ( i4, j4 ):

#*****************************************************************************80
#
## I4_LOG_I4 returns the logarithm of an I4 to an I4 base.
#
#  Discussion:
#
#    Only the integer part of the logarithm is returned.
#
#    If
#
#      K4 = I4_LOG_J4 ( I4, J4 ),
#
#    then we ordinarily have
#
#      J4^(K4-1) < I4 <= J4^K4.
#
#    The base J4 should be positive, and at least 2.  If J4 is negative,
#    a computation is made using the absolute value of J4.  If J4 is
#    -1, 0, or 1, the logarithm is returned as 0.
#
#    The number I4 should be positive and at least 2.  If I4 is negative,
#    a computation is made using the absolute value of I4.  If I4 is
#    -1, 0, or 1, then the logarithm is returned as 0.
#
#    An I4 is an integer value.
#
#  Example:
#
#    I4  J4  K4
#
#     0   3   0
#     1   3   0
#     2   3   0
#     3   3   1
#     4   3   1
#     8   3   1
#     9   3   2
#    10   3   2
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
#    Input, integer I4, the number whose logarithm is desired.
#
#    Input, integer J4, the base of the logarithms.
#
#    Output, integer VALUE, the integer part of the logarithm
#    base abs(J4) of abs(I4).
#
  from math import floor

  value = 0

  i4_abs = abs ( i4 )

  if ( 2 <= i4_abs ):

    j4_abs = abs ( j4 )

    if ( 2 <= j4_abs ):

      while ( j4_abs <= i4_abs ):
        i4_abs = floor ( i4_abs / j4_abs )
        value = value + 1

  return value

def i4_log_i4_test ( ) :

#*****************************************************************************80
#
## I4_LOG_I4_TEST tests I4_LOG_I4.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 November 2014
#
#  Author:
#
#    John Burkardt
#
  print ''
  print 'I4_LOG_I4_TEST'
  print '  I4_LOG_I4: logarithm of I4 base J4,'
  print ''
  print '        I4        J4 I4_LOG_I4'
  print ''

  for j4 in range ( 2, 6 ):
    for i4 in range ( 0, 11 ):
      k = i4_log_i4 ( i4, j4 )
      print '  %8d  %8d  %8d' % ( i4, j4, k )
    print
#
#  Terminate.
#
  print ''
  print 'I4_LOG_I4_TEST'
  print '  Normal end of execution,'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( ) 
  i4_log_i4_test ( )
  timestamp ( )
