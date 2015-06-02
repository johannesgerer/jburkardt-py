#!/usr/bin/env python
#
def bessel_j0_values ( n_data ):

#*****************************************************************************80
#
## BESSEL_J0_VALUES returns some values of the J0 Bessel function.
#
#  Discussion:
#
#    In Mathematica, the function can be evaluated by:
#
#      BesselJ[0,x]
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    15 September 2004
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
  n_max = 21;

  fx_vec = [ \
 ];

  x_vec = [ \
 ];
  import numpy as np

  n_max = 21

  fx_vec = np.array ( ( \
     -0.1775967713143383E+00, \
     -0.3971498098638474E+00, \
     -0.2600519549019334E+00, \
      0.2238907791412357E+00, \
      0.7651976865579666E+00, \
      0.1000000000000000E+01, \
      0.7651976865579666E+00, \
      0.2238907791412357E+00, \
     -0.2600519549019334E+00, \
     -0.3971498098638474E+00, \
     -0.1775967713143383E+00, \
      0.1506452572509969E+00, \
      0.3000792705195556E+00, \
      0.1716508071375539E+00, \
     -0.9033361118287613E-01, \
     -0.2459357644513483E+00, \
     -0.1711903004071961E+00, \
      0.4768931079683354E-01, \
      0.2069261023770678E+00, \
      0.1710734761104587E+00, \
     -0.1422447282678077E-01 ) )

  x_vec = np.array ( ( \
     -5.0E+00, \
     -4.0E+00, \
     -3.0E+00, \
     -2.0E+00, \
     -1.0E+00, \
      0.0E+00, \
      1.0E+00, \
      2.0E+00, \
      3.0E+00, \
      4.0E+00, \
      5.0E+00, \
      6.0E+00, \
      7.0E+00, \
      8.0E+00, \
      9.0E+00, \
     10.0E+00, \
     11.0E+00, \
     12.0E+00, \
     13.0E+00, \
     14.0E+00, \
     15.0E+00 ) )

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

def bessel_j0_values_test ( ):

#*****************************************************************************80
#
## BESSEL_J0_VALUES_TEST demonstrates the use of BESSEL_J0_VALUES.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 December 2014
#
#  Author:
#
#    John Burkardt
#
  print ''
  print 'BESSEL_J0_VALUES_TEST:'
  print '  BESSEL_J0_VALUES stores values of the Bessel J function. of order 0.'
  print ''
  print '      X           J(0,X)'
  print ''

  n_data = 0

  while ( True ):

    n_data, x, fx = bessel_j0_values ( n_data )

    if ( n_data == 0 ):
      break

    print '  %12f  %24.16g' % ( x, fx )

  print ''
  print 'BESSEL_J0_VALUES_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  bessel_j0_values_test ( )
  timestamp ( )
