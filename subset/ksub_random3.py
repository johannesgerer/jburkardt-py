#!/usr/bin/env python

def ksub_random3 ( n, k, seed ):

#*****************************************************************************80
#
## KSUB_RANDOM3 selects a random subset of size K from a set of size N.
#
#  Discussion:
#
#    This routine uses Floyd's algorithm.
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
#  Parameters:
#
#    Input, integer N, the size of the set from which subsets are drawn.
#
#    Input, integer K, number of elements in desired subsets.  K must
#    be between 0 and N.
#
#    Input, integer SEED, a seed for the random number generator.
#
#    Output, integer A(N).  I is an element of the subset
#    if A(I) = 1, and I is not an element if A(I)=0.
#
#    Output, integer SEED, an updated seed for the random number generator.
#
  import numpy as np
  from i4_uniform_ab import i4_uniform_ab
  from sys import exit

  if ( k < 0 ):
    print ''
    print 'KSUB_RANDOM3 - Fatal error!'
    print '  K = %d' % ( k )
    print '  but 0 < K is required!'
    exit ( 'KSUB_RANDOM3 - Fatal error!' )

  if ( n < k ):
    print ''
    print 'KSUB_RANDOM3 - Fatal error!'
    print '  N = %d' % ( n )
    print '  K = %d' % ( k )
    print '  K <= N is required!'
    exit ( 'KSUB_RANDOM3 - Fatal error!' )

  a = np.zeros ( n )

  for i in range ( n - k, n ):

    j, seed = i4_uniform_ab ( 0, i, seed )

    if ( a[j] == 0 ):
      a[j] = 1
    else:
      a[i] = 1

  return a, seed

def ksub_random3_test ( ):

#*****************************************************************************80
#
## KSUB_RANDOM3_TEST tests KSUB_RANDOM3.
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
  n = 5

  print ''
  print 'KSUB_RANDOM3_TEST'
  print '  KSUB_RANDOM3 generates a random K subset of an N set.'
  print '  Set size is N =    %d' % ( n )
  print '  Subset size is K = %d' % ( k )
  print ''

  seed = 123456789

  for i in range ( 0, 10 ):

    a, seed = ksub_random3 ( n, k, seed )

    for j in range ( 0, n ):
      print '  %3d' % ( a[j] ),
    print ''
#
#  Terminate.
#
  print ''
  print 'KSUB_RANDOM3_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  ksub_random3_test ( )
  timestamp ( )
