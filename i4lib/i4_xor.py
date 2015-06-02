#!/usr/bin/env python

def i4_xor ( i, j ):

#*****************************************************************************80
#
## I4_XOR calculates the exclusive OR of two I4's.
#
#  Discussion:
#
#    An I4 is an integer value.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 September 2014
#
#  Author:
#
#   John Burkardt
#
#  Parameters:
#
#    Input, integer I, J, two values whose exclusive OR is needed.
#
#    Output, integer VALUE, the exclusive OR of I and J.
#
  i1 = i
  j1 = j
  value = 0
  l = 1

  while ( i1 != 0 or j1 != 0 ):

    i2 = i1 // 2
    j2 = j1 // 2

    if ( \
      ( ( i1 == 2 * i2 ) and ( j1 != 2 * j2 ) ) or \
      ( ( i1 != 2 * i2 ) and ( j1 == 2 * j2 ) ) ):
      value = value + l

    i1 = i2
    j1 = j2
    l = 2 * l

  return value

def i4_xor_test ( ):

#*****************************************************************************80
#
## I4_XOR_TEST tests I4_XOR.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 September 2014
#
#  Author:
#
#    John Burkardt
#
  from i4_uniform_ab import i4_uniform_ab

  i4_lo = 0
  i4_hi = 100
  test_num = 10
  seed = 123456789

  print ''
  print 'I4_XOR_TEST'
  print '  I4_XOR returns the bitwise exclusive OR of two I4s.'
  print ''
  print '         I         J    I4_XOR       I^J'
  print ''

  for test in range ( 0, test_num ):

    i, seed = i4_uniform_ab ( i4_lo, i4_hi, seed )
    j, seed = i4_uniform_ab ( i4_lo, i4_hi, seed )
    k = i4_xor ( i, j )
    l = ( i ^ j )
    print '  %8d  %8d  %8d  %8d' % ( i, j, k, l )
#
#  Terminate.
#
  print ''
  print 'I4_XOR_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  i4_xor_test ( )
  timestamp ( )

