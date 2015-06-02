#!/usr/bin/env python

def triangle_num ( n ):

#*****************************************************************************80
#
## TRIANGLE_NUM returns the N-th triangular  number.
#
#  Discussion:
#
#    The N-th triangular number T(N) is formed by the sum of the first
#    N integers:
#
#      T(N) = sum ( 1 <= I <= N ) I
#
#    By convention, T(0) = 0.
#
#    T(N) = ( N * ( N + 1 ) ) / 2
#
#  First Values:
#
#     0
#     1
#     3
#     6
#    10
#    15
#    21
#    28
#    36
#    45
#    55
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 February 2015
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
#    Output, integer VALUE, the N-th triangleal number.
#
  value = ( n * ( n + 1 ) ) / 2

  return value

def triangle_num_test ( ):

#*****************************************************************************80
#
## TRIANGLE_NUM_TEST tests TRIANGLE_NUM.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 February 2015
#
#  Author:
#
#    John Burkardt
#
  print ''
  print 'TRIANGLE_NUM_TEST'
  print '  TRIANGLE_NUM computes the triangular numbers.'
  print ''
 
  for n in range ( 1, 11 ):
    print '  %2d  %6d' % ( n, triangle_num ( n ) )

  print ''
  print 'TRIANGLE_NUM_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  triangle_num_test ( )
  timestamp ( )
