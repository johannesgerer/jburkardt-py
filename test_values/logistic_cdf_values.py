#!/usr/bin/env python
#
def logistic_cdf_values ( n_data ):

#*****************************************************************************80
#
## LOGISTIC_CDF_VALUES returns some values of the Logistic CDF.
#
#  Discussion:
#
#    In Mathematica, the function can be evaluated by:
#
#      Needs["Statistics`ContinuousDistributions`"]
#      dist = LogisticDistribution [ mu, beta ]
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
#    Output, real BETA, the shape parameter of the distribution.
#
#    Output, real X, the argument of the function.
#
#    Output, real F, the value of the function.
#
  import numpy as np

  n_max = 12

  beta_vec = np.array ( ( \
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

  f_vec = np.array ( ( \
     0.5000000000000000E+00, \
     0.8807970779778824E+00, \
     0.9820137900379084E+00, \
     0.9975273768433652E+00, \
     0.6224593312018546E+00, \
     0.5825702064623147E+00, \
     0.5621765008857981E+00, \
     0.5498339973124779E+00, \
     0.6224593312018546E+00, \
     0.5000000000000000E+00, \
     0.3775406687981454E+00, \
     0.2689414213699951E+00 ))

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
    beta = 0.0
    x = 0.0
    f = 0.0
  else:
    mu = mu_vec[n_data]
    beta = beta_vec[n_data]
    x = x_vec[n_data]
    f = f_vec[n_data]
    n_data = n_data + 1

  return n_data, mu, beta, x, f

def logistic_cdf_values_test ( ):

#*****************************************************************************80
#
## LOGISTIC_CDF_VALUES_TEST demonstrates the use of LOGISTIC_CDF_VALUES.
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
  print 'LOGISTIC_CDF_VALUES_TEST:'
  print '  LOGISTIC_CDF_VALUES stores values of the LOGISTIC CDF.'
  print ''
  print '        Mu            Beta         X            F(Mu,Beta,X)'
  print ''

  n_data = 0

  while ( True ):

    n_data, mu, beta, x, f = logistic_cdf_values ( n_data )

    if ( n_data == 0 ):
      break

    print '  %12f  %12f  %12f  %24.16g' % ( mu, beta, x, f )

  print ''
  print 'LOGISTIC_CDF_VALUES_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  logistic_cdf_values_test ( )
  timestamp ( )

