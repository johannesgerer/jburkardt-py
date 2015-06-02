#!/usr/bin/env python

def tetrahedron_num ( n ):

#*****************************************************************************80
#
## TETRAHEDRON_NUM returns the N-th tetrahedron number.
#
#  Discussion:
#
#    The N-th tetrahedral number T3(N) is formed by the sum of the first
#    N triangular numbers:
#
#      T3(N) = sum ( 1 <= I <= N ) T2(I)
#            = sum ( 1 <= I <= N ) sum ( 1 <= J < I ) J
#
#    By convention, T3(0) = 0.
#
#    T3(N) = ( N * ( N + 1 ) * ( N + 2 ) ) / 6
#
#  First Values:
#
#     0
#     1
#     4
#    10
#    20
#    35
#    56
#    84
#   120
#   165
#   220
#   275
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
#    Output, integer VALUE, the N-th tetrahedronal number.
#
  value = ( n * ( n + 1 ) * ( n + 2 ) ) / 6

  return value

def tetrahedron_num_test ( ):

#*****************************************************************************80
#
## TETRAHEDRON_NUM_TEST tests TETRAHEDRON_NUM.
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
  print 'TETRAHEDRON_NUM_TEST'
  print '  TETRAHEDRON_NUM computes the triangular numbers.'
  print ''
 
  for n in range ( 1, 11 ):
    print '  %2d  %6d' % ( n, tetrahedron_num ( n ) )

  print ''
  print 'TETRAHEDRON_NUM_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  tetrahedron_num_test ( )
  timestamp ( )
