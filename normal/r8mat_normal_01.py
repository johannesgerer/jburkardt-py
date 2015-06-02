#!/usr/bin/env python

def r8mat_normal_01 ( m, n, seed ):

#*****************************************************************************80
#
## R8MAT_NORMAL_01 returns a unit pseudonormal R8MAT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    04 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, N, the number of rows and columns.
#
#    Input, integer SEED, a seed for the random number generator.
#
#    Output, real X(M,N), the pseudorandom values.
#
#    Output, integer SEED, an updated seed for the random number generator.
#
  import numpy as np
  from r8_normal_01 import r8_normal_01

  x = np.zeros ( ( m, n ) )

  for i in range ( 0, m ):
    for j in range ( 0, n ):
      x[i,j], seed = r8_normal_01 ( seed )

  return x, seed

def r8mat_normal_01_test ( ):

#*****************************************************************************80
#
## R8MAT_NORMAL_01_TEST tests R8MAT_NORMAL_01.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    04 March 2015
#
#  Author:
#
#    John Burkardt
#
  from r8mat_print import r8mat_print
  import numpy as np

  m = 5
  n = 4
  seed = 123456789

  print ''
  print 'R8MAT_NORMAL_01_TEST'
  print '  R8MAT_NORMAL_01 returns a matrix of Normal 01 values'
  print ''
  print '  SEED = %d' % ( seed )

  r, seed = r8mat_normal_01 ( m, n, seed )

  r8mat_print ( m, n, r, '  Matrix:' )

  print ''
  print 'R8MAT_NORMAL_01_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8mat_normal_01_test ( )
  timestamp ( )

