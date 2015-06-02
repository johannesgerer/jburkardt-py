#! /usr/bin/env python
#
def equiv_random ( n, seed ):

#*****************************************************************************80
#
## EQUIV_RANDOM selects a random partition of a set.
#
#  Discussion:
#
#    The user does not control the number of parts in the partition.
#
#    The equivalence classes are numbered in no particular order.
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
#    Input, integer N, the number of elements in the set to be partitioned.
#
#    Input, integer SEED, a seed for the random number generator.
#
#    Output, integer NPART, the number of classes or parts in the 
#    partition.  NPART will be between 1 and N.
#
#    Output, integer A(N), indicates the class to which each element
#    is assigned.
#
#    Output, integer SEED, an updated seed for the random number generator.
#
  import numpy as np
  from i4_uniform_ab import i4_uniform_ab
  from r8_uniform_01 import r8_uniform_01

  b = np.zeros ( n )

  b[0] = 1.0

  for l in range ( 1, n ):

    sum1 = 1.0 / float ( l )
    for k in range ( 1, l ):
      sum1 = ( sum1 + b[k-1] ) / float ( l - k )

    b[l] = ( sum1 + b[l-1] ) / float ( l + 1 )

  a = np.zeros ( n, dtype = np.int32 )

  m = n
  npart = 0

  while ( True ):

    z, seed = r8_uniform_01 ( seed )
    z = m * b[m-1] * z
    k = 0
    npart = npart + 1

    while ( 0.0 <= z ):

      a[m-1] = npart
      m = m - 1

      if ( m == 0 ):
        break

      z = z - b[m-1]
      k = k + 1
      z = z * k

    if ( m == 0 ):
      break
#
#  Randomly permute the assignments.
#
  for i in range ( 1, n ):
    j, seed = i4_uniform_ab ( i, n, seed )
    t      = a[i-1]
    a[i-1] = a[j-1]
    a[j-1] = t

  return npart, a, seed

def equiv_random_test ( ):

#*****************************************************************************80
#
## EQUIV_RANDOM_TEST tests EQUIV_RANDOM.
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
  from equiv_print2 import equiv_print2

  n = 4

  print ''
  print 'EQUIV_RANDOM_TEST'
  print '  EQUIV_RANDOM selects a random set partition.'
 
  seed = 123456789

  for i in range ( 0, 5 ):
 
    npart, a, seed = equiv_random ( n, seed )

    equiv_print2 ( n, a, '  The partition:' )
#
#  Terminate.
#
  print ''
  print 'EQUIV_RANDOM_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  equiv_random_test ( )
  timestamp ( )


