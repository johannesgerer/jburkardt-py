#! /usr/bin/env python
#
def comp_random ( n, k, seed ):

#*****************************************************************************80
#
## COMP_RANDOM selects a random composition of the integer N into K parts.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 April 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Albert Nijenhuis Herbert Wilf,
#    Combinatorial Algorithms,
#    Academic Press, 1978, second edition,
#    ISBN 0-12-519260-6.
#
#  Parameters:
#
#    Input, integer N, the integer to be decomposed.
#
#    Input, integer K, the number of parts in the composition.
#
#    Input, integer SEED, a seed for the random number generator.
#
#    Output, integer A(K), the parts of the composition.
#
#    Output, integer SEED, an updated seed for the random number generator.
#
  import numpy as np
  from ksub_random2 import ksub_random2

  b, seed = ksub_random2 ( n + k - 1, k - 1, seed )

  a = np.zeros ( k )
  for i in range ( 0, k - 1 ):
    a[i] = b[i]
  a[k-1] = n + k

  l = 0

  for i in range ( 0, k ):
    m = a[i]
    a[i] = a[i] - l - 1
    l = m

  return a, seed

def comp_random_test ( ):

#*****************************************************************************80
#
## COMP_RANDOM_TEST tests COMP_RANDOM.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 April 2015
#
#  Author:
#
#    John Burkardt
#
  k = 5

  print ''
  print 'COMP_RANDOM_TEST'
  print '  COMP_RANDOM generates random compositions.'
  print ''

  n = 10
  seed = 123456789

  for i in range ( 1, 6 ):
    a, seed = comp_random ( n, k, seed )
    for j in range ( 0, k ):
      print '  %2d' % ( a[j] ),
    print ''
#
#  Terminate.
#
  print ''
  print 'COMP_RANDOM_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  comp_random_test ( )
  timestamp ( )
