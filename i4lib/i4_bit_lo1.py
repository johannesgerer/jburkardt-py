#!/usr/bin/env python

def i4_bit_lo1 ( n ) :

#*****************************************************************************80
#
## I4_BIT_LO1 returns the position of the low 1 bit base 2 in an I4.
#
#  Discussion:
#
#    An I4 is an integer ( kind = 4 ) value.
#
#  Example:
#
#       N    Binary    Lo 1
#    ----    --------  ----
#       0           0     0
#       1           1     1
#       2          10     2
#       3          11     1
#       4         100     3
#       5         101     1
#       6         110     2
#       7         111     1
#       8        1000     4
#       9        1001     1
#      10        1010     2
#      11        1011     1
#      12        1100     3
#      13        1101     1
#      14        1110     2
#      15        1111     1
#      16       10000     5
#      17       10001     1
#    1023  1111111111     1
#    1024 10000000000    11
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

    if ( i != 2 * i2 ):
      break

    i = i2

  return bit

def i4_bit_lo1_test ( ):

#*****************************************************************************80
#
## I4_BIT_LO1_TEST tests I4_BIT_LO1.
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
  print 'I4_BIT_LO1_TEST'
  print '  I4_BIT_LO1 returns the location of the low 1 bit.'
  print ''
  print '       I  I4_BIT_LO1(I)'
  print ''
 
  for test in range ( 0, test_num ):
    i, seed = i4_uniform_ab ( 0, 100, seed )
    j = i4_bit_lo1 ( i )
    print '  %8d  %8d' % ( i, j )
#
#  Terminate.
#
  print ''
  print 'I4_BIT_LO1_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  i4_bit_lo1_test ( )
  timestamp ( )
