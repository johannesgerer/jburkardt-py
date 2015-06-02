#!/usr/bin/env python

def r8_max ( a, b ):

#*****************************************************************************80
#
## R8_MAX returns the maximum of two R8's.
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
#    Output, real VALUE, the maximum of A and B.
#
  if ( a < b ):
    value = b
  else:
    value = a

  return value

def r8_max_test ( ):

#*****************************************************************************80
#
## R8_MAX_TEST tests R8_MAX.
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
  print 'R8_MAX_TEST'
  print '  R8_MAX computes the maximum of two R8\'s.'

  r8_lo = - 10.0
  r8_hi = + 10.0
  seed = 123456789

  print ''
  print '     A         B         C=R8_MAX(A,B)'
  print ''
  for i in range ( 0, 10 ):
    a, seed = r8_uniform_ab ( r8_lo, r8_hi, seed )
    b, seed = r8_uniform_ab ( r8_lo, r8_hi, seed )
    c = r8_max ( a, b )
    print '  %8g  %8g  %8g' % ( a, b, c )
#
#  Terminate.
#
  print ''
  print 'R8_MAX_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8_max_test ( )
  timestamp ( )

