#!/usr/bin/env python

def r8mat_normal_ab ( m, n, mu, sigma, seed ):

#*****************************************************************************80
#
## R8MAT_NORMAL_AB returns a scaled pseudonormal R8MAT.
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
#    Input, real MU, SIGMA, the mean and standard deviation.
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
      xi, seed = r8_normal_01 ( seed )
      x[i,j] = mu + sigma * xi

  return x, seed

def r8mat_normal_ab_test ( ):

#*****************************************************************************80
#
## R8MAT_NORMAL_AB_TEST tests R8MAT_NORMAL_AB.
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


  print ''
  print 'R8MAT_NORMAL_AB_TEST'
  print '  R8MAT_NORMAL_AB returns a matrix of Normal AB values'

  m = 5
  n = 4
  mu = 100.0
  sigma = 5.0
  seed = 123456789

  print ''
  print '  Mean = %g' % ( mu )
  print '  Standard deviation = %g' % ( sigma )
  print '  SEED = %d' % ( seed )

  r, seed = r8mat_normal_ab ( m, n, mu, sigma, seed )

  r8mat_print ( m, n, r, '  Matrix:' )

  print ''
  print 'R8MAT_NORMAL_AB_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8mat_normal_ab_test ( )
  timestamp ( )

