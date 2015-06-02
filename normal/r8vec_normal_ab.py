#!/usr/bin/env python

def r8vec_normal_ab ( n, mu, sigma, seed ):

#*****************************************************************************80
#
## R8VEC_NORMAL_AB returns a scaled pseudonormal R8VEC.
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
#    Input, integer N, the number of entries in the vector.
#
#    Input, real MU, the average value of the PDF.
#
#    Input, real SIGMA, the standard deviation of the PDF.
#
#    Input, integer SEED, a seed for the random number generator.
#
#    Output, real X(N), the vector of pseudorandom values.
#
#    Output, integer SEED, an updated seed for the random number generator.
#
  import numpy as np
  from r8_normal_01 import r8_normal_01

  x = np.zeros ( n )

  for i in range ( 0, n ):
    xi, seed = r8_normal_01 ( seed )
    x[i] = mu + sigma * xi

  return x, seed

def r8vec_normal_ab_test ( ):

#*****************************************************************************80
#
## R8VEC_NORMAL_AB_TEST tests R8VEC_NORMAL_AB.
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
  from r8vec_print import r8vec_print
  import numpy as np

  print ''
  print 'R8VEC_NORMAL_AB_TEST'
  print '  R8VEC_NORMAL_AB returns a vector of Normal AB values'

  n = 10
  mu = 15.0
  sigma = 0.25
  seed = 123456789

  print ''
  print '  Mean = %g' % ( mu )
  print '  Standard deviation = %g' % ( sigma )
  print '  SEED = %d' % ( seed )

  r, seed = r8vec_normal_ab ( n, mu, sigma, seed )

  r8vec_print ( n, r, '  Vector:' )

  print ''
  print 'R8VEC_NORMAL_AB_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8vec_normal_ab_test ( )
  timestamp ( )

