#!/usr/bin/env python
#
def log_series_cdf_values ( n_data ):

#*****************************************************************************80
#
## LOG_SERIES_CDF_VALUES returns some values of the log series CDF.
#
#  Discussion:
#
#    In Mathematica, the function can be evaluated by:
#
#      Needs["Statistics`DiscreteDistributions`]
#      dist = LogSeriesDistribution [ t ]
#      CDF [ dist, n ]
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
#    Output, real T, the parameter of the function.
#
#    Output, integer N, the argument of the function.
#
#    Output, real F, the value of the function.
#
  import numpy as np

  n_max = 29

  f_vec = np.array ( ( \
     0.9491221581029903E+00, \
     0.9433541128559735E+00, \
     0.9361094611773272E+00, \
     0.9267370278044118E+00, \
     0.9141358246245129E+00, \
     0.8962840235449100E+00, \
     0.8690148741955517E+00, \
     0.8221011541254772E+00, \
     0.7213475204444817E+00, \
     0.6068261510845583E+00, \
     0.5410106403333613E+00, \
     0.4970679476476894E+00, \
     0.4650921887927060E+00, \
     0.4404842934597863E+00, \
     0.4207860535926143E+00, \
     0.4045507673897055E+00, \
     0.3908650337129266E+00, \
     0.2149757685421097E+00, \
     0.0000000000000000E+00, \
     0.2149757685421097E+00, \
     0.3213887739704539E+00, \
     0.3916213575531612E+00, \
     0.4437690508633213E+00, \
     0.4850700239649681E+00, \
     0.5191433267738267E+00, \
     0.5480569580144867E+00, \
     0.5731033910767085E+00, \
     0.5951442521714636E+00, \
     0.6147826594068904E+00 ))

  n_vec = np.array ( ( \
     1, 1, 1, 1, 1, \
     1, 1, 1, 1, 1, \
     1, 1, 1, 1, 1, \
     1, 1, 1, 0, 1, \
     2, 3, 4, 5, 6, \
     7, 8, 9, 10 ))

  t_vec = np.array ( ( \
     0.1000000000000000E+00, \
     0.1111111111111111E+00, \
     0.1250000000000000E+00, \
     0.1428571428571429E+00, \
     0.1666666666666667E+00, \
     0.2000000000000000E+00, \
     0.2500000000000000E+00, \
     0.3333333333333333E+00, \
     0.5000000000000000E+00, \
     0.6666666666666667E+00, \
     0.7500000000000000E+00, \
     0.8000000000000000E+00, \
     0.8333333333333333E+00, \
     0.8571485714857149E+00, \
     0.8750000000000000E+00, \
     0.8888888888888889E+00, \
     0.9000000000000000E+00, \
     0.9900000000000000E+00, \
     0.9900000000000000E+00, \
     0.9900000000000000E+00, \
     0.9900000000000000E+00, \
     0.9900000000000000E+00, \
     0.9900000000000000E+00, \
     0.9900000000000000E+00, \
     0.9900000000000000E+00, \
     0.9900000000000000E+00, \
     0.9900000000000000E+00, \
     0.9900000000000000E+00, \
     0.9900000000000000E+00  ))

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    t = 0.0
    n = 0
    f = 0.0
  else:
    t = t_vec[n_data]
    n = n_vec[n_data]
    f = f_vec[n_data]
    n_data = n_data + 1

  return n_data, t, n, f

def log_series_cdf_values_test ( ):

#*****************************************************************************80
#
## LOG_SERIES_CDF_VALUES_TEST demonstrates the use of LOG_SERIES_CDF_VALUES.
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
  print 'LOG_SERIES_CDF_VALUES_TEST:'
  print '  LOG_SERIES_CDF_VALUES stores values of the LOG_SERIES_CDF function.'
  print ''
  print '      T       N         LOG_SERIES_CDF(T,N)'
  print ''

  n_data = 0

  while ( True ):

    n_data, t, n, f = log_series_cdf_values ( n_data )

    if ( n_data == 0 ):
      break

    print '  %12f  %6d  %24.16f' % ( t, n, f )

  print ''
  print 'LOG_SERIES_CDF_VALUES_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  log_series_cdf_values_test ( )
  timestamp ( )

