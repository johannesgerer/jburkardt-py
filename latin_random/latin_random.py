## /usr/bin/env python
#

def latin_random ( dim_num, point_num, seed ):

#*****************************************************************************80
#
## LATIN_RANDOM returns points in a Latin Random square.
#
#  Discussion:
#
#    In each spatial dimension, there will be exactly one
#    point whose coordinate value lies between consecutive
#    values in the list:
#
#      ( 0, 1, 2, ..., point_num ) / point_num
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 November 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer DIM_NUM, the spatial dimension.
#
#    Input, integer POINT_NUM, the number of points.
#
#    Input/output, integer SEED, a seed for the random
#    number generator.
#
#    Output, real X(DIM_NUM,POINT_NUM), the points.
#
  from perm_uniform import perm_uniform
  from r8mat_uniform_01 import r8mat_uniform_01
#
#  Pick DIM_NUM * POINT_NUM random numbers between 0 and 1.
#
  x, seed = r8mat_uniform_01 ( dim_num, point_num, seed )
#
#  For spatial dimension I,
#    pick a random permutation of 1 to POINT_NUM,
#    force the corresponding I-th components of X to lie in the
#    interval ( PERM(J)-1, PERM(J) ) / POINT_NUM.
#
  for i in range ( 0, dim_num ):

    perm, seed = perm_uniform ( point_num, seed )

    for j in range ( 0, point_num ):

      x[i,j] = ( perm[j] + x[i,j] ) / point_num

  return x, seed

def latin_random_test ( seed ):

#*****************************************************************************80
#
## TEST01 tests LATIN_RANDOM.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 November 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input/output, integer SEED, a seed for the random number
#    generator.
#
  from r8mat_transpose_print import r8mat_transpose_print

  dim_num = 2
  point_num = 10

  print ''
  print 'LATIN_RANDOM_TEST'
  print '  LATIN_RANDOM chooses a random Latin Square'
  print '  cell arrangement, and then returns'
  print '  a random point from each cell.'
  print ' '
  print '  Spatial dimension =  %d' % ( dim_num )
  print '  Number of points =   %d' % ( point_num )
  print '  Random number SEED = %d' % ( seed )

  x, seed = latin_random ( dim_num, point_num, seed )

  r8mat_transpose_print ( dim_num, point_num, x, \
    '  The Latin Random Square points:' )

  print ''
  print 'LATIN_RANDOM_TEST'
  print '  Normal end of execution.'

  return seed

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  seed = 123456789
  for test in range ( 0, 3 ):
    seed = latin_random_test ( seed )
  timestamp ( )

