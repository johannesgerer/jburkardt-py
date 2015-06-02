#!/usr/bin/env python

def i4_divp ( i, j ):

#*****************************************************************************80
#
## I4_DIVP returns the smallest multiple of J greater than or equal to I.
#
#  Example:
#
#    I  J  VALUE
#
#    0  4    0
#    1  4    1
#    2  4    1
#    3  4    1
#    4  4    1
#    5  4    2
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
#    Input, integer I, the number to be analyzed.
#
#    Input, integer J, the number, multiples of which will
#    be compared against I.  J may not be zero.
#
#    Output, integer VALUE, the smallest multiple of J that
#    is greater than or equal to I.
#
  from sys import exit
  from math import floor

  if ( j != 0 ):
    value = 1 + floor ( ( i - 1 ) / j )
  else:
    value = 0
    print ''
    print 'I4_DIVP - Fatal error!'
    print '  The input value of J was zero!'
    exit ( 'I4_DIVP - Fatal error!\n' )

  return value

def i4_divp_test ( ) :

#*****************************************************************************80
#
## I4_DIVP_TEST tests I4_DIVP.
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
  from i4_divp import i4_divp
  from i4_uniform_ab import i4_uniform_ab

  a_hi =  100
  a_lo = -100
  b_hi =  10
  b_lo = -10
  test_num = 20

  print ''
  print 'I4_DIVP_TEST'
  print '  I4_DIVP(A,B) returns the smallest multiplier of J'
  print '  that is less than I'
  print ''
  print '     A     B     C     D'
  print ''

  seed = 123456789

  for test in range ( 1, test_num + 1 ):
    [ a, seed ] = i4_uniform_ab ( a_lo, a_hi, seed )
    [ b, seed ] = i4_uniform_ab ( b_lo, b_hi, seed )
    if ( b == 0 ):
      b = 7 
    c = i4_divp ( a, b )
    d = c * b
    print '  %4d  %4d  %4d  %4d' % ( a, b, c, d )
#
#  Terminate.
#
  print ''
  print 'I4_DIVP_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  i4_divp_test ( )
  timestamp ( )
