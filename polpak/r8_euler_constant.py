#!/usr/bin/env python

def r8_euler_constant ( ):

#*****************************************************************************80
#
## R8_EULER_CONSTANT returns the value of the Euler-Mascheroni constant.
#
#  Discussion:
#
#    The Euler-Mascheroni constant is often denoted by a lower-case
#    Gamma.  Gamma is defined as
#
#      Gamma = limit ( M -> oo )
#        ( sum ( 1 <= N <= M ) 1 / N ) - log ( M )
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    30 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, real VALUE, the value of the Euler-Mascheroni constant.
#
  value = 0.577215664901532860606512090082402431042

  return value

def r8_euler_constant_test ( ):

#*****************************************************************************80
#
## R8_EULER_CONSTANT_TEST tests R8_EULER_CONSTANT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    30 January 2015
#
#  Author:
#
#    John Burkardt
#
  from math import log

  g = r8_euler_constant ( )

  print ''
  print 'R8_EULER_CONSTANT_TEST:'
  print '  R8_EULER_CONSTANT returns the Euler-Mascheroni constant'
  print '  sometimes denoted by "gamma".'
  print ''
  print '  gamma = limit ( N -> oo ) ( sum ( 1 <= I <= N ) 1 / I ) - log ( N )'
  print ''
  print '  Numerically, g = %24.16g' % ( g )
  print ''
  print '         N      Partial Sum    |gamma - partial sum|'
  print ''

  n = 1
  for test in range ( 0, 21 ):
    g_approx = - log ( n )
    for i in range ( 1, n + 1 ):
      g_approx = g_approx + 1.0 / i
    print '  %8d  %14.6g  %14.6g' % ( n, g_approx, abs ( g_approx - g ) )
    n = n * 2

  print ''
  print 'R8_EULER_CONSTANT_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8_euler_constant_test ( )
  timestamp ( )
