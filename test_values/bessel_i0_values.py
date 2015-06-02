#!/usr/bin/env python
#
def bessel_i0_values ( n_data ):

#*****************************************************************************80
#
## BESSEL_I0_VALUES returns some values of the I0 Bessel function.
#
#  Discussion:
#
#    The modified Bessel functions In(Z) and Kn(Z) are solutions of
#    the differential equation
#
#      Z^2 W'' + Z * W' - ( Z^2 + N^2 ) * W = 0.
#
#    The modified Bessel function I0(Z) corresponds to N = 0.
#
#    In Mathematica, the function can be evaluated by:
#
#      BesselI[0,x]
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 December 2014
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
     0.1000000000000000E+01, \
     0.1010025027795146E+01, \
     0.1040401782229341E+01, \
     0.1092045364317340E+01, \
     0.1166514922869803E+01, \
     0.1266065877752008E+01, \
     0.1393725584134064E+01, \
     0.1553395099731217E+01, \
     0.1749980639738909E+01, \
     0.1989559356618051E+01, \
     0.2279585302336067E+01, \
     0.3289839144050123E+01, \
     0.4880792585865024E+01, \
     0.7378203432225480E+01, \
     0.1130192195213633E+02, \
     0.1748117185560928E+02, \
     0.2723987182360445E+02, \
     0.6723440697647798E+02, \
     0.4275641157218048E+03, \
     0.2815716628466254E+04 ) )

  x_vec = np.array ( ( \
     0.00E+00, \
     0.20E+00, \
     0.40E+00, \
     0.60E+00, \
     0.80E+00, \
     0.10E+01, \
     0.12E+01, \
     0.14E+01, \
     0.16E+01, \
     0.18E+01, \
     0.20E+01, \
     0.25E+01, \
     0.30E+01, \
     0.35E+01, \
     0.40E+01, \
     0.45E+01, \
     0.50E+01, \
     0.60E+01, \
     0.80E+01, \
     0.10E+02  ) )

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

def bessel_i0_values_test ( ):

#*****************************************************************************80
#
## BESSEL_I0_VALUES_TEST demonstrates the use of BESSEL_I0_VALUES.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 December 2014
#
#  Author:
#
#    John Burkardt
#
  print ''
  print 'BESSEL_I0_VALUES_TEST:'
  print '  BESSEL_I0_VALUES stores values of the Bessel I function. of order 0.'
  print ''
  print '      X           I(0,X)'
  print ''

  n_data = 0

  while ( True ):

    n_data, x, fx = bessel_i0_values ( n_data )

    if ( n_data == 0 ):
      break

    print '  %12f  %24.16g' % ( x, fx )

  print ''
  print 'BESSEL_I0_VALUES_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  bessel_i0_values_test ( )
  timestamp ( )
