#! /usr/bin/env python
#
def ksub_rank ( k, a ):

#*****************************************************************************80
#
## KSUB_RANK computes the rank of a K subset of an N set.
#
#  Discussion:
#
#    The routine accepts an array representing a subset of size K from a set
#    of size N, and returns the rank (or order) of that subset. 
#
#    It uses the same ranking that KSUB_NEXT2 uses to generate all the subsets 
#    one at a time.  
#
#    Note the value of N is not input, and is not, in fact,
#    needed.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 May 2015
#
#  Author:
#
#    John Burkardt.
#
#  Reference:
#
#    Albert Nijenhuis, Herbert Wilf,
#    Combinatorial Algorithms,
#    Academic Press, 1978, second edition,
#    ISBN 0-12-519260-6.
#
#  Parameters:
#
#    Input, integer K, the number of elements in the subset.
#
#    Input, integer A(K), contains K distinct numbers between
#    1 and N, in order.
#
#    Output, integer RANK, the rank of this subset.
#
  rank = 0

  for i in range ( 0, k ):

    iprod = 1

    for j in range ( i + 2, a[i] ):
      iprod = iprod * j

    for j in range ( 1, a[i] - i - 1 ):
      iprod =  ( iprod // j )

    if ( a[i] == 1 ):
      iprod = 0

    rank = rank + iprod

  rank = rank + 1

  return rank

def ksub_rank_test ( ):

#*****************************************************************************80
#
## KSUB_RANK_TEST tests KSUB_RANK.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 May 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 5
  k = 3
  a = np.array ( [ 1, 3, 5 ] )

  print ''
  print 'KSUB_RANK_TEST'
  print '  KSUB_RANK: rank of a K subset of an N set.'
  print ''
  print '  For N = %d' % ( n )
  print '  and K = %d' % ( k )
  print '  the subset is:'
  for i in range ( 0, k ):
    print '  %4d' % ( a[i] ),
  print ''
 
  rank = ksub_rank ( k, a )
 
  print ''
  print '  The rank is %d' % ( rank )
#
#  Terminate.
#
  print ''
  print 'KSUB_RANK_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  ksub_rank_test ( )
  timestamp ( )
