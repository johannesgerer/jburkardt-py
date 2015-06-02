#! /usr/bin/env python
#
def subset_gray_rank ( n, a ):

#*****************************************************************************80
#
## SUBSET_GRAY_RANK ranks a subset of an N set, using the Gray code ordering.
#
#  Example:
#
#    N = 4
#
#       A       Rank
#    -------   -----
#
#    0 0 0 0       1
#    1 0 0 0       2
#    1 1 0 0       3
#    0 1 0 0       4
#    0 1 1 0       5
#    1 1 1 0       6
#    1 0 1 0       7
#    0 0 1 0       8
#    0 0 1 1       9
#    1 0 1 1      10
#    1 1 1 1      11
#    0 1 1 1      12
#    0 1 0 1      13
#    1 1 0 1      14
#    1 0 0 1      15
#    0 0 0 1      16
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    31 May 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the order of the total set from which
#    subsets will be drawn.
#
#    Input, integer A(N); A(I) is 1 if element I is in the set,
#    and 0 otherwise.
#
#    Output, integer RANK, the rank of the subset in the Gray code ordering.
#
  from gray_rank2 import gray_rank2
  from ubvec_to_ui4 import ubvec_to_ui4

  gray = ubvec_to_ui4 ( n, a )

  rank = gray_rank2 ( gray )

  rank = rank + 1

  return rank

def subset_gray_rank_test ( ):

#*****************************************************************************80
#
## SUBSET_GRAY_RANK_TEST tests SUBSET_GRAY_RANK.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    31 May 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 5
  a = np.array ( [ 1, 0, 1, 1, 0 ] )

  print ''
  print 'SUBSET_GRAY_RANK_TEST'
  print '  SUBSET_GRAY_RANK returns rank of a subset of an N set'
  print '  using the Gray code ordering.'
  print ''
  print '  For N = %d' % ( n )
  print '  the subset is:'
  for i in range ( 0, n ):
    print '  %4d' % ( a[i] ),
  print ''
 
  rank = subset_gray_rank ( n, a )
 
  print ''
  print '  The rank is %d' % ( rank )
#
#  Terminate.
#
  print ''
  print 'SUBSET_GRAY_RANK_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  subset_gray_rank_test ( )
  timestamp ( )

