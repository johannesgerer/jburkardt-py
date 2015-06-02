#!/usr/bin/env python
#
def bessel_k0_values ( n_data ):

#*****************************************************************************80
#
## BESSEL_K0_VALUES returns some values of the K0 Bessel function.
#
#  Discussion:
#
#    The modified Bessel functions In(Z) and Kn(Z) are solutions of
#    the differential equation
#
#      Z^2 W'' + Z * W' - ( Z^2 + N^2 ) * W = 0.
#
#    The modified Bessel function K0(Z) corresponds to N = 0.
#
#    In Mathematica, the function can be evaluated by:
#
#      BesselK[0,x]
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 December 2014
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
#    Output, real X, the argument of the function.
#
#    Output, real FX, the value of the function.
#
  import numpy as np

  n_max = 20

  fx_vec = np.array ( ( \
     0.2427069024702017E+01, \
     0.1752703855528146E+01, \
     0.1114529134524434E+01, \
     0.7775220919047293E+00, \
     0.5653471052658957E+00, \
     0.4210244382407083E+00, \
     0.3185082202865936E+00, \
     0.2436550611815419E+00, \
     0.1879547519693323E+00, \
     0.1459314004898280E+00, \
     0.1138938727495334E+00, \
     0.6234755320036619E-01, \
     0.3473950438627925E-01, \
     0.1959889717036849E-01, \
     0.1115967608585302E-01, \
     0.6399857243233975E-02, \
     0.3691098334042594E-02, \
     0.1243994328013123E-02, \
     0.1464707052228154E-03, \
     0.1778006231616765E-04 ) )

  x_vec = np.array ( ( \
      0.1E+00, \
      0.2E+00, \
      0.4E+00, \
      0.6E+00, \
      0.8E+00, \
      1.0E+00, \
      1.2E+00, \
      1.4E+00, \
      1.6E+00, \
      1.8E+00, \
      2.0E+00, \
      2.5E+00, \
      3.0E+00, \
      3.5E+00, \
      4.0E+00, \
      4.5E+00, \
      5.0E+00, \
      6.0E+00, \
      8.0E+00, \
     10.0E+00 ) )

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    x = 0.0
    fx = 0.0
  else:
    x = x_vec[n_data]
    fx = fx_vec[n_data]
    n_data = n_data + 1

  return n_data, x, fx

def bessel_k0_values_test ( ):

#*****************************************************************************80
#
## BESSEL_K0_VALUES_TEST demonstrates the use of BESSEL_K0_VALUES.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 December 2014
#
#  Author:
#
#    John Burkardt
#
  print ''
  print 'BESSEL_K0_VALUES_TEST:'
  print '  BESSEL_K0_VALUES stores values of the Bessel K function. of order 0.'
  print ''
  print '      X           K(0,X)'
  print ''

  n_data = 0

  while ( True ):

    n_data, x, fx = bessel_k0_values ( n_data )

    if ( n_data == 0 ):
      break

    print '  %12f  %24.16g' % ( x, fx )

  print ''
  print 'BESSEL_K0_VALUES_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  bessel_k0_values_test ( )
  timestamp ( )
