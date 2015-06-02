#!/usr/bin/env python

def perm0_uniform ( n, seed ):

#*****************************************************************************80
#
## PERM0_UNIFORM selects a random permutation of 0, ..., N-1.
#
#  Discussion:
#
#    An I4VEC is a vector of I4 values.
#
#    The algorithm is known as the Fisher-Yates or Knuth shuffle.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 October 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of entries in the vector.
#
#    Input, integer SEED, a seed for the random number generator.
#
#    Output, integer P[N], a permutation of the digits 0 through N-1.
#
#    Output, integer SEED, an updated seed.
#
  from i4_uniform_ab import i4_uniform_ab
  import numpy as np

  p = np.zeros ( n, dtype = np.int32 )

  for i in range ( 0, n ):
    p[i] = i

  for i in range ( 0, n - 1 ):
    j, seed = i4_uniform_ab ( i, n - 1, seed )
    k    = p[i]
    p[i] = p[j]
    p[j] = k

  return p, seed

def perm0_uniform_test ( ):

#*****************************************************************************80
#
## PERM0_UNIFORM_TEST tests PERM0_UNIFORM.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    23 May 2015
#
#  Author:
#
#    John Burkardt
#
  n = 10

  print ''
  print 'PERM0_UNIFORM_TEST'
  print '  PERM0_UNIFORM randomly selects a permutation of 0, ..., N-1.'
  print ''

  seed = 123456789;

  for test in range ( 0, 5 ):
    p, seed = perm0_uniform ( n, seed )
    print '  ',
    for i in range ( 0, n ):
      print '%4d' % ( p[i] ),
    print ''
#
#  Terminate.
#
  print ''
  print 'PERM0_UNIFORM_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  perm0_uniform_test ( )
  timestamp ( )
