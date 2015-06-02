#!/usr/bin/env python
#
def hail ( n ):

#*****************************************************************************80
#
## HAIL computes the hail function.
#
#  Discussion:
#
#    Starting with a positive integer N, we divide it by 2 if it is
#    even, or triple and add 1 if odd, and repeat this process until
#    reaching the value 1.  The number of times the process is carried
#    out is the value of the hail function for the given starting value.
#
#    Actually, HAIL is not well defined, since it is not known if
#    the above process actually terminates at 1 for every starting value N.
#
#  Example:
#
#     N  Sequence                                                  Hail
#
#     1                                                               0
#     2   1                                                           1
#     3  10,  5, 16,  8,  4,  2,  1                                   7
#     4   2   1                                                       2
#     5  16,  8,  4,  2,  1                                           5
#     6   3, 10,  5, 16,  8,  4,  2,  1                               8
#     7  22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1   16
#     8   4,  2,  1                                                   3
#     9  28, 14,  7, ...                                             19
#    10   5, 16,  8,  4,  2,  1                                       6
#    11  34, 17, 52, 26, 13, 40, 20, 10,  5, 16, 8, 4, 2, 1          14
#    12   6,  3, 10,  5, 16,  8,  4,  2,  1                           9
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    11 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the starting value for the hail sequence.
#
#    Output, integer VALUE, the number of steps before the hail sequence 
#    reached 1.
#
  k = 0
  m = n

  if ( 0 < n ):

    while ( m != 1 ):
      k = k + 1
      if ( ( m % 2 ) == 0 ):
        m = ( m // 2 )
      else:
        m = 3 * m + 1

  value = k

  return value

def hail_test ( ):

#*****************************************************************************80
#
## HAIL_TEST tests HAIL.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    11 February 2015
#
#  Author:
#
#    John Burkardt
#
  print ''
  print 'HAIL_TEST'
  print '  HAIL(I) computes the length of the hail sequence'
  print '  for I, also known as the 3*N+1 sequence.'
  print ''
  print '     I   HAIL(I))'
  print ''

  for i in range ( 0, 21 ):
    h = hail ( i )
    print '  %6d  %6d' % ( i, h )
 
  print ''
  print 'HAIL_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  hail_test ( )
  timestamp ( )
