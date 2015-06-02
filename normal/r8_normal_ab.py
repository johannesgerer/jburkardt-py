#!/usr/bin/env python

def r8_normal_ab ( mu, sigma, seed ):

#*****************************************************************************80
#
## R8_NORMAL_AB returns a scaled pseudonormal R8.
#
#  Discussion:
#
#    The normal probability distribution function (PDF) is sampled,
#    with mean MU and standard deviation SIGMA.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real MU, the mean of the PDF.
#
#    Input, real SIGMA, the standard deviation of the PDF.
#
#    Input, integer SEED, a seed for the random number generator.
#
#    Output, real VALUE, a normally distributed
#    random value.
#
#    Output, integer SEED, an updated seed for the random
#    number generator.
#
  import numpy as np
  from r8_uniform_01 import r8_uniform_01

  r1, seed = r8_uniform_01 ( seed )
  r2, seed = r8_uniform_01 ( seed )
  value = np.sqrt ( - 2.0 * np.log ( r1 ) ) * np.cos ( 2.0 * np.pi * r2 )
  value = mu + sigma * value

  return value, seed

def r8_normal_ab_test ( ):

#*****************************************************************************80
#
## R8_NORMAL_AB_TEST tests R8_NORMAL_AB.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 March 2015
#
#  Author:
#
#    John Burkardt
#
  print ''
  print 'R8_NORMAL_AB_TEST'
  print '  R8_NORMAL_AB computes real pseudonormal values with'
  print '  mean MU and standard deviation SIGMA.'

  mu = 10.0
  sigma = 2.0
  seed = 123456789

  print ''
  print '  MU = %g' % ( mu )
  print '  SIGMA = %g' % ( sigma )
  print '  SEED = %d' % ( seed )
  print ''
  for i in range ( 0, 10 ):
    r, seed = r8_normal_ab ( mu, sigma, seed )
    print '  %2d  %14f' % ( i, r )

  print ''
  print 'R8_NORMAL_AB_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8_normal_ab_test ( )
  timestamp ( )
