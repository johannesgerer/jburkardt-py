#!/usr/bin/env python
#
def bessel_j1_values ( n_data ):

#*****************************************************************************80
#
## BESSEL_J1_VALUES returns some values of the J1 Bessel function.
#
#  Discussion:
#
#    In Mathematica, the function can be evaluated by:
#
#      BesselJ[1,x]
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
      0.3275791375914652E+00, \
      0.6604332802354914E-01, \
     -0.3390589585259365E+00, \
     -0.5767248077568734E+00, \
     -0.4400505857449335E+00, \
      0.0000000000000000E+00, \
      0.4400505857449335E+00, \
      0.5767248077568734E+00, \
      0.3390589585259365E+00, \
     -0.6604332802354914E-01, \
     -0.3275791375914652E+00, \
     -0.2766838581275656E+00, \
     -0.4682823482345833E-02, \
      0.2346363468539146E+00, \
      0.2453117865733253E+00, \
      0.4347274616886144E-01, \
     -0.1767852989567215E+00, \
     -0.2234471044906276E+00, \
     -0.7031805212177837E-01, \
      0.1333751546987933E+00, \
      0.2051040386135228E+00 ) )

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
     15.0E+00  ) )

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

def bessel_j1_values_test ( ):

#*****************************************************************************80
#
## BESSEL_J1_VALUES_TEST demonstrates the use of BESSEL_J1_VALUES.
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
  print 'BESSEL_J1_VALUES_TEST:'
  print '  BESSEL_J1_VALUES stores values of the Bessel J function. of order 1.'
  print ''
  print '      X           J(1,X)'
  print ''

  n_data = 0

  while ( True ):

    n_data, x, fx = bessel_j1_values ( n_data )

    if ( n_data == 0 ):
      break

    print '  %12f  %24.16g' % ( x, fx )

  print ''
  print 'BESSEL_J1_VALUES_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  bessel_j1_values_test ( )
  timestamp ( )
