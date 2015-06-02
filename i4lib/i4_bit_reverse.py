#!/usr/bin/env python

def i4_bit_reverse ( i, n ):

#*****************************************************************************80
#
## I4_BIT_REVERSE reverses the bits in an I4.
#
#  Discussion:
#
#    An I4 is an integer ( kind = 4 ) value.
#
#  Example:
#
#       I      N  2^N     I4_BIT_REVERSE ( I, N )
#    ----    --------  -----------------------
#       0      0    1     0
#       1      0    1     1
#
#       0      3    8     0
#       1      3    8     4
#       2      3    8     2
#       3      3    8     6
#       4      3    8     1
#       5      3    8     5
#       6      3    8     3
#       7      3    8     7
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    18 March 2008
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer I, the integer to be bit reversed.
#    I should be nonnegative.  Normally I < 2^N.
#
#    Input, integer N, indicates the number of bits to
#    be reverse (N+1) or the base with respect to which the integer is to
#    be reversed (2^N).  N should be nonnegative.
#
#    Output, integer VALUE, the bit reversed value.
#
  if ( i < 0 ):

    value = -1

  elif ( n < 0 ):

    value = -1

  else:

    b = 2 ** n
    j = ( i % b )

    value = 0

    while ( True ):

      if ( b == 1 ):

        value = value + j
        j = 0
        break

      else:

        if ( ( j % 2 ) == 1 ):
          value = value + b // 2
          j = j - 1

        j = j // 2
        b = b // 2

  return value

def i4_bit_reverse_test ( ):

#*****************************************************************************80
#
## I4_BIT_REVERSE_TEST tests I4_BIT_REVERSE.
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
  print 'I4_BIT_REVERSE_TEST'
  print '  I4_BIT_REVERSE bit reverses I with respect to 2^J.'
  print ''
  print '         I         J  I4_BIT_REVERSE(I,J)'
  print ''
 
  for j in range ( 0, 5 ):
    i_hi = 2 ** j
    for i in range ( 0, i_hi ):
      k = i4_bit_reverse ( i, j )
      print '  %8d  %8d  %8d' % ( i, j, k )
#
#  Terminate.
#
  print ''
  print 'I4_BIT_REVERSE_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  i4_bit_reverse_test ( )
  timestamp ( )
