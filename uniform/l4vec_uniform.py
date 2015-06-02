#!/usr/bin/env python

def l4vec_uniform ( n, seed ):

#*****************************************************************************80
#
## L4VEC_UNIFORM returns a pseudorandom L4VEC.
#
#  Discussion:
#
#    An L4VEC is a vector of LOGICAL values.
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
#    Input, integer N, the order of the vector.
#
#    Input, integer SEED, the "seed" value, which should NOT be 0.
#
#    Output, logical L4VEC(N), a pseudorandom logical vector.
#
#    Output, integer SEED, the updated seed.
#
  import numpy
  from sys import exit

  i4_huge      = 2147483647
  i4_huge_half = 1073741823

  if ( seed < 0 ):
    seed = seed + i4_huge

  if ( seed == 0 ):
    print ''
    print 'L4VEC_UNIFORM - Fatal error!'
    print '  Input value of SEED = 0.'
    exit ( 'L4VEC_UNIFORM - Fatal error!' )

  l4vec = numpy.zeros ( n )

  for i in range ( 0, n ):

    k = ( seed // 127773 )

    seed = 16807 * ( seed - k * 127773 ) - k * 2836

    if ( seed < 0 ):
      seed = seed + i4_huge

    l4vec[i] = ( i4_huge_half < seed )

  return l4vec, seed

def l4vec_uniform_test ( ):

#*****************************************************************************80
#
## L4VEC_UNIFORM_TEST tests L4VEC_UNIFORM.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    17 December 2014
#
#  Author:
#
#    John Burkardt
#
  from l4vec_print import l4vec_print
  import numpy as np

  n = 10
  seed = 123456789

  print ''
  print 'L4VEC_UNIFORM_TEST'
  print '  L4VEC_UNIFORM computes a random L4VEC.'
  print ''
  print '  Initial seed is %d' % ( seed )

  v, seed = l4vec_uniform ( n, seed )

  l4vec_print ( n, v, '  Random L4VEC:' )

  print ''
  print 'L4VEC_UNIFORM_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  l4vec_uniform_test ( )
  timestamp ( )

