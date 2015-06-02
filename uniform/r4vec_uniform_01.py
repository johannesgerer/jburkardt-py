#!/usr/bin/env python

def r4vec_uniform_01 ( n, seed ):

#*****************************************************************************80
#
## R4VEC_UNIFORM_01 returns a unit pseudorandom R4VEC.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    25 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Paul Bratley, Bennett Fox, Linus Schrage,
#    A Guide to Simulation,
#    Second Edition,
#    Springer, 1987,
#    ISBN: 0387964673,
#    LC: QA76.9.C65.B73.
#
#    Bennett Fox,
#    Algorithm 647:
#    Implementation and Relative Efficiency of Quasirandom
#    Sequence Generators,
#    ACM Transactions on Mathematical Software,
#    Volume 12, Number 4, December 1986, pages 362-376.
#
#    Pierre L'Ecuyer,
#    Random Number Generation,
#    in Handbook of Simulation,
#    edited by Jerry Banks,
#    Wiley, 1998,
#    ISBN: 0471134031,
#    LC: T57.62.H37.
#
#    Peter Lewis, Allen Goodman, James Miller,
#    A Pseudo-Random Number Generator for the System/360,
#    IBM Systems Journal,
#    Volume 8, Number 2, 1969, pages 136-143.
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
  import numpy
  from sys import exit

  i4_huge = 2147483647;

  if ( seed < 0 ):
    seed = seed + i4_huge

  if ( seed == 0 ):
    print ''
    print 'R4VEC_UNIFORM_01 - Fatal error!'
    print '  Input SEED = 0!'
    exit ( 'R4VEC_UNIFORM_01 - Fatal error!' )

  x = numpy.zeros ( n );

  for i in range ( 0, n ):

    k = ( seed // 127773 )

    seed = 16807 * ( seed - k * 127773 ) - k * 2836

    if ( seed < 0 ):
      seed = seed + i4_huge

    x[i] = seed * 4.656612875E-10

  return x, seed

def r4vec_uniform_01_test ( ):

#*****************************************************************************80
#
## R4VEC_UNIFORM_01_TEST tests R4VEC_UNIFORM_01.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    25 December 2014
#
#  Author:
#
#    John Burkardt
#
  from r4vec_print import r4vec_print
  import numpy as np

  n = 10
  seed = 123456789

  print ''
  print 'R4VEC_UNIFORM_01_TEST'
  print '  R4VEC_UNIFORM_01 computes a random R4VEC.'
  print ''
  print '  Initial seed is %d' % ( seed )

  v, seed = r4vec_uniform_01 ( n, seed )

  r4vec_print ( n, v, '  Uniform R4VEC:' )

  print ''
  print 'R4VEC_UNIFORM_01_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r4vec_uniform_01_test ( )
  timestamp ( )

