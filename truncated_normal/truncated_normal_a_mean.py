#!/usr/bin/env python
#
def truncated_normal_a_mean ( mu, sigma, a ):

#*****************************************************************************80
#
## TRUNCATED_NORMAL_A_MEAN returns the mean of the lower Truncated Normal distribution.
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
#    Input, real MU, SIGMA, the parameters of the parent Normal Distribution.
#
#    Input, real A, the lower truncation limit.
#
#    Output, real VALUE, the mean of the PDF.
#
  from normal_01_cdf import normal_01_cdf
  from normal_01_pdf import normal_01_pdf

  alpha = ( a - mu ) / sigma

  alpha_cdf = normal_01_cdf ( alpha )
  beta_cdf = 1.0

  alpha_pdf = normal_01_pdf ( alpha )
  beta_pdf = 0.0

  value = mu + sigma * ( alpha_pdf - beta_pdf ) / ( beta_cdf - alpha_cdf )

  return value

def truncated_normal_a_mean_test ( ):

#*****************************************************************************80
#
## TRUNCATED_NORMAL_A_MEAN_TEST tests TRUNCATED_NORMAL_A_MEAN.
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
  from r8vec_max import r8vec_max
  from r8vec_mean import r8vec_mean
  from r8vec_min import r8vec_min

  sample_num = 1000
  seed = 123456789
  a = 50.0
  mu = 100.0
  sigma = 25.0

  print ''
  print 'TRUNCATED_NORMAL_A_MEAN_TEST'
  print '  TRUNCATED_NORMAL_A_MEAN computes the mean'
  print '  of the Truncated Normal distribution.'

  print ''
  print '  The "parent" normal distribution has'
  print '    mean =               %g' % ( mu )
  print '    standard deviation = %g' % ( sigma )
  print '  The parent distribution is truncated to'
  print '  the interval [%g,+oo)' % ( a )

  m = truncated_normal_a_mean ( mu, sigma, a )

  print ''
  print '  PDF mean = %g' % ( m )

  x = np.zeros ( sample_num )
  for i in range ( 0, sample_num ):
    x[i], seed = truncated_normal_a_sample ( mu, sigma, a, seed )

  ms = r8vec_mean ( sample_num, x )
  xmax = r8vec_max ( sample_num, x )
  xmin = r8vec_min ( sample_num, x )

  print ''
  print '  Sample size =     %6d' % ( sample_num )
  print '  Sample mean =     %14g' % ( ms )
  print '  Sample maximum =  %14g' % ( xmax )
  print '  Sample minimum =  %14g' % ( xmin )

  print ''
  print 'TRUNCATED_NORMAL_A_MEAN_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  truncated_normal_a_mean_test ( )
  timestamp ( )
