#!/usr/bin/env python

def r8vec_normal_01 ( n, seed ):

#*****************************************************************************80
#
## R8VEC_NORMAL_01 returns a unit pseudonormal R8VEC.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    04 March 2015
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
#    Output, real X(N), the vector of pseudorandom values.
#
#    Output, integer SEED, an updated seed for the random number generator.
#
  import numpy as np
  from r8_normal_01 import r8_normal_01

  x = np.zeros ( n )

  for i in range ( 0, n ):
    x[i], seed = r8_normal_01 ( seed )

  return x, seed

def r8vec_normal_01_test ( ):

#*****************************************************************************80
#
## R8VEC_NORMAL_01_TEST tests R8VEC_NORMAL_01.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    04 March 2015
#
#  Author:
#
#    John Burkardt
#
  from r8vec_print import r8vec_print
  import numpy as np

  n = 10
  seed = 123456789

  print ''
  print 'R8VEC_NORMAL_01_TEST'
  print '  R8VEC_NORMAL_01 returns a vector of Normal 01 values'
  print ''
  print '  SEED = %d' % ( seed )

  r, seed = r8vec_normal_01 ( n, seed )

  r8vec_print ( n, r, '  Vector:' )

  print ''
  print 'R8VEC_NORMAL_01_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8vec_normal_01_test ( )
  timestamp ( )

