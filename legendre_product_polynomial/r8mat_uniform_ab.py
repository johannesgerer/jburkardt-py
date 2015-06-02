#!/usr/bin/env python

def r8mat_uniform_ab ( m, n, a, b, seed ):

#*****************************************************************************80
#
## R8MAT_UNIFORM_AB returns a scaled pseudorandom R8MAT.
#
#  Discussion:
#
#    An R8MAT is an array of R8's.
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
#    Input, integer M, N, the number of rows and columns in the array.
#
#    Input, real A, B, the range of the pseudorandom values.
#
#    Input, integer SEED, the integer "seed" used to generate
#    the output random number.
#
#    Output, real R(M,N), an array of random values between 0 and 1.
#
#    Output, integer SEED, the updated seed.  This would
#    normally be used as the input seed on the next call.
#
  import numpy
  from math import floor
  from sys import exit

  i4_huge = 2147483647

  seed = floor ( seed )

  if ( seed < 0 ):
    seed = seed + i4_huge

  if ( seed == 0 ):
    print ''
    print 'R8MAT_UNIFORM_AB - Fatal error!'
    print '  Input SEED = 0!'
    exit ( 'R8MAT_UNIFORM_AB - Fatal error!' )

  r = numpy.zeros ( ( m, n ) )

  for j in range ( 0, n ):
    for i in range ( 0, m ):

      k = floor ( seed / 127773 )

      seed = 16807 * ( seed - k * 127773 ) - k * 2836

      seed = floor ( seed )

      seed = ( seed % i4_huge )

      if ( seed < 0 ):
        seed = seed + i4_huge

      r[i][j] = a + ( b - a ) * seed * 4.656612875E-10

  return r, seed

def r8mat_uniform_ab_test ( ):

#*****************************************************************************80
#
## R8MAT_UNIFORM_AB_TEST tests R8MAT_UNIFORM_AB.
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
  from r8mat_print import r8mat_print
  import numpy as np

  m = 5
  n = 4
  a = -1.0
  b = +5.0
  seed = 123456789

  print ''
  print 'R8MAT_UNIFORM_AB_TEST'
  print '  R8MAT_UNIFORM_AB computes a random R8MAT.'
  print ''
  print '  %g <= X <= %g' % ( a, b )
  print '  Initial seed is %d' % ( seed )

  v, seed = r8mat_uniform_ab ( m, n, a, b, seed )

  r8mat_print ( m, n, v, '  Random R8MAT:' )

  print ''
  print 'R8MAT_UNIFORM_AB_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp

  timestamp ( )
  r8mat_uniform_ab_test ( )
  timestamp ( )


