#!/usr/bin/env python
#
def dielectric_values ( n_data ):

#*****************************************************************************80
#
## DIELECTRIC_VALUES returns some values of the static dielectric constant.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 February 2015
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
#      for Vapor and Liquid States of Water in SI Units,
#    Hemisphere Publishing Corporation, Washington, 1984,
#    TJ270.H3, page 266.
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
#    Output, real P, the pressure, in bar.
#
#    Output, real EPS, the dielectric constant, dimensionless.
#
  import numpy as np

  n_max = 15

  eps_vec = np.array ( ( \
      88.29E+00, \
      90.07E+00, \
      92.02E+00, \
      95.14E+00, \
     100.77E+00, \
      78.85E+00, \
      70.27E+00, \
      62.60E+00, \
      55.78E+00, \
      44.31E+00, \
      35.11E+00, \
      20.40E+00, \
       1.17E+00, \
       1.11E+00, \
       1.08E+00 ))

  p_vec = np.array ( ( \
      100.0E+00, \
      500.0E+00, \
     1000.0E+00, \
     2000.0E+00, \
     5000.0E+00, \
      100.0E+00, \
      100.0E+00, \
      100.0E+00, \
      100.0E+00, \
      100.0E+00, \
      100.0E+00, \
      100.0E+00, \
      100.0E+00, \
      100.0E+00, \
      100.0E+00 ))

  tc_vec = np.array ( ( \
       0.0E+00, \
       0.0E+00, \
       0.0E+00, \
       0.0E+00, \
       0.0E+00, \
      25.0E+00, \
      50.0E+00, \
      75.0E+00, \
     100.0E+00, \
     150.0E+00, \
     200.0E+00, \
     300.0E+00, \
     400.0E+00, \
     500.0E+00, \
     600.0E+00 ))

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    tc = 0.0
    p = 0.0
    eps = 0.0
  else:
    tc = tc_vec[n_data]
    p = p_vec[n_data]
    eps = eps_vec[n_data]
    n_data = n_data + 1

  return n_data, tc, p, eps

def dielectric_values_test ( ):

#*****************************************************************************80
#
## DIELECTRIC_VALUES_TEST demonstrates the use of DIELECTRIC_VALUES.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 February 2015
#
#  Author:
#
#    John Burkardt
#
  print ''
  print 'DIELECTRIC_VALUES_TEST:'
  print '  DIELECTRIC_VALUES stores values of the dielectric function.'
  print ''
  print '      T            P            EPS(T,P)'
  print ''

  n_data = 0

  while ( True ):

    n_data, tc, p, eps = dielectric_values ( n_data )

    if ( n_data == 0 ):
      break

    print '  %12f  %12f  %24.16f' % ( tc, p, eps )

  print ''
  print 'DIELECTRIC_VALUES_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  dielectric_values_test ( )
  timestamp ( )
