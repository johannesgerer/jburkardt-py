#!/usr/bin/env python
#
def comb_row_next ( n, c ):

#*****************************************************************************80
#
## COMB_ROW_NEXT computes the next row of Pascal's triangle.
#
#  Discussion:
#
#    Row N contains the combinatorial coefficients
#
#      C(N,0), C(N,1), C(N,2), ... C(N,N)
#
#    The sum of the elements of row N is equal to 2**N.
#
#    C(N,K) = N! / ( K! * (N-K)! )
#
#  First terms:
#
#     N K:0  1   2   3   4   5   6   7  8  9 10
#
#     0   1
#     1   1  1
#     2   1  2   1
#     3   1  3   3   1
#     4   1  4   6   4   1
#     5   1  5  10  10   5   1
#     6   1  6  15  20  15   6   1
#     7   1  7  21  35  35  21   7   1
#     8   1  8  28  56  70  56  28   8  1
#     9   1  9  36  84 126 126  84  36  9  1
#    10   1 10  45 120 210 252 210 120 45 10  1
#
#  Recursion:
#
#    C(N,K) = C(N-1,K-1)+C(N-1,K)
#
#  Special values:
#
#    C(N,0) = C(N,N) = 1
#    C(N,1) = C(N,N-1) = N
#    C(N,N-2) = sum ( 1 <= I <= N ) N
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the desired row.
#
#    Input/output, integer C(N+1).  On input, row N-1 is contained in
#    entries 0 through N-1.  On output, row N is contained in entries 0
#    through N.
#  
  if ( n < 0 ):
    return

  c[n] = 1
  for i in range ( n - 1, 0, -1 ):
    c[i] = c[i] + c[i-1]
  c[0] = 1

  return c

def comb_row_next_test ( ):

#*****************************************************************************80
#
## COMB_ROW_NEXT_TEST tests COMB_ROW_NEXT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 December 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n_max = 10

  print ''
  print 'COMB_ROW_NEXT_TEST'
  print '  COMB_ROW_NEXT computes the next row of Pascals triangle.'
  print ''

  c = np.zeros ( n_max + 1 )

  for n in range ( 0, n_max + 1 ):
    c = comb_row_next ( n, c )
    print '  %2d  ' % ( n ),
    for i in range ( 0, n + 1 ):
      print '  %3d' % ( c[i] ),
    print ''
 
  print ''
  print 'COMB_ROW_NEXT_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  comb_row_next_test ( )
  timestamp ( )
