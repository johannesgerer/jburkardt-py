#! /usr/bin/env python
#
def ksub_unrank ( k, rank ):

#*****************************************************************************80
#
## KSUB_UNRANK returns the subset of a given rank.
#
#  Discussion:
#
#    The routine is given a rank and returns the corresponding subset of K
#    elements of a set of N elements.  
#
#    It uses the same ranking that KSUB_NEXT2 uses to generate all the subsets 
#    one at a time.  
#
#    Note that the value of N itself is not input, nor is it needed.
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
#    Input, integer RANK, the rank of the desired subset.
#    There are ( N*(N-1)*...*(N+K-1)) / ( K*(K-1)*...*2*1) such
#    subsets, so RANK must be between 1 and that value.
#
#    Output, integer A(K), K distinct integers in order between
#    1 and N, which define the subset.
#
  import numpy as np

  a = np.zeros ( k )

  jrank = rank - 1

  for i in range ( k, 0, -1 ):

    ip = i - 1
    iprod = 1

    while ( True ):

      ip = ip + 1

      if ( ip != i ):
        iprod = ( ( ip * iprod ) // ( ip - i ) )

      if ( jrank < iprod ):
        break

    if ( ip != i ):
      iprod = ( ( ( ip - i ) * iprod ) // ip )

    jrank = jrank - iprod
    a[i-1] = ip

  return a

def ksub_unrank_test ( ):

#*****************************************************************************80
#
## KSUB_UNRANK_TEST tests KSUB_UNRANK.
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
  n = 5

  k = 3
  rank = 8

  print ''
  print 'KSUB_UNRANK_TEST'
  print '  KSUB_UNRANK: find the K-subset of an N set'
  print '  of a given rank.'
  print ''
  print '  N is %d' % ( n )
  print '  K is %d' % ( k )
  print '  and the desired rank is %d' % ( rank )
 
  a = ksub_unrank ( k, rank )
 
  print ''
  print '  The subset of the given rank is:'
  for i in range ( 0, k ):
    print '  %2d' % ( a[i] ),
  print ''
#
#  Terminate.
#
  print ''
  print 'KSUB_UNRANK_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  ksub_unrank_test ( )
  timestamp ( )

