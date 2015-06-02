#!/usr/bin/env python
#
def bessel_k1_values ( n_data ):

#*****************************************************************************80
#
## BESSEL_K1_VALUES returns some values of the K1 Bessel function.
#
#  Discussion:
#
#    The modified Bessel functions In(Z) and Kn(Z) are solutions of
#    the differential equation
#
#      Z^2 W'' + Z * W' - ( Z^2 + N^2 ) * W = 0.
#
#    The modified Bessel function K1(Z) corresponds to N = 1.
#
#    In Mathematica, the function can be evaluated by:
#
#      BesselK[1,x]
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
     0.9853844780870606E+01, \
     0.4775972543220472E+01, \
     0.2184354424732687E+01, \
     0.1302834939763502E+01, \
     0.8617816344721803E+00, \
     0.6019072301972346E+00, \
     0.4345923910607150E+00, \
     0.3208359022298758E+00, \
     0.2406339113576119E+00, \
     0.1826230998017470E+00, \
     0.1398658818165224E+00, \
     0.7389081634774706E-01, \
     0.4015643112819418E-01, \
     0.2223939292592383E-01, \
     0.1248349888726843E-01, \
     0.7078094908968090E-02, \
     0.4044613445452164E-02, \
     0.1343919717735509E-02, \
     0.1553692118050011E-03, \
     0.1864877345382558E-04 ) )

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
     10.0E+00  ) )

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

def bessel_k1_values_test ( ):

#*****************************************************************************80
#
## BESSEL_K1_VALUES_TEST demonstrates the use of BESSEL_K1_VALUES.
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
  print 'BESSEL_K1_VALUES_TEST:'
  print '  BESSEL_K1_VALUES stores values of the Bessel K function. of order 1.'
  print ''
  print '      X           K(1,X)'
  print ''

  n_data = 0

  while ( True ):

    n_data, x, fx = bessel_k1_values ( n_data )

    if ( n_data == 0 ):
      break

    print '  %12f  %24.16g' % ( x, fx )

  print ''
  print 'BESSEL_K1_VALUES_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  bessel_k1_values_test ( )
  timestamp ( )
