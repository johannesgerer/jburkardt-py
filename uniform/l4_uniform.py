#!/usr/bin/env python

def l4_uniform ( seed ):

#*****************************************************************************80
#
## L4_UNIFORM returns a pseudorandom L4.
#
#  Discussion:
#
#    An L4 is a LOGICAL value.
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
#    Input, integer SEED, the "seed" value, which should NOT be 0. 
#
#    Output, logical VALUE, a pseudorandom logical value.
#
#    Output, integer SEED, the updated seed value.
#
  from sys import exit

  i4_huge      = 2147483647
  i4_huge_half = 1073741823

  if ( seed < 0 ):
    seed = seed + i4_huge

  seed = ( seed % i4_huge )

  if ( seed == 0 ):
    print ''
    print 'L4_UNIFORM - Fatal error!'
    print '  Input value of SEED = 0.'
    exit ( 'L4_UNIFORM - Fatal error!' )

  k = ( seed // 127773 )

  seed = 16807 * ( seed - k * 127773 ) - k * 2836

  if ( seed < 0 ):
    seed = seed + i4_huge

  value = ( i4_huge_half < seed )

  return value, seed

def l4_uniform_test ( ):

#*****************************************************************************80
#
## L4_UNIFORM_TEST tests L4_UNIFORM.
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
  print ''
  print 'L4_UNIFORM_TEST'
  print '  L4_UNIFORM returns random logical values'
  print ''

  seed = 123456789

  for i in range ( 0, 10 ):
    l4, seed = l4_uniform ( seed )
    print '  %d' % ( l4 )

  print ''
  print 'L4_UNIFORM_TEST'
  print '  Normal end of execution'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  l4_uniform_test ( )
  timestamp ( )
