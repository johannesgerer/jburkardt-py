#!/usr/bin/env python

def i4_bit_lo0 ( n ):

#*****************************************************************************80
#
## I4_BIT_LO0 returns the position of the low 0 bit base 2 in an I4.
#
#  Discussion:
#
#    An I4 is an integer ( kind = 4 ) value.
#
#  Example:
#
#       N    Binary    Lo 0
#    ----    --------  ----
#       0           0     1
#       1           1     2
#       2          10     1
#       3          11     3
#       4         100     1
#       5         101     2
#       6         110     1
#       7         111     4
#       8        1000     1
#       9        1001     2
#      10        1010     1
#      11        1011     3
#      12        1100     1
#      13        1101     2
#      14        1110     1
#      15        1111     5
#      16       10000     1
#      17       10001     2
#    1023  1111111111     1
#    1024 10000000000     1
#    1025 10000000001     1
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
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the integer to be measured.
#    N should be nonnegative.
#
#    Output, integer BIT, the position of the low 1 bit.
#
  bit = 0
  i = n

  while ( True ):

    bit = bit + 1
    i2 = i // 2

    if ( i == 2 * i2 ):
      break

    i = i2

  return bit

def i4_bit_lo0_test ( ):

#*****************************************************************************80
#
## I4_BIT_LO0_TEST tests I4_BIT_LO0.
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
#    John Burkardt
#
  from i4_uniform_ab import i4_uniform_ab

  seed = 123456789
  test_num = 10

  print ''
  print 'I4_BIT_LO0_TEST'
  print '  I4_BIT_LO0 returns the location of the low 0 bit.'
  print ''
  print '       I  I4_BIT_LO0(I)'
  print ''
 
  for test in range ( 0, test_num ):
    i, seed = i4_uniform_ab ( 0, 100, seed )
    j = i4_bit_lo0 ( i )
    print '  %8d  %8d' % ( i, j )
#
#  Terminate.
#
  print ''
  print 'I4_BIT_LO0_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  i4_bit_lo0_test ( )
  timestamp ( )
