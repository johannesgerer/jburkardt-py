#!/usr/bin/env python

def ksub_random5 ( n, k, seed ):

#*****************************************************************************80
#
## KSUB_RANDOM5 selects a random subset of size K from a set of size N.
#
#  Discussion:
#
#    Consider the set A(1:N) = 1, 2, 3, ... N.
#    Choose a random index I1 between 1 and N, and swap items A(1) and A(I1).
#    Choose a random index I2 between 2 and N, and swap items A(2) and A(I2).
#    repeat K times.
#    A(1:K) is your random K-subset.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 June 2011
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the size of the set from which subsets
#    are drawn.
#
#    Input, integer K, number of elements in desired subsets.
#    1 <= K <= N.
#
#    Input/output, integer SEED, a seed for the random
#    number generator.
#
#    Output, integer A(K), the indices of the randomly
#    chosen elements.
#
  import numpy as np
  from i4_uniform_ab import i4_uniform_ab


#
#  Let B index the set.
#
  b = np.zeros ( n )
  for i in range ( 0, n ):
    b[i] = i
#
#  Choose item 1 from N things,
#  choose item 2 from N-1 things,
#  choose item K from N-K+1 things.
#
  for i in range ( 0, k ): 

    j, seed = i4_uniform_ab ( i, n - 1, seed )

    t    = b[i]
    b[i] = b[j]
    b[j] = t
#
#  Copy the first K elements.
#
  a = np.zeros ( k )
  for i in range ( 0, k ):
    a[i] = b[i]
#
#  Put the elements in ascending order.
#
  a = np.sort ( a )

  return a, seed

def ksub_random5_test ( ):

#*****************************************************************************80
#
## KSUB_RANDOM5_TEST tests KSUB_RANDOM5.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 May 2015
#
#  Author:
#
#    John Burkardt
#
  k = 3
  n = 100

  print ''
  print 'KSUB_RANDOM5_TEST'
  print '  KSUB_RANDOM5 generates a random K subset of an N set.'
  print '  Set size is N =    %d' % ( n )
  print '  Subset size is K = %d' % ( k )
  print ''

  seed = 123456789

  for i in range ( 0, 10 ):

    a, seed = ksub_random5 ( n, k, seed )

    for j in range ( 0, k ):
      print '  %3d' % ( a[j] ),
    print ''
#
#  Terminate.
#
  print ''
  print 'KSUB_RANDOM5_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  ksub_random5_test ( )
  timestamp ( )
