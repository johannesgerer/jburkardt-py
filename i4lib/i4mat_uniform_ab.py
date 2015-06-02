#!/usr/bin/env python

def i4mat_uniform_ab ( m, n, a, b, seed ):

#*****************************************************************************80
#
## I4MAT_UNIFORM_AB returns a scaled pseudorandom I4MAT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    08 April 2013
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
#    Input, integer M, N, the row and column dimensions of the matrix.
#
#    Input, integer A, B, the minimum and maximum acceptable values.
#
#    Input, integer SEED, a seed for the random number generator.
#
#    Output, integer C(M,N), the randomly chosen integer vector.
#
#    Output, integer SEED, the updated seed.
#
  import numpy
  from sys import exit

  i4_huge = 2147483647

  if ( seed < 0 ):
    seed = seed + i4_huge

  if ( seed == 0 ):
    print ''
    print 'I4MAT_UNIFORM_AB - Fatal error!'
    print '  Input SEED = 0!'
    exit ( 'I4MAT_UNIFORM_AB - Fatal error!' )

  a = round ( a )
  b = round ( b )

  c = numpy.zeros ( ( m, n ) )

  for j in range ( 0, n ):

    for i in range ( 0, m ): 

      k =  ( seed // 127773 )

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

      c[i][j] = value

  return c, seed

def i4mat_uniform_ab_test ( ):

#*****************************************************************************80
#
## I4MAT_UNIFORM_AB_TEST tests I4MAT_UNIFORM_AB.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    31 October 2014
#
#  Author:
#
#    John Burkardt
#
  from i4mat_print import i4mat_print
  import numpy as np

  m = 5
  n = 4
  a = -1
  b = +5
  seed = 123456789

  print ''
  print 'I4MAT_UNIFORM_AB_TEST'
  print '  I4MAT_UNIFORM_AB computes a random R8MAT.'
  print ''
  print '  %d <= X <= %d' % ( a, b )
  print '  Initial seed is %d' % ( seed )

  v, seed = i4mat_uniform_ab ( m, n, a, b, seed )

  i4mat_print ( m, n, v, '  Random I4MAT:' )
#
#  Terminate.
#
  print ''
  print 'I4MAT_UNIFORM_AB_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  i4mat_uniform_ab_test ( )
  timestamp ( )
