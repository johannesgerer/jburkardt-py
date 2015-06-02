#!/usr/bin/env python

def c8vec_uniform_01 ( n, seed ):

#*****************************************************************************80
#
## C8VEC_UNIFORM_01 returns a unit pseudorandom C8VEC.
#
#  Discussion:
#
#    The angles should be uniformly distributed between 0 and 2 * PI,
#    the square roots of the radius uniformly distributed between 0 and 1.
#
#    This results in a uniform distribution of values in the unit circle.
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
#    Input, integer N, the number of values to compute.
#
#    Input, integer SEED, a seed for the random number generator.
#
#    Output, complex C(N), the pseudorandom complex vector.
#
#    Output, integer SEED, a seed for the random number generator.
#
  import numpy
  from math import cos, floor, pi, sin, sqrt
  from sys import exit

  i4_huge = 2147483647

  seed = floor ( seed )

  if ( seed < 0 ):
    seed = seed + i4_huge

  if ( seed == 0 ):
    print ''
    print 'C8VEC_UNIFORM_01 - Fatal error!'
    print '  Input SEED = 0!'
    exit ( 'C8VEC_UNIFORM_01 - Fatal error!' )

  c = numpy.zeros ( n, 'complex' )

  for j in range ( 0, n ):

    k = floor ( seed / 127773 )

    seed = 16807 * ( seed - k * 127773 ) - k * 2836

    if ( seed < 0 ):
      seed = seed + i4_huge

    r = sqrt ( seed * 4.656612875E-10 )

    k = floor ( seed / 127773 )

    seed = 16807 * ( seed - k * 127773 ) - k * 2836

    if ( seed < 0 ):
      seed = seed + i4_huge

    theta = 2.0 * pi * seed * 4.656612875E-10

    c[j] = r * complex ( cos ( theta ), sin ( theta ) )

  return c, seed

def c8vec_uniform_01_test ( ):

#*****************************************************************************80
#
## C8VEC_UNIFORM_01_TEST tests C8VEC_UNIFORM_01.
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
  seed = 123456789

  print ''
  print 'C8VEC_UNIFORM_01_TEST'
  print '  C8VEC_UNIFORM_01 computes pseudorandom complex values'
  print '  in the unit circle.'

  print ''
  print '  The initial seed is %d' % ( seed )
  print ''

  n = 10

  [ x, seed ] = c8vec_uniform_01 ( n, seed )

  for i in range ( 0, n ):
    print '  %6d  ( %f, %f )' % ( i, x[i].real, x[i].imag )

  print ''
  print 'C8VEC_UNIFORM_01_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  c8vec_uniform_01_test ( )
  timestamp ( )


