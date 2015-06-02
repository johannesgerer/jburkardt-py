#!/usr/bin/env python

def l4mat_uniform ( m, n, seed ):

#*****************************************************************************80
#
## L4MAT_UNIFORM returns a pseudorandom L4MAT.
#
#  Discussion:
#
#    An L4MAT is a two dimensional array of LOGICAL values.
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
#    Input, integer M, N, the order of the matrix.
#
#    Input/output, integer SEED, the "seed" value, which should
#    NOT be 0.  On output, SEED has been updated.
#
#    Output, logical L4MAT(M,N), a pseudorandom logical matrix.
#
  import numpy
  from sys import exit

  i4_huge      = 2147483647
  i4_huge_half = 1073741823

  if ( seed < 0 ):
    seed = seed + i4_huge

  if ( seed == 0 ):
    print ''
    print 'L4MAT_UNIFORM - Fatal error!'
    print '  Input value of SEED = 0.'
    exit ( 'L4MAT_UNIFORM - Fatal error!' )

  l4mat = numpy.zeros ( ( m, n ) )

  for j in range ( 0, n ):

    for i in range ( 0, m ):

      k = ( seed // 127773 )

      seed = 16807 * ( seed - k * 127773 ) - k * 2836

      if ( seed < 0 ):
        seed = seed + i4_huge

      l4mat[i][j] = ( i4_huge_half < seed )

  return l4mat, seed

def l4mat_uniform_test ( ):

#*****************************************************************************80
#
## L4MAT_UNIFORM_TEST tests L4MAT_UNIFORM.
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
  from l4mat_print import l4mat_print
  import numpy as np

  m = 5
  n = 4
  seed = 123456789

  print ''
  print 'L4MAT_UNIFORM_TEST'
  print '  L4MAT_UNIFORM computes a random L4MAT.'
  print ''
  print '  Initial seed is %d' % ( seed )

  v, seed = l4mat_uniform ( m, n, seed )

  l4mat_print ( m, n, v, '  Random L4MAT:' )

  print ''
  print 'L4MAT_UNIFORM_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  l4mat_uniform_test ( )
  timestamp ( )

