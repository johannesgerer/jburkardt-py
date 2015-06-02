#!/usr/bin/env python

def i4vec_uniform_ab ( n, a, b, seed ):

#*****************************************************************************80
#
## I4VEC_UNIFORM_AB returns a scaled pseudorandom I4VEC.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    05 April 2013
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
#    Input, integer A, B, the minimum and maximum acceptable values.
#
#    Input, integer SEED, a seed for the random number generator.
#
#    Output, integer C(N), the randomly chosen integer vector.
#
#    Output, integer SEED, the updated seed.
#
  import numpy
  from math import floor
  from sys import exit

  i4_huge = 2147483647

  seed = floor ( seed  )

  if ( seed < 0 ):
    seed = seed + i4_huge

  if ( seed == 0 ):
    print ''
    print 'I4VEC_UNIFORM_AB - Fatal error!'
    print '  Input SEED = 0!'
    exit ( 'I4VEC_UNIFORM_AB - Fatal error!' )

  seed = floor ( seed )
  a = round ( a )
  b = round ( b )

  c = numpy.zeros ( n )

  for i in range ( 0, n ):

    k = floor ( seed / 127773 )

    seed = 16807 * ( seed - k * 127773 ) - k * 2836

    seed = ( seed % i4_huge )

    if ( seed < 0 ):
      seed = seed + i4_huge

    r = seed * 4.656612875E-10
#
#  Scale R to lie between A-0.5 and B+0.5.
#
    r = ( 1.0 - r ) * ( min ( a, b ) - 0.5 ) \
      +         r   * ( max ( a, b ) + 0.5 )
#
#  Use rounding to convert R to an integer between A and B.
#
    value = round ( r )

    value = max ( value, min ( a, b ) )
    value = min ( value, max ( a, b ) )

    c[i] = value

  return c, seed

def i4vec_uniform_ab_test ( ):

#*****************************************************************************80
#
## I4VEC_UNIFORM_AB_TEST tests I4VEC_UNIFORM_AB.
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
  a = -100
  b = 200
  seed = 123456789

  print ''
  print 'I4VEC_UNIFORM_AB_TEST'
  print '  I4VEC_UNIFORM_AB computes pseudorandom values'
  print '  in an interval [A,B].'
  print ''
  print '  The lower endpoint A = %d' % ( a )
  print '  The upper endpoint B = %d' % ( b )
  print '  The initial seed is %d' % ( seed )
  print ''

  v, seed = i4vec_uniform_ab ( n, a, b, seed )

  i4vec_print ( n, v, '  The random vector:' )

  print ''
  print 'I4VEC_UNIFORM_AB_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp

  timestamp ( )
  i4vec_uniform_ab_test ( )
  timestamp ( )

