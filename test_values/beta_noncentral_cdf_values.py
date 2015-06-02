#!/usr/bin/env python
#
def beta_noncentral_cdf_values ( n_data ):

#*****************************************************************************80
#
## BETA_NONCENTRAL_CDF_VALUES returns some values of the noncentral Beta CDF.
#
#  Discussion:
#
#    The values presented here are taken from the reference, where they
#    were given to a limited number of decimal places.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    15 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    R Chattamvelli, R Shanmugam,
#    Algorithm AS 310:
#    Computing the Non-central Beta Distribution Function,
#    Applied Statistics,
#    Volume 46, Number 1, 1997, pages 146-156.
#
#  Parameters:
#
#    Input/output, integer N_DATA.  The user sets N_DATA to 0
#    before the first call.  On each call, the routine increments N_DATA by 1,
#    and returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    Output, rea A, B, the shape parameters.
#
#    Output, real LAMDA, the noncentrality parameter.
#    It is necessary to misspell LAMBDA since Python uses it as a keyword.
#
#    Output, real X, the argument of the function.
#
#    Output, real FX, the value of the function.
#
  import numpy as np

  n_max = 25

  a_vec = np.array ( ( \
        5.0, \
        5.0, \
        5.0, \
       10.0, \
       10.0, \
       10.0, \
       20.0, \
       20.0, \
       20.0, \
       10.0, \
       10.0, \
       15.0, \
       20.0, \
       20.0, \
       20.0, \
       30.0, \
       30.0, \
       10.0, \
       10.0, \
       10.0, \
       15.0, \
       10.0, \
       12.0, \
       30.0, \
       35.0  ))

  b_vec = np.array ( ( \
        5.0, \
        5.0, \
        5.0, \
       10.0, \
       10.0, \
       10.0, \
       20.0, \
       20.0, \
       20.0, \
       20.0, \
       10.0, \
        5.0, \
       10.0, \
       30.0, \
       50.0, \
       20.0, \
       40.0, \
        5.0, \
       10.0, \
       30.0, \
       20.0, \
        5.0, \
       17.0, \
       30.0, \
       30.0 ))

  f_vec = np.array ( ( \
       0.4563021, \
       0.1041337, \
       0.6022353, \
       0.9187770, \
       0.6008106, \
       0.0902850, \
       0.9998655, \
       0.9925997, \
       0.9641112, \
       0.9376626573, \
       0.7306817858, \
       0.1604256918, \
       0.1867485313, \
       0.6559386874, \
       0.9796881486, \
       0.1162386423, \
       0.9930430054, \
       0.0506899273, \
       0.1030959706, \
       0.9978417832, \
       0.2555552369, \
       0.0668307064, \
       0.0113601067, \
       0.7813366615, \
       0.8867126477 ) )

  lamda_vec = np.array ( ( \
        54.0, \
       140.0, \
       170.0, \
        54.0, \
       140.0, \
       250.0, \
        54.0, \
       140.0, \
       250.0, \
       150.0, \
       120.0, \
        80.0, \
       110.0, \
        65.0, \
       130.0, \
        80.0, \
       130.0, \
        20.0, \
        54.0, \
        80.0, \
       120.0, \
        55.0, \
        64.0, \
       140.0, \
        20.0 ))

  x_vec = np.array ( ( \
       0.8640, \
       0.9000, \
       0.9560, \
       0.8686, \
       0.9000, \
       0.9000, \
       0.8787, \
       0.9000, \
       0.9220, \
       0.868, \
       0.900, \
       0.880, \
       0.850, \
       0.660, \
       0.720, \
       0.720, \
       0.800, \
       0.644, \
       0.700, \
       0.780, \
       0.760, \
       0.795, \
       0.560, \
       0.800, \
       0.670   ) )

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    a = 0.0
    b = 0.0
    lamda = 0.0
    x = 0.0
    f = 0.0
  else:
    a = a_vec[n_data]
    b = b_vec[n_data]
    lamda = lamda_vec[n_data]
    x = x_vec[n_data]
    f = f_vec[n_data]
    n_data = n_data + 1

  return n_data, a, b, lamda, x, f

def beta_noncentral_cdf_values_test ( ):

#*****************************************************************************80
#
## BETA_NONCENTRAL_CDF_VALUES_TEST tests BETA_NONCENTRAL_CDF_VALUES.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    15 January 2015
#
#  Author:
#
#    John Burkardt
#
  print ''
  print 'BETA_NONCENTRAL_CDF_VALUES_TEST:'
  print '  BETA_NONCENTRAL_CDF_VALUES stores values of the noncentral BETA CDF.'
  print ''
  print '      A         B         LAMDA     X        BETA_NONCENTRAL_CDF(A,B,LAMDA,X)'
  print ''

  n_data = 0

  while ( True ):

    n_data, a, b, lamda, x, f = beta_noncentral_cdf_values ( n_data )

    if ( n_data == 0 ):
      break

    print '  %12f  %12f  %12f  %12f  %24.16g' % ( a, b, lamda, x, f )

  print ''
  print 'BETA_NONCENTRAL_CDF_VALUES_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  beta_noncentral_cdf_values_test ( )
  timestamp ( )

