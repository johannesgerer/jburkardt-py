#! /usr/bin/env python
#
def comb_unrank ( m, n, rank ):

#*****************************************************************************80
#
## COMB_UNRANK returns the RANK-th combination of N things out of M.
#
#  Discussion:
#
#    Going from a rank to a thing is called "unranking".
#
#    The combinations are ordered lexically.
#
#    Lexical order can be illustrated for the general case of N and M as
#    follows:
#
#    1:       1,     2,     3,     ..., N-2, N-1, N
#    2:       1,     2,     3,     ..., N-2, N-1, N+1
#    3:       1,     2,     3,     ..., N-2, N-1, N+2
#    ...
#    M-N+1:   1,     2,     3,     ..., N-2, N-1, M
#    M-N+2:   1,     2,     3,     ..., N-2, N,   N+1
#    M-N+3:   1,     2,     3,     ..., N-2, N,   N+2
#    ...
#    LAST-2:  M-N,   M-N+1, M-N+3, ..., M-2, M-1, M
#    LAST-1:  M-N,   M-N+2, M-N+3, ..., M-2, M-1, M
#    LAST:    M-N+1, M-N+2, M-N+3, ..., M-2, M-1, M
#
#    There are a total of M!/(N!*(M-N)!) combinations of M
#    things taken N at a time.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 May 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    B P Buckles, M Lybanon,
#    Algorithm 515,
#    Generation of a Vector from the Lexicographical Index,
#    ACM Transactions on Mathematical Software,
#    Volume 3, Number 2, pages 180-182, June 1977.
#
#  Parameters:
#
#    Input, integer M, the size of the set.
#
#    Input, integer N, the number of things in the combination.
#    N must be greater than 0, and no greater than M.
#
#    Input, integer RANK, the lexicographical rank of the combination
#    sought.  RANK must be at least 1, and no greater than M!/(N!*(M-N)!).
#
#    Output, integer A(N), the combination.
#
  import numpy as np
  from i4_choose import i4_choose

  a = np.zeros ( n, dtype = np.int32 )
#
#  Initialize the lower bound index.
#
  k = 0
#
#  Select elements in ascending order.
#
  for i in range ( 0, n - 1 ):
#
#  Set the lower bound element number for next element value.
#
    a[i] = 0

    if ( 0 < i ):
      a[i] = a[i-1]
#
#  Check each element value.
#
    while ( True ):

      a[i] = a[i] + 1
      j = i4_choose ( m - a[i], n - i - 1 )
      k = k + j

      if ( rank <= k ):
        break

    k = k - j;

  a[n-1] = a[n-2] + rank - k

  return a

def comb_unrank_test ( ):

#*****************************************************************************80
#
## COMB_UNRANK_TEST tests COMB_UNRANK.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 May 2015
#
#  Author:
#
#    John Burkardt
#
  from i4_choose import i4_choose

  n = 5
  m = 10
  cnk = i4_choose ( m, n )

  print ''
  print 'COMB_UNRANK_TEST'
  print '  COMB_UNRANK returns a combination of N things'
  print '  out of M, given the lexicographic rank.'
  print ''
  print '  The total set size is M = %d' % ( m )
  print '  The subset size is N =    %d' % ( n )
  print '  The number of combinations of N out of M is %d' % ( cnk )
  print ''
  print '   Rank	  Combination'
  print ''
 
  for rank in range ( 1, 4 ):
    a = comb_unrank ( m, n, rank )
    print '  %3d' % ( rank ),
    for i in range ( 0, n ):
      print '  %5d' % ( a[i] ),
    print ''
 
  for rank in range ( 6, 9 ):
    a = comb_unrank ( m, n, rank )
    print '  %3d' % ( rank ),
    for i in range ( 0, n ):
      print '  %5d' % ( a[i] ),
    print ''
 
  for rank in range ( 250, 253 ):
    a = comb_unrank ( m, n, rank )
    print '  %3d' % ( rank ),
    for i in range ( 0, n ):
      print '  %5d' % ( a[i] ),
    print ''
#
#  Terminate.
#
  print ''
  print 'COMB_UNRANK_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  comb_unrank_test ( )
  timestamp ( )
