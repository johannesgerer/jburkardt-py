#!/usr/bin/env python

def r8_min ( a, b ):

#*****************************************************************************80
#
## R8_MIN returns the minimum of two R8's.
#
#  Discussion:
#
#    An R8 is a double precision real value.
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
#  Parameters:
#
#    Input, real A, B, values to compare.
#
#    Output, real VALUE, the minimum of A and B.
#
  if ( a < b ):
    value = a
  else:
    value = b

  return value

def r8_min_test ( ):

#*****************************************************************************80
#
## R8_MIN_TEST tests R8_MIN.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 March 2015
#
#  Author:
#
#    John Burkardt
#
  from r8_uniform_ab import r8_uniform_ab

  print ''
  print 'R8_MIN_TEST'
  print '  R8_MIN computes the minimum of two R8\'s.'

  r8_lo = - 10.0
  r8_hi = + 10.0
  seed = 123456789

  print ''
  print '     A         B         C=R8_MIN(A,B)'
  print ''
  for i in range ( 0, 10 ):
    a, seed = r8_uniform_ab ( r8_lo, r8_hi, seed )
    b, seed = r8_uniform_ab ( r8_lo, r8_hi, seed )
    c = r8_min ( a, b )
    print '  %8g  %8g  %8g' % ( a, b, c )
#
#  Terminate.
#
  print ''
  print 'R8_MIN_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8_min_test ( )
  timestamp ( )

