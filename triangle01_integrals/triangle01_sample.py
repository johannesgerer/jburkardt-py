#! /usr/bin/env python
#
def triangle01_sample ( n, seed ):

#*****************************************************************************80
#
## TRIANGLE01_SAMPLE samples the interior of the unit triangle in 2D.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    18 April 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Reuven Rubinstein,
#    Monte Carlo Optimization, Simulation, and Sensitivity
#    of Queueing Networks,
#    Krieger, 1992,
#    ISBN: 0894647644,
#    LC: QA298.R79.
#
#  Parameters:
#
#    Input, integer N, the number of points.
#
#    Input/output, integer SEED, a seed for the random
#    number generator.
#
#    Output, real X[2,N], the points.
#
  import numpy as np
  from r8vec_uniform_01 import r8vec_uniform_01

  x = np.zeros ( ( 2, n ) )
  m = 2

  for j in range ( 0, n ):

    e, seed = r8vec_uniform_01 ( m + 1, seed )

    for i in range ( 0, m + 1 ):
      e[i] = - np.log ( e[i] )

    e_sum = 0.0
    for i in range ( 0, m + 1 ):
      e_sum = e_sum + e[i]

    for i in range ( 0, m ):
      x[i,j] = e[i] / e_sum

  return x, seed

def triangle01_sample_test ( ):

#*****************************************************************************80
#
## TRIANGLE01_SAMPLE_TEST tests TRIANGLE01_SAMPLE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    18 April 2015
#
#  Author:
#
#    John Burkardt
#
  from r8mat_transpose_print import r8mat_transpose_print

  print ''
  print 'TRIANGLE01_SAMPLE_TEST'
  print '  TRIANGLE01_SAMPLE randomly samples the unit triangle.'

  m = 2
  n = 10
  seed = 123456789

  print ''
  print '  Number of samples to select is N = %d' % ( n )

  x, seed = triangle01_sample ( n, seed )

  r8mat_transpose_print ( m, n, x, '  Random points in unit triangle.' )
#
#  Terminate.
#
  print ''
  print 'TRIANGLE01_SAMPLE_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  triangle01_sample_test ( )
  timestamp ( )
