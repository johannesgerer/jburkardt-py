#!/usr/bin/env python

def subset_random ( n, seed ):

#*****************************************************************************80
#
## SUBSET_RANDOM selects a random subset of an N-set.
#
#  Example:
#
#    N = 4
#
#    0 0 1 1
#    0 1 0 1
#    1 1 0 1
#    0 0 1 0
#    0 0 0 1
#    1 1 0 0
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
#    Input, integer N, the size of the full set.
#
#    Input, integer SEED, a seed for the random number generator.
#
#    Output, integer A(N).  A vector to hold the information about
#    the set chosen.  On return, if A(I) = 1, then
#    I is in the random subset, otherwise, A(I) = 0
#    and I is not in the random subset.
#
#    Output, integer SEED, an updated seed for the random number generator.
#
  import numpy as np
  from i4_uniform_ab import i4_uniform_ab

  a = np.zeros ( n )

  i4_lo = 0
  i4_hi = 1
  for i in range ( 0, n ):
    a[i], seed = i4_uniform_ab ( i4_lo, i4_hi, seed )

  return a, seed

def subset_random_test ( ):

#*****************************************************************************80
#
## SUBSET_RANDOM_TEST tests SUBSET_RANDOM.
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
  n = 5

  print ''
  print 'SUBSET_RANDOM_TEST'
  print '  SUBSET_RANDOM randomly selects a subset.'
  print '  The number of elements in the set is %d' % ( n )
  print ''

  seed = 123456789;

  for test in range ( 0, 5 ):
    a, seed = subset_random ( n, seed )
    print '  ',
    for i in range ( 0, n ):
      print '%4d' % ( a[i] ),
    print ''
#
#  Terminate.
#
  print ''
  print 'SUBSET_RANDOM_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  subset_random_test ( )
  timestamp ( )
