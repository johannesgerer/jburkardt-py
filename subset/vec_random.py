#!/usr/bin/env python

def vec_random ( n, base, seed ):

#*****************************************************************************80
#
## VEC_RANDOM selects a random N-vector of integers modulo a given base.
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
#  Parameters:
#
#    Input, integer N, the size of the vector to be generated.
#
#    Input, integer BASE, the base to be used.
#
#    Input, integer SEED, a random number seed.
#
#    Output, integer A(N), a list of N random values between
#    0 and BASE-1.
#
#    Input, integer SEED, an updated random number seed.
#
  import numpy as np
  from i4_uniform_ab import i4_uniform_ab

  a = np.zeros ( n )
  i4_lo = 0
  i4_hi = base - 1

  for i in range ( 0, n ):
    a[i], seed = i4_uniform_ab ( i4_lo, i4_hi, seed )

  return a, seed

def vec_random_test ( ):

#*****************************************************************************80
#
## VEC_RANDOM_TEST tests VEC_RANDOM.
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
  n = 3
  base = 3
  seed = 123456789

  print ''
  print 'VEC_RANDOM_TEST'
  print '  VEC_RANDOM generates a random N-vector'
  print '  in a given base.'
  print '  Here, we use base %d' % ( base )
  print ''

  for i in range ( 0, 5 ):
    a, seed = vec_random ( n, base, seed )
    for j in range ( 0, n ): 
      print '  %2d' % ( a[j] ),
    print ''
#
#  Terminate.
#
  print ''
  print 'VEC_RANDOM_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  vec_random_test ( )
  timestamp ( )
