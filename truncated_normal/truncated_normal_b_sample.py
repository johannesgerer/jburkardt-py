#!/usr/bin/env python

def truncated_normal_b_sample ( mu, sigma, b, seed ):

#*****************************************************************************80
#
## TRUNCATED_NORMAL_B_SAMPLE samples the upper Truncated Normal distribution.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real MU, SIGMA, the mean and standard deviation of the
#    parent Normal distribution.
#
#    Input, real B, the upper truncation limit.
#
#    Input, integer SEED, a seed for the random number generator.
#
#    Output, real X, a sample of the PDF.
#
#    Output, integer SEED, a seed for the random number generator.
#
  from normal_01_cdf import normal_01_cdf
  from normal_01_cdf_inv import normal_01_cdf_inv
  from r8_uniform_01 import r8_uniform_01

  beta = ( b - mu ) / sigma

  alpha_cdf = 0.0
  beta_cdf = normal_01_cdf ( beta )

  u, seed = r8_uniform_01 ( seed )
  xi_cdf = alpha_cdf + u * ( beta_cdf - alpha_cdf )
  xi = normal_01_cdf_inv ( xi_cdf )

  x = mu + sigma * xi

  return x, seed

def truncated_normal_b_sample_test ( ):

#*****************************************************************************80
#
## TRUNCATED_NORMAL_B_SAMPLE_TEST tests TRUNCATED_NORMAL_B_SAMPLE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 March 2015
#
#  Author:
#
#    John Burkardt
#
  sample_num = 10
  seed = 123456789
  b = 150.0
  mu = 100.0
  sigma = 25.0

  print ''
  print 'TRUNCATED_NORMAL_B_SAMPLE_TEST'
  print '  TRUNCATED_NORMAL_B_SAMPLE samples'
  print '  the upper Truncated Normal distribution.'

  print ''
  print '  The "parent" normal distribution has'
  print '    mean =               %g' % ( mu )
  print '    standard deviation = %g' % ( sigma )
  print '  The parent distribution is truncated to'
  print '  the interval (-oo,%g]' % ( b )
  print ''

  print ''
  for i in range ( 0, sample_num ):
    x, seed = truncated_normal_b_sample ( mu, sigma, b, seed )
    print '  %4d  %14.6g' % ( i, x )

  print ''
  print 'TRUNCATED_NORMAL_B_SAMPLE_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  truncated_normal_b_sample_test ( )
  timestamp ( )
