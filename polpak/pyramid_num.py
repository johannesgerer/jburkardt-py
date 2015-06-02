#!/usr/bin/env python

def pyramid_num ( n ):

#*****************************************************************************80
#
## PYRAMID_NUM returns the N-th pyramidal number.
#
#  Discussion:
#
#    The N-th pyramidal number P(N) is formed by the sum of the first
#    N triangular numbers T(J):
#
#      T(J) = sum ( 1 <= J <= N ) J
#
#      P(N) = sum ( 1 <= I <= N ) T(I)
#
#    By convention, T(0) = 0.
#
#    P(N) = ( (N+1)^3 - (N+1) ) / 6
#
#    Note that this pyramid will have a triangular base.
#
#    The first values are:
#
#      0
#      1
#      4
#     10
#     20
#     35
#     56
#     84
#    120
#    165
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    04 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the index of the desired number, which must be
#    at least 0.
#
#    Output, integer VALUE, the N-th pyramidal number.
#
  value = ( ( n + 1 ) ** 3 - ( n + 1 ) ) / 6

  return value

def pyramid_num_test ( ):

#*****************************************************************************80
#
## PYRAMID_NUM_TEST tests PYRAMID_NUM.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    04 December 2014
#
#  Author:
#
#    John Burkardt
#
  print ''
  print 'PYRAMID_NUM_TEST'
  print '  PYRAMID_NUM computes the pyramidal numbers.'
  print ''
 
  for n in range ( 1, 11 ):
    print '  %2d  %6d' % ( n, pyramid_num ( n ) )

  print ''
  print 'PYRAMID_NUM_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  pyramid_num_test ( )
  timestamp ( )
