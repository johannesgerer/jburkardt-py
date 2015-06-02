#!/usr/bin/env python
#
def ytb_random ( n, lam, seed ):

#*****************************************************************************80
#
## YTB_RANDOM selects a random Young tableau of a given shape.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 May 2015
#
#  Author:
#
#    John Burkardt
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
#    Input, integer N, the integer which has been partitioned.
#
#    Input, integer LAM(N), the partition of N.
#    N = sum ( 1 <= I <= N ) LAM(I).
#
#    Input, integer SEED, a seed for the random number generator.
#
#    Output, integer A(N), the vector describing the Young tableau.
#
#    Output, integer SEED, an updated seed for the random number generator.
#
  import numpy as np
  from i4_uniform_ab import i4_uniform_ab

  a = np.zeros ( n )

  i = 0
  k = 0

  while ( True ):

    for j in range ( 0, lam[i] ):
      a[j] = a[j] + 1
      k = k + 1

    i = i + 1

    if ( n <= k ):
      break

  for m in range ( 0, n ):

    while ( True ):

      i, seed = i4_uniform_ab ( 1, a[0], seed )
      im1 = i - 1
      j, seed = i4_uniform_ab ( 1, lam[0], seed )
      jm1 = j - 1

      if ( i <= a[jm1] and j <= lam[im1] ):
        break

    while ( True ):

      ih = a[jm1] + lam[im1] - i - j

      if ( ih == 0 ):
        break;

      k, seed = i4_uniform_ab ( 1, ih, seed )

      if ( k <= lam[im1] - j ):
        j = j + k
        jm1 = j - 1
      else:
        i = k - lam[im1] + i + j
        im1 = i - 1

    lam[im1] = lam[im1] - 1
    a[jm1] = a[jm1] - 1
    a[n-1-m] = i

  for i in range ( 0, n ):
    lam[a[i]-1] = lam[a[i]-1] + 1

  return a, seed

def ytb_random_test ( ):

#*****************************************************************************80
#
## YTB_RANDOM_TEST tests YTB_RANDOM.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 May 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  from ytb_print import ytb_print

  print ''
  print 'YTB_RANDOM_TEST'
  print '  YTB_RANDOM generates a random Young tableau'

  n = 6
  lam = np.array ( [ 3, 2, 1, 0, 0, 0 ] )
  seed = 123456789

  for i in range ( 0, 5 ):
 
    a, seed = ytb_random ( n, lam, seed )
    ytb_print ( n, a, '' )
#
#  Terminate.
#
  print ''
  print 'YTB_RANDOM_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  ytb_random_test ( )
  timestamp ( )
