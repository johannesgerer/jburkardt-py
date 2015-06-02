#!/usr/bin/env python
#
def tsat_values ( n_data ):

#*****************************************************************************80
#
## TSAT_VALUES returns some values of the saturation temperature.
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
#    TJ270.H3, pages 16-22.
#
#  Parameters:
#
#    Input/output, integer N_DATA.  The user sets N_DATA to 0 before the
#    first call.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    Output, real P, the pressure, in bar.
#
#    Output, real TC, the saturation temperature, in
#    degrees Celsius.
#
  import numpy as np

  n_max = 20

  p_vec = np.array ( ( \
       0.0061173, \
       0.012, \
       0.025, \
       0.055, \
       0.080, \
       0.110, \
       0.160, \
       0.250, \
       0.500, \
       0.750, \
       1.000, \
       1.500, \
       2.000, \
       5.000, \
      10.000, \
      20.000, \
      50.000, \
     100.000, \
     200.000, \
     220.550 ))

  tc_vec = np.array ( ( \
       0.010, \
       9.655, \
      21.080, \
      34.589, \
      41.518, \
      47.695, \
      55.327, \
      64.980, \
      81.339, \
      91.783, \
      99.632, \
     111.378, \
     120.443, \
     151.866, \
     179.916, \
     212.417, \
     263.977, \
     311.031, \
     365.800, \
     373.976 ))

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    p = 0.0
    tc = 0.0
  else:
    p = p_vec[n_data]
    tc = tc_vec[n_data]
    n_data = n_data + 1

  return n_data, p, tc

def tsat_values_test ( ):

#*****************************************************************************80
#
## TSAT_VALUES_TEST demonstrates the use of TSAT_VALUES.
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
  print 'TSAT_VALUES_TEST:'
  print '  TSAT_VALUES stores values of the TSAT function.'
  print ''
  print '      P          TSAT(P)'
  print ''

  n_data = 0

  while ( True ):

    n_data, p, tc = tsat_values ( n_data )

    if ( n_data == 0 ):
      break

    print '  %12g  %24.16g' % ( p, tc )

  print ''
  print 'TSAT_VALUES_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  tsat_values_test ( )
  timestamp ( )

