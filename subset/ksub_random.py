#!/usr/bin/env python

def ksub_random ( n, k, seed ):

#*****************************************************************************80
#
## KSUB_RANDOM selects a random subset of size K from a set of size N.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    19 December 2014
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
#    Input, integer N, the size of the set from which subsets are drawn.
#
#    Input, integer K, number of elements in desired subsets.  K must
#    be between 0 and N.
#
#    Input, integer SEED, a seed for the random number generator.
#
#    Output, integer A(K).  A(I) is the I-th element of the
#    output set.  The elements of A are in order.
#
#    Output, integer SEED, an updated seed for the random number generator.
#
  import numpy as np
  from i4_uniform_ab import i4_uniform_ab
  from math import floor
  from sys import exit

  if ( k <= 0 ):
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

  for i in range ( 1, k + 1 ):
    a[i-1] = ( ( ( i - 1 ) * n ) // k )

  for i in range ( 1, k + 1 ):

    while ( True ):

      ix, seed = i4_uniform_ab ( 1, n, seed )

      l = ( ( ix * k - 1 ) // n )

      if ( a[l-1] < ix ):
        break

    a[l-1] = a[l-1] + 1

  ip = 0
  iq = k

  for i in range ( 1, k + 1 ):

    m = a[i-1]
    a[i-1] = 0

    if ( m != ( ( ( i - 1 ) * n ) / k ) ):
      ip = ip + 1
      a[ip-1] = m

  ihi = ip

  for i in range ( 1, ihi + 1 ):

    ip = ihi + 1 - i
    l = 1 + ( ( a[ip-1] * k - 1 ) // n )
    ids = a[ip-1] - ( ( ( l - 1 ) * n ) // k )
    a[ip-1] = 0
    a[iq-1] = l
    iq = iq - ids

  for ll in range ( 1, k + 1 ):

    l = k + 1 - ll

    if ( a[l-1] != 0 ):
      ir = l
      m0 = 1 + ( ( ( a[l-1] - 1 ) * n ) // k )
      m = ( ( a[l-1] * n ) // k ) - m0 + 1

    ix, seed = i4_uniform_ab ( m0, m0 + m - 1, seed )

    i = l + 1

    while ( i <= ir ):

      if ( ix < a[i-1] ):
        break

      ix = ix + 1
      a[i-2] = a[i-1]
      i = i + 1

    a[i-2] = ix
    m = m - 1

  return a, seed

def ksub_random_test ( ):

#*****************************************************************************80
#
## KSUB_RANDOM_TEST tests KSUB_RANDOM.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    19 December 2014
#
#  Author:
#
#    John Burkardt
#
  k = 3
  n = 5

  print ''
  print 'KSUB_RANDOM_TEST'
  print '  KSUB_RANDOM generates a random K subset of an N set.'
  print '  Set size is N =    %d' % ( n )
  print '  Subset size is K = %d' % ( k )
  print ''

  seed = 123456789

  for i in range ( 0, 5 ):

    a, seed = ksub_random ( n, k, seed )

    for j in range ( 0, k ):
      print '  %3d' % ( a[j] ),
    print ''
#
#  Terminate.
#
  print ''
  print 'KSUB_RANDOM_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  ksub_random_test ( )
  timestamp ( )
