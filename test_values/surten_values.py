#!/usr/bin/env python
#
def surten_values ( n_data ):

#*****************************************************************************80
#
## SURTEN_VALUES returns some values of the surface tension.
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
#    Lester Haar, John Gallagher and George Kell,
#    NBS/NRC Steam Tables:
#    Thermodynamic and Transport Properties and Computer Programs
#    for Vapor and Liquid States of Water in SI Units,
#    Hemisphere Publishing Corporation, Washington, 1984,
#    TJ270.H3, pages 267.
#
#  Parameters:
#
#    Input/output, integer N_DATA.  The user sets N_DATA to 0 before the
#    first call.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    Output, real TC, the temperature, in degrees Celsius.
#
#    Output, real SIGMA, the surface tension,
#    in Pascal * m = Newton / m.
#
  import numpy as np

  n_max = 14

  sigma_vec = np.array ( ( \
     74.22E+00, \
     72.74E+00, \
     71.20E+00, \
     69.60E+00, \
     67.95E+00, \
     58.92E+00, \
     48.75E+00, \
     37.68E+00, \
     26.05E+00, \
     14.37E+00, \
      8.78E+00, \
      3.67E+00, \
      0.40E+00, \
      0.00E+00 ))

  tc_vec = np.array ( ( \
      10.000E+00, \
      20.000E+00, \
      30.000E+00, \
      40.000E+00, \
      50.000E+00, \
     100.000E+00, \
     150.000E+00, \
     200.000E+00, \
     250.000E+00, \
     300.000E+00, \
     325.000E+00, \
     350.000E+00, \
     370.000E+00, \
     373.976E+00 ))

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    tc = 0.0
    sigma = 0.0
  else:
    tc = tc_vec[n_data]
    sigma = sigma_vec[n_data]
    n_data = n_data + 1

  return n_data, tc, sigma

def surten_values_test ( ):

#*****************************************************************************80
#
## SURTEN_VALUES_TEST demonstrates the use of SURTEN_VALUES.
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
  print 'SURTEN_VALUES_TEST:'
  print '  SURTEN_VALUES stores values of the SURTEN function.'
  print ''
  print '      TC         SIGMA(TC)'
  print ''

  n_data = 0

  while ( True ):

    n_data, tc, sigma = surten_values ( n_data )

    if ( n_data == 0 ):
      break

    print '  %12g %24.16g' % ( tc, sigma )

  print ''
  print 'SURTEN_VALUES_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  surten_values_test ( )
  timestamp ( )

