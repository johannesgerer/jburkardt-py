#!/usr/bin/env python
#
def log_normal_cdf_values ( n_data ):

#*****************************************************************************80
#
## LOG_NORMAL_CDF_VALUES returns some values of the Log Normal CDF.
#
#  Discussion:
#
#    In Mathematica, the function can be evaluated by:
#
#      Needs["Statistics`ContinuousDistributions`"]
#      dist = LogNormalDistribution [ mu, sigma ]
#      CDF [ dist, x ]
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    19 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Milton Abramowitz and Irene Stegun,
#    Handbook of Mathematical Functions,
#    US Department of Commerce, 1964.
#
#    Stephen Wolfram,
#    The Mathematica Book,
#    Fourth Edition,
#    Wolfram Media / Cambridge University Press, 1999.
#
#  Parameters:
#
#    Input/output, integer N_DATA.  The user sets N_DATA to 0 before the
#    first call.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    Output, real MU, the mean of the distribution.
#
#    Output, real SIGMA, the shape parameter of the distribution.
#
#    Output, real X, the argument of the function.
#
#    Output, real F, the value of the function.
#
  import numpy as np

  n_max = 12

  f_vec = np.array ( ( \
     0.2275013194817921E-01, \
     0.2697049307349095E+00, \
     0.5781741008028732E+00, \
     0.7801170895122241E+00, \
     0.4390310097476894E+00, \
     0.4592655190218048E+00, \
     0.4694258497695908E+00, \
     0.4755320473858733E+00, \
     0.3261051056816658E+00, \
     0.1708799040927608E+00, \
     0.7343256357952060E-01, \
     0.2554673736161761E-01 ))

  mu_vec = np.array ( ( \
     0.1000000000000000E+01, \
     0.1000000000000000E+01, \
     0.1000000000000000E+01, \
     0.1000000000000000E+01, \
     0.1000000000000000E+01, \
     0.1000000000000000E+01, \
     0.1000000000000000E+01, \
     0.1000000000000000E+01, \
     0.2000000000000000E+01, \
     0.3000000000000000E+01, \
     0.4000000000000000E+01, \
     0.5000000000000000E+01 ))

  sigma_vec = np.array ( ( \
     0.5000000000000000E+00, \
     0.5000000000000000E+00, \
     0.5000000000000000E+00, \
     0.5000000000000000E+00, \
     0.2000000000000000E+01, \
     0.3000000000000000E+01, \
     0.4000000000000000E+01, \
     0.5000000000000000E+01, \
     0.2000000000000000E+01, \
     0.2000000000000000E+01, \
     0.2000000000000000E+01, \
     0.2000000000000000E+01 ))

  x_vec = np.array ( ( \
     0.1000000000000000E+01, \
     0.2000000000000000E+01, \
     0.3000000000000000E+01, \
     0.4000000000000000E+01, \
     0.2000000000000000E+01, \
     0.2000000000000000E+01, \
     0.2000000000000000E+01, \
     0.2000000000000000E+01, \
     0.3000000000000000E+01, \
     0.3000000000000000E+01, \
     0.3000000000000000E+01, \
     0.3000000000000000E+01 ))

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    mu = 0.0
    sigma = 0.0
    x = 0.0
    f = 0.0
  else:
    mu = mu_vec[n_data]
    sigma = sigma_vec[n_data]
    x = x_vec[n_data]
    f = f_vec[n_data]
    n_data = n_data + 1

  return n_data, mu, sigma, x, f

def log_normal_cdf_values_test ( ):

#*****************************************************************************80
#
## LOG_NORMAL_CDF_VALUES_TEST demonstrates the use of LOG_NORMAL_CDF_VALUES.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    19 February 2015
#
#  Author:
#
#    John Burkardt
#
  print ''
  print 'LOG_NORMAL_CDF_VALUES_TEST:'
  print '  LOG_NORMAL_CDF_VALUES stores values of the LOG_NORMAL CDF.'
  print ''
  print '      Mu        Sigma      X        F(Mu,Sigma,X)'
  print ''

  n_data = 0

  while ( True ):

    n_data, mu, sigma, x, f = log_normal_cdf_values ( n_data )

    if ( n_data == 0 ):
      break

    print '  %12f  %12f  %12f  %24.16g' % ( mu, sigma, x, f )

  print ''
  print 'LOG_NORMAL_CDF_VALUES_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  log_normal_cdf_values_test ( )
  timestamp ( )

