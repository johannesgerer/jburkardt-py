#!/usr/bin/env python

def ksub_random2 ( n, k, seed ):

#*****************************************************************************80
#
## KSUB_RANDOM2 selects a random subset of size K from a set of size N.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 December 2014
#
#  Author:
#
#    John Burkardt.
#
#  Reference:
#
#    A Nijenhuis and H Wilf,
#    Combinatorial Algorithms,
#    Academic Press, 1978, second edition,
#    ISBN 0-12-519260-6.
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
#    Output, integer A(K).  A(I) is the I-th element of the
#    output set.
#
#    Output, integer SEED, an updated seed for the random number generator.
#
  import numpy as np
  from r8_uniform_01 import r8_uniform_01
  from sys import exit

  if ( k < 0 ):
    print ''
    print 'KSUB_RANDOM - Fatal error!'
    print '  K = %d' % ( k )
    print '  but 0 < K is required!'
    exit ( 'KSUB_RANDOM - Fatal error!' )

  if ( n < k ):
    print ''
    print 'KSUB_RANDOM - Fatal error!'
    print '  N = %d' % ( n )
    print '  K = %d' % ( k )
    print '  K <= N is required!'
    exit ( 'KSUB_RANDOM - Fatal error!' )

  a = np.zeros ( k )

  if ( k == 0 ):
    return a

  need = k
  have = 0

  available = n
  candidate = 0

  while ( True ):

    candidate = candidate + 1

    r, seed = r8_uniform_01 ( seed )

    if ( available * r <= need ):

      need = need - 1;
      a[have] = candidate
      have = have + 1

      if ( need <= 0 ):
        break

    available = available - 1

  return a, seed

def ksub_random2_test ( ):

#*****************************************************************************80
#
## KSUB_RANDOM2_TEST tests KSUB_RANDOM2.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 December 2014
#
#  Author:
#
#    John Burkardt
#
  k = 3
  n = 5

  print ''
  print 'KSUB_RANDOM2_TEST'
  print '  KSUB_RANDOM2 generates a random K subset of an N set.'
  print '  Set size is N =    %d' % ( n )
  print '  Subset size is K = %d' % ( k )
  print ''

  seed = 123456789

  for i in range ( 0, 10 ):

    a, seed = ksub_random2 ( n, k, seed )

    for j in range ( 0, k ):
      print '  %3d' % ( a[j] ),
    print ''
#
#  Terminate.
#
  print ''
  print 'KSUB_RANDOM2_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  ksub_random2_test ( )
  timestamp ( )
