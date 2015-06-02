#!/usr/bin/env python

def r8vec_uniform_abvec ( n, a, b, seed ):

#*****************************************************************************80
#
## R8VEC_UNIFORM_AB returns a scaled pseudorandom R8VEC.
#
#  Discussion:
#
#    Dimension I ranges from A(I) to B(I).
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 April 2013
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
#    Input, real A(N), B(N), the range of the pseudorandom values.
#
#    Input, integer SEED, a seed for the random number generator.
#
#    Output, real X(N), the vector of pseudorandom values.
#
#    Output, integer SEED, an updated seed for the random number generator.
#
  import numpy
  from sys import exit

  i4_huge = 2147483647

  if ( seed < 0 ):
    seed = seed + i4_huge

  if ( seed == 0 ):
    print ''
    print 'R8VEC_UNIFORM_ABVEC - Fatal error!'
    print '  Input SEED = 0!'
    exit ( 'R8VEC_UNIFORM_ABVEC - Fatal error!' )

  x = numpy.zeros ( n )

  for i in range ( 0, n ):

    k = ( seed // 127773 )

    seed = 16807 * ( seed - k * 127773 ) - k * 2836

    if ( seed < 0 ):
      seed = seed + i4_huge

    x[i] = a[i] + ( b[i] - a[i] ) * seed * 4.656612875E-10

  return x, seed

def r8vec_uniform_abvec_test ( ):

#*****************************************************************************80
#
## R8VEC_UNIFORM_ABVEC_TEST tests R8VEC_UNIFORM_ABVEC.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    28 December 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 5
  a = np.array ( (  0.0, 0.20, 10.0, 52.0, -1.0 ) )
  b = np.array ( ( +1.0, 0.25, 20.0, 54.0, +1.0 ) )
  seed = 123456789

  print ''
  print 'R8VEC_UNIFORM_ABVEC_TEST'
  print '  R8VEC_UNIFORM_ABVEC computes a random R8VEC.'
  print ''
  print '  Initial seed is %d' % ( seed )

  v, seed = r8vec_uniform_abvec ( n, a, b, seed )

  print ''
  print '   I         A         X         B'
  print ''
  for i in range ( 0, n ):
    print '  %4d  %10g  %10g  %10g' % ( i, a[i], v[i], b[i] )
  print ''

  print ''
  print 'R8VEC_UNIFORM_ABVEC_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8vec_uniform_abvec_test ( )
  timestamp ( )

