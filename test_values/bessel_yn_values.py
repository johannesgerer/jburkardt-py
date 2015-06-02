#!/usr/bin/env python
#
def bessel_yn_values ( n_data ):

#*****************************************************************************80
#
## BESSEL_YN_VALUES returns some values of the Kn Bessel function.
#
#  Discussion:
#
#    In Mathematica, the function can be evaluated by:
#
#      BesselY[n,x]
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    14 January 2015
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
#    Output, integer NU, the order of the function.
#
#    Output, real X, the argument of the function.
#
#    Output, real FX, the value of the function.
#
  import numpy as np

  n_max = 20

  fx_vec = np.array ( ( \
     -0.1650682606816254E+01, \
     -0.6174081041906827E+00, \
      0.3676628826055245E+00, \
     -0.5868082442208615E-02, \
      0.9579316872759649E-01, \
     -0.2604058666258122E+03, \
     -0.9935989128481975E+01, \
     -0.4536948224911019E+00, \
      0.1354030476893623E+00, \
     -0.7854841391308165E-01, \
     -0.1216180142786892E+09, \
     -0.1291845422080393E+06, \
     -0.2512911009561010E+02, \
     -0.3598141521834027E+00, \
      0.5723897182053514E-02, \
     -0.4113970314835505E+23, \
     -0.4081651388998367E+17, \
     -0.5933965296914321E+09, \
     -0.1597483848269626E+04, \
      0.1644263394811578E-01 ) )

  nu_vec = np.array ( ( \
     2,  2,  2,  2, \
     2,  5,  5,  5, \
     5,  5, 10, 10, \
    10, 10, 10, 20, \
    20, 20, 20, 20 ))

  x_vec = np.array ( ( \
      1.0E+00, \
      2.0E+00, \
      5.0E+00, \
     10.0E+00, \
     50.0E+00, \
      1.0E+00, \
      2.0E+00, \
      5.0E+00, \
     10.0E+00, \
     50.0E+00, \
      1.0E+00, \
      2.0E+00, \
      5.0E+00, \
     10.0E+00, \
     50.0E+00, \
      1.0E+00, \
      2.0E+00, \
      5.0E+00, \
     10.0E+00, \
     50.0E+00 ) )

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    nu = 0
    x = 0.0
    fx = 0.0
  else:
    nu = nu_vec[n_data]
    x = x_vec[n_data]
    fx = fx_vec[n_data]
    n_data = n_data + 1

  return n_data, nu, x, fx

def bessel_yn_values_test ( ):

#*****************************************************************************80
#
## BESSEL_YN_VALUES_TEST demonstrates the use of BESSEL_YN_VALUES.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    14 January 2015
#
#  Author:
#
#    John Burkardt
#
  print ''
  print 'BESSEL_YN_VALUES_TEST:'
  print '  BESSEL_YN_VALUES stores values of the Bessel Y function. of order NU.'
  print ''
  print '      NU  X           Y(NU,X)'
  print ''

  n_data = 0

  while ( True ):

    n_data, nu, x, fx = bessel_yn_values ( n_data )

    if ( n_data == 0 ):
      break

    print '  %4d  %12f  %24.16g' % ( nu, x, fx )

  print ''
  print 'BESSEL_YN_VALUES_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  bessel_yn_values_test ( )
  timestamp ( )
