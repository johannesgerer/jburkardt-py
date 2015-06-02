#!/usr/bin/env python
#
def bessel_y1_spherical_values ( n_data ):

#*****************************************************************************80
#
## BESSEL_Y1_SPHERICAL_VALUES returns some values of the Spherical Bessel function y1.
#
#  Discussion:
#
#    In Mathematica, the function can be evaluated by:
#
#      Sqrt[Pi/(2*x)] * BesselY[3/2,x]
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Milton Abramowitz, Irene Stegun,
#    Handbook of Mathematical Functions,
#    National Bureau of Standards, 1964,
#    LC: QA47.A34,
#    ISBN: 0-486-61272-4.
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

  n_max = 21

  fx_vec = np.array ( ( \
     -0.1004987506942709E+03, \
     -0.2549501110000635E+02, \
     -0.6730177068289658E+01, \
     -0.3233669719296388E+01, \
     -0.1985299346979349E+01, \
     -0.1381773290676036E+01, \
     -0.1028336567803712E+01, \
     -0.7906105943286149E+00, \
     -0.6133274385019998E+00, \
     -0.4709023582986618E+00, \
     -0.3506120042760553E+00, \
     -0.2459072254437506E+00, \
     -0.1534232496148467E+00, \
     -0.7151106706610352E-01, \
      0.5427959479750482E-03, \
      0.6295916360231598E-01, \
      0.1157316440198251E+00, \
      0.1587922092967723E+00, \
      0.1921166676076864E+00, \
      0.2157913917934037E+00, \
      0.2300533501309578E+00 ) )

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
     2.2E+00, \
     2.4E+00, \
     2.6E+00, \
     2.8E+00, \
     3.0E+00, \
     3.2E+00, \
     3.4E+00, \
     3.6E+00, \
     3.8E+00, \
     4.0E+00  ) )

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

def bessel_y1_spherical_values_test ( ):

#*****************************************************************************80
#
## BESSEL_Y1_SPHERICAL_VALUES_TEST tests BESSEL_Y1_SPHERICAL_VALUES.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 January 2015
#
#  Author:
#
#    John Burkardt
#
  print ''
  print 'BESSEL_Y1_SPHERICAL_VALUES_TEST:'
  print '  BESSEL_Y1_SPHERICAL_VALUES stores values of the spherical Bessel Y function of order 1.'
  print ''
  print '      X        Spherical Y(1,X)'
  print ''

  n_data = 0

  while ( True ):

    n_data, x, fx = bessel_y1_spherical_values ( n_data )

    if ( n_data == 0 ):
      break

    print '  %12f  %24.16g' % ( x, fx )

  print ''
  print 'BESSEL_Y1_SPHERICAL_VALUES_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  bessel_y1_spherical_values_test ( )
  timestamp ( )
