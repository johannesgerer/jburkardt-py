#!/usr/bin/env python
#
def eulerian ( n ):

#*****************************************************************************80
#
## EULERIAN computes the Eulerian number E(N,K).
#
#  Definition:
#
#    A run in a permutation is a sequence of consecutive ascending values.
#
#    E(N,K) is the number of permutations of N objects which contain
#    exactly K runs.
#
#  Examples:
#
#     N = 7
#
#     1     0     0     0     0     0     0
#     1     1     0     0     0     0     0
#     1     4     1     0     0     0     0
#     1    11    11     1     0     0     0
#     1    26    66    26     1     0     0
#     1    57   302   302    57     1     0
#     1   120  1191  2416  1191   120     1
#
#  Recursion:
#
#    E(N,K) = K * E(N-1,K) + (N-K+1) * E(N-1,K-1).
#
#  Properties:
#
#    E(N,1) = E(N,N) = 1.
#    E(N,K) = 0 if K <= 0 or N < K.
#    sum ( 1 <= K <= N ) E(N,K) = N!.
#    X^N = sum ( 0 <= K <= N ) COMB(X+K-1, N ) E(N,K)
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    04 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Dennis Stanton and Dennis White,
#    Constructive Combinatorics,
#    Springer Verlag, 1986
#
#  Parameters:
#
#    Input, integer N, the number of rows desired.
#
#    Output, integer E(N,N), the first N rows of Eulerian numbers.
#
  import numpy as np

  e = np.zeros ( ( n, n ) )
#
#  Construct rows 1, 2, ..., N of the Eulerian triangle.
#
  e[0,0] = 1
  for j in range ( 1, n ):
    e[0,j] = 0

  for i in range ( 1, n ):
    e[i,0] = 1
    for j in range ( 1, n ):
      e[i,j] = ( j + 1 ) * e[i-1,j] + ( i - j + 1 ) * e[i-1,j-1]

  return e

def eulerian_test ( ):

#*****************************************************************************80
#
## EULERIAN_TEST tests EULERIAN.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    04 February 2015
#
#  Author:
#
#    John Burkardt
#
  print ''
  print 'EULERIAN_TEST'
  print '  EULERIAN computes Eulerian numbers.'

  n = 7
  e = eulerian ( n )

  for i in range ( 0, n ):
    for j in range ( 0, n ):
      print '  %4d' % ( e[i,j] ),
    print ''
 
  print ''
  print 'EULERIAN_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  eulerian_test ( )
  timestamp ( )
