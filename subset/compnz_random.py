#!/usr/bin/env python

def compnz_random ( n, k, seed ):

#*****************************************************************************80
#
## COMPNZ_RANDOM selects a random composition of the integer N into K nonzero parts.
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
#  Reference:
#
#    Albert Nijenhuis and Herbert Wilf,
#    Combinatorial Algorithms,
#    Academic Press, 1978, second edition,
#    ISBN 0-12-519260-6.
#
#  Parameters:
#
#    Input, integer N, the integer to be decomposed.
#
#    Input, integer K, the number of parts in the composition.
#    K must be no greater than N.
#
#    Input, integer SEED, a seed for the random number generator.
#
#    Output, integer A(K), the parts of the composition.
#
#    Output, integer SEED, an updated seed for the random number generator.
#
  import numpy as np
  from ksub_random2 import ksub_random2

  a = np.zeros ( k, dtype = np.int32 )

  if ( 1 < n and 1 < k ):
    [ b, seed ] = ksub_random2 ( n - 1, k - 1, seed )

  for i in range ( 0, k - 1 ):
    a[i] = b[i]

  a[k-1] = n
  l = 0

  for i in range ( 0, k ):
    m = a[i]
    a[i] = a[i] - l - 1
    l = m

  for i in range ( 0, k ):
    a[i] = a[i] + 1

  return a, seed

def compnz_random_test ( ):

#*****************************************************************************80
#
## COMPNZ_RANDOM_TEST tests COMPNZ_RANDOM.
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
  k = 5
  n = 10
  seed = 123456789

  print ''
  print 'COMPNZ_RANDOM_TEST'
  print '  COMPNZ_RANDOM generates random compositions'
  print '  using nonzero parts.'
  print ''
  print '  Seeking random compositions of N = %d' % ( n )
  print '  using %d nonzero parts.' % ( k )
  print ''

  for i in range ( 0, 5 ):
    a, seed = compnz_random ( n, k, seed )
    for j in range ( 0, k ):
      print '  %2d' % ( a[j] ),
    print ''  
#
#  Terminate.
#
  print ''
  print 'COMPNZ_RANDOM_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  compnz_random_test ( )
  timestamp ( )
