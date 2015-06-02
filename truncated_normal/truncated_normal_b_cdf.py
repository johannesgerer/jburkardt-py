#!/usr/bin/env python
#
def truncated_normal_b_cdf ( x, mu, sigma, b ):

#*****************************************************************************80
#
## TRUNCATED_NORMAL_B_CDF evaluates the upper Truncated Normal CDF.
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
#    Input, real X, the argument of the CDF.
#
#    Input, real MU, SIGMA, the mean and standard deviation of the
#    parent Normal distribution.
#
#    Input, real B, the upper truncation limit.
#
#    Output, real VALUE, the value of the CDF.
# 
  from normal_01_cdf import normal_01_cdf

  beta = ( b - mu ) / sigma
  xi = ( x - mu ) / sigma

  alpha_cdf = 0.0
  beta_cdf = normal_01_cdf ( beta )
  xi_cdf = normal_01_cdf ( xi )

  value = ( xi_cdf - alpha_cdf ) / ( beta_cdf - alpha_cdf )

  return value

def truncated_normal_b_cdf_test ( ):

#*****************************************************************************80
#
## TRUNCATED_NORMAL_AB_CDF_TEST tests TRUNCATED_NORMAL_AB_CDF.
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
  from truncated_normal_b_cdf_values import truncated_normal_b_cdf_values

  print ''
  print 'TRUNCATED_NORMAL_B_CDF_TEST'
  print '  TRUNCATED_NORMAL_AB_CDF evaluates the CDF'
  print '  of the upper Truncated Normal distribution.'
  print ''
  print '  The "parent" normal distribution has'
  print '    mean = mu'
  print '    standard deviation = sigma'
  print '  The parent distribution is truncated to'
  print '  the interval (-oo,b]'

  print ''
  print '                                                 Stored         Computed'
  print '       X        Mu         S         B             CDF             CDF'
  print ''

  n_data = 0

  while ( True ):

    n_data, mu, sigma, b, x, cdf1 = truncated_normal_b_cdf_values ( n_data )

    if ( n_data == 0 ):
      break

    cdf2 = truncated_normal_b_cdf ( x, mu, sigma, b )

    print '  %8.1f  %8.1f  %8.1f  %8.1f  %14g  %14g' \
      % ( x, mu, sigma, b, cdf1, cdf2 )

  print ''
  print 'TRUNCATED_NORMAL_B_CDF_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  truncated_normal_b_cdf_test ( )
  timestamp ( )


