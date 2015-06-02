#!/usr/bin/env python

def i4_gcd ( i, j ):

#*****************************************************************************80
#
## I4_GCD finds the greatest common divisor of I and J.
#
#  Discussion:
#
#    Only the absolute values of I and J are
#    considered, so that the result is always nonnegative.
#
#    If I or J is 0, I4_GCD is returned as max ( 1, abs ( I ), abs ( J ) ).
#
#    If I and J have no common factor, I4_GCD is returned as 1.
#
#    Otherwise, using the Euclidean algorithm, I4_GCD is the
#    largest common factor of I and J.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    04 April 2013
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer I, J, two numbers whose greatest common divisor
#    is desired.
#
#    Output, integer VALUE, the greatest common divisor of I and J.
#
  value = 1
#
#  Return immediately if either I or J is zero.
#
  if ( i == 0 ):
    value = max ( 1, abs ( j ) )
    return value
  elif ( j == 0 ):
    value = max ( 1, abs ( i ) )
    return value
#
#  Set IP to the larger of I and J, IQ to the smaller.
#  This way, we can alter IP and IQ as we go.
#
  ip = max ( abs ( i ), abs ( j ) )
  iq = min ( abs ( i ), abs ( j ) )
#
#  Carry out the Euclidean algorithm.
#
  while ( True ):

    ir = ( ip % iq )

    if ( ir == 0 ):
      break

    ip = iq
    iq = ir

  value = iq

  return value

def i4_gcd_test ( ):

#*****************************************************************************80
#
## I4_GCD_TEST tests I4_GCD.
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
  from i4_gcd import i4_gcd

  test_num = 7

  i_test = [ 36, 49, 0, 12, 36, 1, 91 ]
  j_test = [ 30, -7, 71, 12, 49, 42, 28 ]

  print ''
  print 'I4_GCD_TEST'
  print '  I4_GCD computes the greatest common factor'
  print 
  print '     I     J   I4_GCD'
  print ''
 
  for test in range ( 0, test_num ):
    i = i_test[test]
    j = j_test[test]
    k = i4_gcd ( i, j )
    print '  %6d  %6d  %6d' % ( i, j, k )
#
#  Terminate.
#
  print ''
  print 'I4_GCD_TEST'
  print '  Normal end of execution'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  i4_gcd_test ( )
  timestamp ( )
