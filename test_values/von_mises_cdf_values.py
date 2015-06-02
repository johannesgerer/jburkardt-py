#!/usr/bin/env python
#
def von_mises_cdf_values ( n_data ):

#*****************************************************************************80
#
## VON_MISES_CDF_VALUES returns some values of the von Mises CDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Kanti Mardia and Peter Jupp,
#    Directional Statistics,
#    Wiley, 2000, QA276.M335
#
#  Parameters:
#
#    Input/output, integer N_DATA.  The user sets N_DATA to 0 before the
#    first call.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    Output, real A, B, the parameters of the function.
#
#    Output, real X, the argument of the function.
#
#    Output, real F, the value of the function.
#
  import numpy as np

  n_max = 23

  a_vec = np.array ( ( \
     0.0E+00, \
     0.0E+00, \
     0.0E+00, \
     0.0E+00, \
     0.0E+00, \
     0.1E+01, \
     0.1E+01, \
     0.1E+01, \
     0.1E+01, \
     0.1E+01, \
     0.1E+01, \
    -0.2E+01, \
    -0.1E+01, \
     0.0E+01, \
     0.1E+01, \
     0.2E+01, \
     0.3E+01, \
     0.0E+00, \
     0.0E+00, \
     0.0E+00, \
     0.0E+00, \
     0.0E+00, \
     0.0E+00 ))

  b_vec = np.array ( ( \
     0.1E+01, \
     0.1E+01, \
     0.1E+01, \
     0.1E+01, \
     0.1E+01, \
     0.2E+01, \
     0.2E+01, \
     0.2E+01, \
     0.2E+01, \
     0.2E+01, \
     0.2E+01, \
     0.3E+01, \
     0.3E+01, \
     0.3E+01, \
     0.3E+01, \
     0.3E+01, \
     0.3E+01, \
     0.0E+00, \
     0.1E+01, \
     0.2E+01, \
     0.3E+01, \
     0.4E+01, \
     0.5E+01 ))

  f_vec = np.array ( ( \
    0.2535089956281180E-01, \
    0.1097539041177346E+00, \
    0.5000000000000000E+00, \
    0.8043381312498558E+00, \
    0.9417460124555197E+00, \
    0.5000000000000000E+00, \
    0.6018204118446155E+00, \
    0.6959356933122230E+00, \
    0.7765935901304593E+00, \
    0.8410725934916615E+00, \
    0.8895777369550366E+00, \
    0.9960322705517925E+00, \
    0.9404336090170247E+00, \
    0.5000000000000000E+00, \
    0.5956639098297530E-01, \
    0.3967729448207649E-02, \
    0.2321953958111930E-03, \
    0.6250000000000000E+00, \
    0.7438406999109122E+00, \
    0.8369224904294019E+00, \
    0.8941711407897124E+00, \
    0.9291058600568743E+00, \
    0.9514289900655436E+00 ))

  x_vec = np.array ( ( \
    -0.2617993977991494E+01, \
    -0.1570796326794897E+01, \
     0.0000000000000000E+00, \
     0.1047197551196598E+01, \
     0.2094395102393195E+01, \
     0.1000000000000000E+01, \
     0.1200000000000000E+01, \
     0.1400000000000000E+01, \
     0.1600000000000000E+01, \
     0.1800000000000000E+01, \
     0.2000000000000000E+01, \
     0.0000000000000000E+00, \
     0.0000000000000000E+00, \
     0.0000000000000000E+00, \
     0.0000000000000000E+00, \
     0.0000000000000000E+00, \
     0.0000000000000000E+00, \
     0.7853981633974483E+00, \
     0.7853981633974483E+00, \
     0.7853981633974483E+00, \
     0.7853981633974483E+00, \
     0.7853981633974483E+00, \
     0.7853981633974483E+00 ))

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    a = 0.0
    b = 0.0
    x = 0.0
    f = 0.0
  else:
    a = a_vec[n_data]
    b = b_vec[n_data]
    x = x_vec[n_data]
    f = f_vec[n_data]
    n_data = n_data + 1

  return n_data, a, b, x, f

def von_mises_cdf_values_test ( ):

#*****************************************************************************80
#
## VON_MISES_CDF_VALUES_TEST demonstrates the use of VON_MISES_CDF_VALUES.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 February 2015
#
#  Author:
#
#    John Burkardt
#
  print ''
  print 'VON_MISES_CDF_VALUES_TEST:'
  print '  VON_MISES_CDF_VALUES stores values of the von Mises CDF.'
  print ''
  print '      A           B           X         CDF(A,B,X)'
  print ''

  n_data = 0

  while ( True ):

    n_data, a, b, x, f = von_mises_cdf_values ( n_data )

    if ( n_data == 0 ):
      break

    print '  %12g  %12g  %12g  %24.16g' % ( a, b, x, f )

  print ''
  print 'VON_MISES_CDF_VALUES_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  von_mises_cdf_values_test ( )
  timestamp ( )

