#!/usr/bin/env python

def truncated_normal_b_cdf_inv ( cdf, mu, sigma, b ):

#*****************************************************************************80
#
## TRUNCATED_NORMAL_B_CDF_INV inverts the upper truncated Normal CDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real CDF, the value of the CDF.
#    0.0 <= CDF <= 1.0.
#
#    Input, real MU, SIGMA, the mean and standard deviation of the
#    parent Normal distribution.
#
#    Input, real B, the upper truncation limit.
#
#    Output, real X, the corresponding argument.
#
  from normal_01_cdf import normal_01_cdf
  from normal_01_cdf_inv import normal_01_cdf_inv
  from sys import exit

  if ( cdf < 0.0 or 1.0 < cdf ):
    print ''
    print 'TRUNCATED_NORMAL_B_CDF_INV - Fatal error!'
    print '  CDF < 0 or 1 < CDF.'
    exit ( 'TRUNCATED_NORMAL_B_CDF_INV - Fatal error!' )

  beta = ( b - mu ) / sigma

  alpha_cdf = 0.0
  beta_cdf = normal_01_cdf ( beta )

  xi_cdf = ( beta_cdf - alpha_cdf ) * cdf + alpha_cdf
  xi = normal_01_cdf_inv ( xi_cdf )

  x = mu + sigma * xi

  return x

def truncated_normal_b_cdf_inv_test ( ):

#*****************************************************************************80
#
## TRUNCATED_NORMAL_B_CDF_INV_TEST tests TRUNCATED_NORMAL_B_CDF_INV.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 March 2015
#
#  Author:
#
#    John Burkardt
#
  from truncated_normal_b_cdf import truncated_normal_b_cdf
  from truncated_normal_b_sample import truncated_normal_b_sample

  sample_num = 10
  seed = 123456789
  b = 150.0
  mu = 100.0
  sigma = 25.0

  print ''
  print 'TRUNCATED_NORMAL_B_CDF_INV_TEST'
  print '  TRUNCATED_NORMAL_B_CDF_INV inverts the CDF of'
  print '  the Truncated Normal distribution.'

  print ''
  print '  The "parent" normal distribution has'
  print '    mean =               %g' % ( mu )
  print '    standard deviation = %g' % ( sigma )
  print '  The parent distribution is truncated to'
  print '  the interval (-oo,%g]' % ( b )

  print ''
  print '             X            CDF            CDF_INV'
  print ''

  for i in range ( 0, sample_num ):
    x, seed = truncated_normal_b_sample ( mu, sigma, b, seed )
    cdf = truncated_normal_b_cdf ( x, mu, sigma, b )
    x2 = truncated_normal_b_cdf_inv ( cdf, mu, sigma, b )
    print '  %14.6g  %14.6g  %14.6g' % ( x, cdf, x2 )

  print ''
  print 'TRUNCATED_NORMAL_B_CDF_INV_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  truncated_normal_b_cdf_inv_test ( )
  timestamp ( )
