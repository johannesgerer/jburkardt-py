#!/usr/bin/env python

def vibonacci ( n, seed ):

#*****************************************************************************80
#
## VIBONACCI computes the first N Vibonacci numbers.
#
#  Discussion:
#
#    The "Vibonacci numbers" are a generalization of the Fibonacci numbers:
#      V(N+1) = +/- V(N) +/- V(N-1)
#    where the signs are chosen randomly.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Brian Hayes,
#    The Vibonacci Numbers,
#    American Scientist,
#    July-August 1999, Volume 87, Number 4.
#
#    Divakar Viswanath,
#    Random Fibonacci sequences and the number 1.13198824,
#    Mathematics of Computation, 1998.
#
#  Parameters:
#
#    Input, integer N, the highest number to compute.
#
#    Input, integer SEED, a seed for the random number generator.
#
#    Output, integer V(N), the first N Vibonacci numbers.  By convention,
#    V(1) and V(2) are taken to be 1.
#
#    Output, integer SEED, an updated seed for the random number generator.
#
  import numpy as np
  from i4_uniform_ab import i4_uniform_ab

  v = np.zeros ( n )

  if ( n <= 0 ):
    return v
 
  v[0] = 1

  if ( n <= 1 ):
    return v

  v[1] = 1

  for i in range ( 2, n ):
   
    j, seed = i4_uniform_ab ( 0, 1, seed )

    if ( j == 0 ):
      s1 = -1
    else:
      s1 = +1

    j, seed = i4_uniform_ab ( 0, 1, seed )

    if ( j == 0 ):
      s2 = -1
    else:
      s2 = +1

    v[i] = s1 * v[i-1] + s2 * v[i-2]

  return v, seed

def vibonacci_test ( ):

#*****************************************************************************80
#
## VIBONACCI_TEST tests VIBONACCI.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    27 October 2014
#
#  Author:
#
#    John Burkardt
#
  from i4vec_print import i4vec_print

  n = 20
  n_time = 3

  print ''
  print 'VIBONACCI_TEST'
  print '  VIBONACCI computes a Vibonacci sequence.'
  print ''
  print '  Compute the series 3 times.'

  seed = 123456789
  v1, seed = vibonacci ( n, seed )
  v2, seed = vibonacci ( n, seed )
  v3, seed = vibonacci ( n, seed )

  print ''
  for i in range ( 0, n ):
    print '  %2d:  %6d  %6d  %6d' % ( i, v1[i], v2[i], v3[i] )

  print ''
  print 'I4_UNIFORM_AB_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp

  timestamp ( )
  vibonacci_test ( )
  timestamp ( )


