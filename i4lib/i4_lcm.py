#!/usr/bin/env python

def i4_lcm ( i, j ) :

#*****************************************************************************80
#
## I4_LCM computes the least common multiple of two I4's.
#
#  Discussion:
#
#    The least common multiple may be defined as
#
#      LCM(I,J) = ABS( I * J ) / GCD(I,J)
#
#    where GCD(I,J) is the greatest common divisor of I and J.
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
#  Parameters:
#
#    Input, integer I, J, the integers whose LCM is desired.
#
#    Output, integer VALUE, the least common multiple of I and J.
#    VALUE is never negative.  VALUE is 0 if either I or J is zero.
#
  from i4_gcd import i4_gcd

  value = abs ( i * ( j / i4_gcd ( i, j ) ) )

  return value

def i4_lcm_test ( ):

#*****************************************************************************80
#
## I4_LCM_TEST tests I4_LCM.
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
  from i4_lcm import i4_lcm

  test_num = 7

  i_test = [ 36, 49, 0, 12, 36, 1, 91 ]
  j_test = [ 30, -7, 71, 12, 49, 42, 28 ]

  print ''
  print 'I4_LCM_TEST'
  print '  I4_LCM computes the least common multiple.'
  print ''
  print '       I       J  I4_LCM'
  print ''
 
  for test in range ( 0, test_num ):
    i = i_test[test]
    j = j_test[test]
    k = i4_lcm ( i, j )
    print '  %6d  %6d  %6d' % ( i, j, k )
#
#  Terminate.
#
  print ''
  print 'I4_LCM_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  i4_lcm_test ( )
  timestamp ( )
