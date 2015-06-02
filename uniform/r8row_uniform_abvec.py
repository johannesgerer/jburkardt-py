#!/usr/bin/env python

def r8row_uniform_abvec ( m, n, a, b, seed ):

#*****************************************************************************80
#
## R8ROW_UNIFORM_ABVEC fills an R8ROW with scaled pseudorandom numbers.
#
#  Discussion:
#
#    An R8ROW is an array of R8 values, regarded as a set of row vectors.
#
#    The user specifies a minimum and maximum value for each column.
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
#    Input, integer M, N, the number of rows and columns in
#    the array.
#
#    Input, real A(N), B(N), the lower and upper limits.
#
#    Input/output, integer SEED, the "seed" value, which
#    should NOT be 0.  On output, SEED has been updated.
#
#    Output, real R(M,N), the array of pseudorandom values.
#
  import numpy
  from sys import exit

  i4_huge = 2147483647

  if ( seed < 0 ):
    seed = seed + i4_huge

  if ( seed == 0 ):
    print ''
    print 'R8ROW_UNIFORM_ABVEC - Fatal error!'
    print '  Input SEED = 0!'
    exit ( 'R8ROW_UNIFORM_ABVEC - Fatal error!' )

  r = numpy.zeros ( ( m, n ) )

  for i in range ( 0, m ):

    for j in range ( 0, n ):

      k = ( seed // 127773 )

      seed = 16807 * ( seed - k * 127773 ) - k * 2836

      seed = ( seed % i4_huge )

      if ( seed < 0 ):
        seed = seed + i4_huge;

      r[i][j] = a[j] + ( b[j] - a[j] ) * seed * 4.656612875E-10

  return r, seed

def r8row_uniform_abvec_test ( ):

#*****************************************************************************80
#
## R8ROW_UNIFORM_ABVEC_TEST tests R8ROW_UNIFORM_ABVEC.
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
  a = np.array ( ( -1.0, 0.0, 50.0, 100.0 ) )
  b = np.array ( ( +1.0, 1.0, 55.0, 100.1 ) )

  seed = 123456789

  print ''
  print 'R8ROW_UNIFORM_ABVEC_TEST'
  print '  R8ROW_UNIFORM_ABVEC computes a random scaled R8ROW.'
  print ''
  print '   Col         Min         Max'
  print ''
  for i in range ( 0, n ):
    print '  %4d  %10g  %10g' % ( i, a[i], b[i] )
  print ''
  print '  Initial seed is %d' % ( seed )

  v, seed = r8row_uniform_abvec ( m, n, a, b, seed )

  r8mat_print ( m, n, v, '  Random R8ROW:' )

  print ''
  print 'R8ROW_UNIFORM_ABVEC_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8row_uniform_abvec_test ( )
  timestamp ( )
