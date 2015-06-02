#!/usr/bin/env python
#
def normal_cdf_values ( n_data ):

#*****************************************************************************80
#
## NORMAL_CDF_VALUES returns some values of the Normal CDF.
#
#  Discussion:
#
#    In Mathematica, the function can be evaluated by:
#
#      Needs["Statistics`ContinuousDistributions`"]
#      dist = NormalDistribution [ mu, sigma ]
#      CDF [ dist, x ]
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    20 February 2015
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
     0.9772498680518208E+00, \
     0.9999683287581669E+00, \
     0.9999999990134124E+00, \
     0.6914624612740131E+00, \
     0.6305586598182364E+00, \
     0.5987063256829237E+00, \
     0.5792597094391030E+00, \
     0.6914624612740131E+00, \
     0.5000000000000000E+00, \
     0.3085375387259869E+00, \
     0.1586552539314571E+00 ))

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

def normal_cdf_values_test ( ):

#*****************************************************************************80
#
## NORMAL_CDF_VALUES_TEST demonstrates the use of NORMAL_CDF_VALUES.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    20 February 2015
#
#  Author:
#
#    John Burkardt
#
  print ''
  print 'NORMAL_CDF_VALUES_TEST:'
  print '  NORMAL_CDF_VALUES stores values of the normal CDF.'
  print ''
  print '      MU          SIGMA       X         NORMAL_CDF(X)'
  print ''

  n_data = 0

  while ( True ):

    n_data, mu, sigma, x, f = normal_cdf_values ( n_data )

    if ( n_data == 0 ):
      break

    print '  %12f  %12f  %12f  %24.16f' % ( mu, sigma, x, f )

  print ''
  print 'NORMAL_CDF_VALUES_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  normal_cdf_values_test ( )
  timestamp ( )

