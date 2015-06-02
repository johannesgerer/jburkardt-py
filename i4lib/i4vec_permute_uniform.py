#! /usr/bin/env python
#
def i4vec_permute_uniform ( n, a, seed ):

#*****************************************************************************80
#
## I4VEC_PERMUTE_UNIFORM randomly permutes an I4VEC.
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
#  Parameters:
#
#    Input, integer N, the number of objects.
#
#    Input, integer A(N), the array to be permuted.
#
#    Input, integer SEED, a seed for the random number generator.
#
#    Output, integer A(N), the permuted array.
#
#    Output, integer SEED, a seed for the random number generator.
#
  from i4vec_permute import i4vec_permute
  from perm0_uniform import perm0_uniform

  p, seed = perm0_uniform ( n, seed )

  a = i4vec_permute ( n, p, a )

  return a, seed

def i4vec_permute_uniform_test ( ):

#*****************************************************************************80
#
## I4VEC_PERMUTE_UNIFORM_TEST tests I4VEC_PERMUTE_UNIFORM.
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
  import numpy as np
  from i4vec_print import i4vec_print

  n = 12
  seed = 123456789

  print ''
  print 'I4VEC_PERMUTE_UNIFORM_TEST'
  print '  I4VEC_PERMUTE_UNIFORM randomly reorders an I4VEC.'

  a = np.zeros ( n )
  for i in range ( 0, n ):
    a[i] = 101 + i

  i4vec_print ( n, a, '  A, before rearrangement:' )

  a, seed = i4vec_permute_uniform ( n, a, seed )

  i4vec_print ( n, a, '  A, after rearrangement:' )
#
#  Terminate.
#
  print ''
  print 'I4VEC_PERMUTE_UNIFORM_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  i4vec_permute_uniform_test ( )
  timestamp ( )
