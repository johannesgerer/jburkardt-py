#!/usr/bin/env python

def r8vec_uniform_ab ( n, a, b, seed ):

#*****************************************************************************80
#
## R8VEC_UNIFORM_AB returns a scaled pseudorandom R8VEC.
#
#  Discussion:
#
#    Each dimension ranges from A to B.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    29 October 2014
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Paul Bratley, Bennett Fox, Linus Schrage,
#    A Guide to Simulation,
#    Springer Verlag, pages 201-202, 1983.
#
#    Bennett Fox,
#    Algorithm 647:
#    Implementation and Relative Efficiency of Quasirandom
#    Sequence Generators,
#    ACM Transactions on Mathematical Software,
#    Volume 12, Number 4, pages 362-376, 1986.
#
#    Peter Lewis, Allen Goodman, James Miller,
#    A Pseudo-Random Number Generator for the System/360,
#    IBM Systems Journal,
#    Volume 8, pages 136-143, 1969.
#
#  Parameters:
#
#    Input, integer N, the number of entries in the vector.
#
#    Input, real A, B, the range of the pseudorandom values.
#
#    Input, integer SEED, a seed for the random number generator.
#
#    Output, real X(N), the vector of pseudorandom values.
#
#    Output, integer SEED, an updated seed for the random number generator.
#
  from math import floor
  import numpy
  from sys import exit

  i4_huge = 2147483647

  seed = floor ( seed )

  if ( seed < 0 ):
    seed = seed + i4_huge

  if ( seed == 0 ):
    print ''
    print 'R8VEC_UNIFORM_AB - Fatal error!'
    print '  Input SEED = 0!'
    exit ( 'R8VEC_UNIFORM_AB - Fatal error!' )

  x = numpy.zeros ( n )

  for i in range ( 0, n ):

    k = floor ( seed / 127773 )

    seed = 16807 * ( seed - k * 127773 ) - k * 2836

    if ( seed < 0 ):
      seed = seed + i4_huge

    x[i] = a + ( b - a ) * seed * 4.656612875E-10

  return x, seed

def r8vec_uniform_ab_test ( ):

#*****************************************************************************80
#
## R8VEC_UNIFORM_AB_TEST tests R8VEC_UNIFORM_AB.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    29 October 2014
#
#  Author:
#
#    John Burkardt
#
  from r8vec_print import r8vec_print
  import numpy as np

  n = 10
  a = -1.0
  b = +5.0
  seed = 123456789

  print ''
  print 'R8VEC_UNIFORM_AB_TEST'
  print '  R8VEC_UNIFORM_AB computes a random R8VEC.'
  print ''
  print '  %g <= X <= %g' % ( a, b )
  print '  Initial seed is %d' % ( seed )

  v, seed = r8vec_uniform_ab ( n, a, b, seed )

  r8vec_print ( n, v, '  Random R8VEC:' )
#
#  Terminate.
#
  print ''
  print 'R8VEC_UNIFORM_AB_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8vec_uniform_ab_test ( )
  timestamp ( )

