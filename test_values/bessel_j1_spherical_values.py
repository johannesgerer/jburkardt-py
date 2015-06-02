#!/usr/bin/env python
#
def bessel_j1_spherical_values ( n_data ):

#*****************************************************************************80
#
## BESSEL_J1_SPHERICAL_VALUES returns some values of the Spherical Bessel function j1.
#
#  Discussion:
#
#    In Mathematica, the function can be evaluated by:
#
#      Sqrt[Pi/(2*x)] * BesselJ[3/2,x]
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 January 2015
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
     0.3330001190255757E-01, \
     0.6640038067032223E-01, \
     0.1312121544218529E+00, \
     0.1928919568034122E+00, \
     0.2499855053465475E+00, \
     0.3011686789397568E+00, \
     0.3452845698577903E+00, \
     0.3813753724123076E+00, \
     0.4087081401263934E+00, \
     0.4267936423844913E+00, \
     0.4353977749799916E+00, \
     0.4345452193763121E+00, \
     0.4245152947656493E+00, \
     0.4058301968314685E+00, \
     0.3792360591872637E+00, \
     0.3456774997623560E+00, \
     0.3062665174917607E+00, \
     0.2622467779189737E+00, \
     0.2149544641595738E+00, \
     0.1657769677515280E+00, \
     0.1161107492591575E+00 ) )

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

def bessel_j1_spherical_values_test ( ):

#*****************************************************************************80
#
## BESSEL_J1_SPHERICAL_VALUES_TEST tests BESSEL_J1_SPHERICAL_VALUES.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 January 2015
#
#  Author:
#
#    John Burkardt
#
  print ''
  print 'BESSEL_J1_SPHERICAL_VALUES_TEST:'
  print '  BESSEL_J1_SPHERICAL_VALUES stores values of the spherical Bessel J function. of order 1.'
  print ''
  print '      X        Spherical J(1,X)'
  print ''

  n_data = 0

  while ( True ):

    n_data, x, fx = bessel_j1_spherical_values ( n_data )

    if ( n_data == 0 ):
      break

    print '  %12f  %24.16g' % ( x, fx )

  print ''
  print 'BESSEL_J1_SPHERICAL_VALUES_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  bessel_j1_spherical_values_test ( )
  timestamp ( )
