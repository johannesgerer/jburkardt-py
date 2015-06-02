#!/usr/bin/env python
#
def catalan ( n ):

#*****************************************************************************80
#
## CATALAN computes the Catalan numbers, from C(0) to C(N).
#
#  First values:
#
#     C(0)     1
#     C(1)     1
#     C(2)     2
#     C(3)     5
#     C(4)    14
#     C(5)    42
#     C(6)   132
#     C(7)   429
#     C(8)  1430
#     C(9)  4862
#    C(10) 16796
#
#  Formula:
#
#    C(N) = (2*N)! / ( (N+1) * (N!) * (N!) )
#         = 1 / (N+1) * COMB ( 2N, N )
#         = 1 / (2N+1) * COMB ( 2N+1, N+1).
#
#  Recursion:
#
#    C(N) = 2 * (2*N-1) * C(N-1) / (N+1)
#    C(N) = sum ( 1 <= I <= N-1 ) C(I) * C(N-I)
#
#  Discussion:
#
#    The Catalan number C(N) counts:
#
#    1) the number of binary trees on N vertices;
#    2) the number of ordered trees on N+1 vertices;
#    3) the number of full binary trees on 2N+1 vertices;
#    4) the number of well formed sequences of 2N parentheses;
#    5) number of ways 2N ballots can be counted, in order,
#       with N positive and N negative, so that the running sum
#       is never negative;
#    6) the number of standard tableaus in a 2 by N rectangular Ferrers diagram;
#    7) the number of monotone functions from [1..N} to [1..N} which
#       satisfy f(i) <= i for all i;
#
#  Example:
#
#    N = 3
#
#    ()()()
#    ()(())
#    (()())
#    (())()
#    ((()))
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    23 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Dennis Stanton and Dennis White,
#    Constructive Combinatorics,
#    Springer Verlag, New York, 1986.
#
#  Parameters:
#
#    Input, integer N, the number of Catalan numbers desired.
#
#    Output, integer C(1:N+1), the Catalan numbers from C(0) to C(N).
#
  import numpy as np

  c = np.zeros ( n + 1 );

  c[0] = 1
#
#  The extra parentheses ensure that the integer division is
#  done AFTER the integer multiplication.
#
  for i in range ( 1, n + 1 ):
    c[i] = ( c[i-1] * 2 * ( 2 * i - 1 ) ) / ( i + 1 )

  return c

def catalan_test ( ):

#*****************************************************************************80
#
## CATALAN_TEST tests CATALAN.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    23 December 2014
#
#  Author:
#
#    John Burkardt
#
  from catalan_values import catalan_values

  print ''
  print 'CATALAN_TEST'
  print '  CATALAN computes Catalan numbers.'
  print ''
  print '  N  exact C(I)  computed C(I)'
  print ''

  n_data = 0

  while ( True ):

    n_data, n, c = catalan_values ( n_data )

    if ( n_data == 0 ):
      break

    c2 = catalan ( n )

    print '  %2d  %6d  %6d' % ( n, c, c2[n] )
 
  print ''
  print 'CATALAN_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  catalan_test ( )
  timestamp ( )
