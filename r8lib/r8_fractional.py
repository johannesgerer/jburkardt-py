#!/usr/bin/env python

def r8_fractional ( x ):

#*****************************************************************************80
#
## R8_FRACTIONAL returns the fractional part of an R8.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    05 June 2013
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real X, the argument.
#
#    Output, real VALUE, the fractional part of X.
#
  from math import floor

  value = abs ( x ) - floor ( abs ( x ) )

  return value

def r8_fractional_test ( ):

#*****************************************************************************80
#
## R8_FRACTIONAL_TEST tests R8_FRACTIONAL.
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
  from r8_uniform_ab import r8_uniform_ab

  r8_hi = 5.0
  r8_lo = -3.0
  test_num = 10

  seed = 123456789

  print ''
  print 'R8_FRACTIONAL_TEST'
  print '  R8_FRACTIONAL returns the fractional part of an R8.'
  print ''
  print '       X       R8_FRACTIONAL(X)'
  print ''

  for test in range ( 0, test_num ):
    r8, seed = r8_uniform_ab ( r8_lo, r8_hi, seed )
    fractional = r8_fractional ( r8 )
    print '  %10f  %10f' % ( r8, fractional )
#
#  Terminate.
#
  print ''
  print 'R8_FRACTIONAL_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( ) 
  r8_fractional_test ( )
  timestamp ( )

