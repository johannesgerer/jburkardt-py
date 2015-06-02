#! /usr/bin/env python
#
def pent_enum ( n ):

#*****************************************************************************80
#
## PENT_ENUM computes the N-th pentagonal number.
#
#  Discussion:
#
#    The pentagonal number P(N) counts the number of dots in a figure of
#    N nested pentagons.  The pentagonal numbers are defined for both
#    positive and negative N.
#
#    The pentagonal numbers are also useful in determining the
#    number of partitions of an integer.
#
#  First values:
#
#     N    P
#
#    -5   40
#    -4   26
#    -3   15
#    -2    7
#    -1    2
#     0    0
#     1    1
#     2    5
#     3   12
#     4   22
#     5   35
#     6   51
#     7   70
#     8   92
#     9  117
#    10  145
#
#  Formula:
#
#    P(N) = ( N * ( 3 * N - 1 ) ) / 2
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    09 June 2004
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the index of the pentagonal number desired.
#
#    Output, integer VALUE, the value of the N-th pentagonal number.
#
  value = ( n * ( 3 * n - 1 ) ) / 2

  return value

def pent_enum_test ( ):

#*****************************************************************************80
#
## PENT_ENUM_TEST tests PENT_ENUM.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    19 December 2014
#
#  Author:
#
#    John Burkardt
#
  n = 10

  print ''
  print 'PENT_ENUM_TEST'
  print '  PENT_ENUM counts points in pentagons;'
  print ''
  print '  N    Pent(N)'
  print ''

  for i in range ( 0, n + 1 ):
    print '  %8d  %8d' % ( i, pent_enum ( i ) )
#
#  Terminate.
#
  print ''
  print 'PENT_ENUM_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  pent_enum_test ( )
  timestamp ( )

