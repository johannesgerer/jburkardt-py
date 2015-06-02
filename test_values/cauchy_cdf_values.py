#!/usr/bin/env python
#
def cauchy_cdf_values ( n_data ):

#*****************************************************************************80
#
## CAUCHY_CDF_VALUES returns some values of the Cauchy CDF.
#
#  Discussion:
#
#    In Mathematica, the function can be evaluated by:
#
#      Needs["Statistics`ContinuousDistributions`"]
#      dist = CauchyDistribution [ mu, sigma ]
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    18 January 2015
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
#    Output, real SIGMA, the standard deviation of the distribution.
#
#    Output, real X, the argument of the function.
#
#    Output, real F, the value of the function.
#
  import numpy as np

  n_max = 12

  f_vec = np.array ( ( \
     0.5000000000000000E+00, \
     0.8524163823495667E+00, \
     0.9220208696226307E+00, \
     0.9474315432887466E+00, \
     0.6475836176504333E+00, \
     0.6024163823495667E+00, \
     0.5779791303773693E+00, \
     0.5628329581890012E+00, \
     0.6475836176504333E+00, \
     0.5000000000000000E+00, \
     0.3524163823495667E+00, \
     0.2500000000000000E+00 ) )

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
     0.5000000000000000E+01  ) )

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

def cauchy_cdf_values_test ( ):

#*****************************************************************************80
#
## CAUCHY_CDF_VALUES_TEST tests CAUCHY_CDF_VALUES.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    18 January 2015
#
#  Author:
#
#    John Burkardt
#
  print ''
  print 'CAUCHY_CDF_VALUES_TEST:'
  print '  CAUCHY_CDF_VALUES stores values of the Cauchy CDF.'
  print ''
  print '      MU      SIGMA       X        CAUCHY_CDF(MU,SIGMA,X)'
  print ''

  n_data = 0

  while ( True ):

    n_data, mu, sigma, x, f = cauchy_cdf_values ( n_data )

    if ( n_data == 0 ):
      break

    print '  %12f  %12f  %12f  %24.16g' % ( mu, sigma, x, f )

  print ''
  print 'CAUCHY_CDF_VALUES_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  cauchy_cdf_values_test ( )
  timestamp ( )

