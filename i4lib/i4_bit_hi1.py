#!/usr/bin/env python

def i4_bit_hi1 ( n ) :

#*****************************************************************************80
#
## I4_BIT_HI1 returns the position of the high 1 bit base 2 in an I4.
#
#  Discussion:
#
#    An I4 is an integer ( kind = 4 ) value.
#
#  Example:
#
#       N    Binary    Hi 1
#    ----    --------  ----
#       0           0     0
#       1           1     1
#       2          10     2
#       3          11     2
#       4         100     3
#       5         101     3
#       6         110     3
#       7         111     3
#       8        1000     4
#       9        1001     4
#      10        1010     4
#      11        1011     4
#      12        1100     4
#      13        1101     4
#      14        1110     4
#      15        1111     4
#      16       10000     5
#      17       10001     5
#    1023  1111111111    10
#    1024 10000000000    11
#    1025 10000000001    11
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 October 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the integer to be measured.
#    N should be nonnegative.  If N is nonpositive, the function
#    will always be 0.
#
#    Output, integer BIT, the position of the highest bit.
#
  i = n
  bit = 0

  while ( True ):

    if ( i <= 0 ):
      break

    bit = bit + 1
    i = i // 2

  return bit

def i4_bit_hi1_test ( ):

#*****************************************************************************80
#
## I4_BIT_HI1_TEST tests I4_BIT_HI1.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 October 2014
#
#  Author:
#
#    John Burkardt
#
  from i4_uniform_ab import i4_uniform_ab

  seed = 123456789
  test_num = 10

  print ''
  print 'I4_BIT_HI1_TEST'
  print '  I4_BIT_HI1 returns the location of the high 1 bit.'
  print ''
  print '       I  I4_BIT_HI1(I)'
  print ''
 
  for test in range ( 0, test_num ):
    i, seed = i4_uniform_ab ( 0, 100, seed )
    j = i4_bit_hi1 ( i )
    print '  %8d  %8d' % ( i, j )
#
#  Terminate.
#
  print ''
  print 'I4_BIT_HI1_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  i4_bit_hi1_test ( )
  timestamp ( )

