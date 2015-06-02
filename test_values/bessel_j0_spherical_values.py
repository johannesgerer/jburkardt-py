#!/usr/bin/env python
#
def bessel_j0_spherical_values ( n_data ):

#*****************************************************************************80
#
## BESSEL_J0_SPHERICAL_VALUES returns some values of the Spherical Bessel function j0.
#
#  Discussion:
#
#    In Mathematica, the function can be evaluated by:
#
#      Sqrt[Pi/(2*x)] * BesselJ[1/2,x]
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 January 2015
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

  n_max = 21

  fx_vec = np.array ( ( \
      0.9983341664682815E+00, \
      0.9933466539753061E+00, \
      0.9735458557716262E+00, \
      0.9410707889917256E+00, \
      0.8966951136244035E+00, \
      0.8414709848078965E+00, \
      0.7766992383060220E+00, \
      0.7038926642774716E+00, \
      0.6247335019009407E+00, \
      0.5410264615989973E+00, \
      0.4546487134128408E+00, \
      0.3674983653725410E+00, \
      0.2814429918963129E+00, \
      0.1982697583928709E+00, \
      0.1196386250556803E+00, \
      0.4704000268662241E-01, \
     -0.1824191982111872E-01, \
     -0.7515914765495039E-01, \
     -0.1229223453596812E+00, \
     -0.1610152344586103E+00, \
     -0.1892006238269821E+00 ) )

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

def bessel_j0_spherical_values_test ( ):

#*****************************************************************************80
#
## BESSEL_J0_SPHERICAL_VALUES_TEST tests BESSEL_J0_SPHERICAL_VALUES.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 January 2015
#
#  Author:
#
#    John Burkardt
#
  print ''
  print 'BESSEL_J0_SPHERICAL_VALUES_TEST:'
  print '  BESSEL_J0_SPHERICAL_VALUES stores values of the spherical Bessel J function. of order 0.'
  print ''
  print '      X        Spherical J(0,X)'
  print ''

  n_data = 0

  while ( True ):

    n_data, x, fx = bessel_j0_spherical_values ( n_data )

    if ( n_data == 0 ):
      break

    print '  %12f  %24.16g' % ( x, fx )

  print ''
  print 'BESSEL_J0_SPHERICAL_VALUES_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  bessel_j0_spherical_values_test ( )
  timestamp ( )
