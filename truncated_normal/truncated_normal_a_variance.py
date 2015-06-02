#!/usr/bin/env python
#
def truncated_normal_a_variance ( mu, sigma, a ):

#*****************************************************************************80
#
## TRUNCATED_NORMAL_A_VARIANCE: variance of the lower Truncated Normal distribution.
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
#    Input, real MU, SIGMA, the parameters of the PDF.
#
#    Input, real A, the lower truncation limit.
#
#    Output, real VALUE, the variance of the PDF.
#
  from normal_01_cdf import normal_01_cdf
  from normal_01_pdf import normal_01_pdf

  alpha = ( a - mu ) / sigma

  alpha_pdf = normal_01_pdf ( alpha )
  beta_pdf = 0.0

  alpha_cdf = normal_01_cdf ( alpha )
  beta_cdf = 1.0

  value = sigma * sigma * ( 1.0 \
    + ( alpha * alpha_pdf - 0.0 ) / ( beta_cdf - alpha_cdf ) \
    - ( ( alpha_pdf - beta_pdf ) / ( beta_cdf - alpha_cdf ) ) ** 2 )

  return value

def truncated_normal_a_variance_test ( ):

#*****************************************************************************80
#
## TRUNCATED_NORMAL_A_VARIANCE_TEST tests TRUNCATED_NORMAL_A_VARIANCE.
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
  import numpy as np
  from truncated_normal_a_sample import truncated_normal_a_sample
  from r8vec_variance import r8vec_variance

  sample_num = 1000
  seed = 123456789
  a = 50.0
  mu = 100.0
  sigma = 25.0

  print ''
  print 'TRUNCATED_NORMAL_A_VARIANCE_TEST'
  print '  TRUNCATED_NORMAL_A_VARIANCE computes the variance'
  print '  of the Truncated Normal distribution.'
  print ''
  print '  The "parent" normal distribution has'
  print '    mean =               %g' % ( mu )
  print '    standard deviation = %g' % ( sigma )
  print '  The parent distribution is truncated to'
  print '  the interval [%g,+oo)' % ( a )

  value = truncated_normal_a_variance ( mu, sigma, a )

  print ''
  print '  PDF variance = %g' % ( value )

  x = np.zeros ( sample_num )
  for i in range ( 0, sample_num ):
    x[i], seed = truncated_normal_a_sample ( mu, sigma, a, seed )

  value = r8vec_variance ( sample_num, x )

  print ''
  print '  Sample size = %d' % ( sample_num )
  print '  Sample variance = %g' % ( value )

  print ''
  print 'TRUNCATED_NORMAL_A_VARIANCE_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  truncated_normal_a_variance_test ( )
  timestamp ( )
