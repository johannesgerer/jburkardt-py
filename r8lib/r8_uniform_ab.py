#!/usr/bin/env python

def r8_uniform_ab ( a, b, seed ):

#*****************************************************************************80
#
## R8_UNIFORM_AB returns a scaled pseudorandom R8.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    04 April 2013
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
#    Input, real A, B, the minimum and maximum values.
#
#    Input, integer SEED, a seed for the random number generator.
#
#    Output, real R, the randomly chosen value.
#
#    Output, integer SEED, an updated seed for the random number generator.
#
  from math import floor
  from sys import exit

  i4_huge = 2147483647

  if ( seed == 0 ):
    print ''
    print 'R8_UNIFORM_AB - Fatal error!'
    print '  Input SEED = 0!'
    exit ( 'R8_UNIFORM_AB - Fatal error!' )

  seed = floor ( seed )

  seed = ( seed % i4_huge )

  if ( seed < 0 ):
    seed = seed + i4_huge

  k = floor ( seed / 127773 )

  seed = 16807 * ( seed - k * 127773 ) - k * 2836

  if ( seed < 0 ):
    seed = seed + i4_huge

  r = a + ( b - a ) * seed * 4.656612875E-10

  return r, seed

def r8_uniform_ab_test ( ):

#*****************************************************************************80
#
## R8_UNIFORM_AB_TEST tests R8_UNIFORM_AB.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 July 2014
#
#  Author:
#
#    John Burkardt
#
  a = 10.0
  b = 20.0

  print ''
  print 'R8_UNIFORM_AB_TEST'
  print '  R8_UNIFORM_AB returns random values in a given range:'
  print '  [ A, B ]'
  print ''
  print '  For this problem:'
  print '  A = %f' % ( a )
  print '  B = %f' % ( b )
  print ''

  seed = 123456789

  for i in range ( 0, 10 ):
    r, seed = r8_uniform_ab ( a, b, seed )
    print '  %f' % ( r )
#
#  Terminate.
#
  print ''
  print 'R8_UNIFORM_AB_TEST'
  print '  Normal end of execution'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8_uniform_ab_test ( )
  timestamp ( )
