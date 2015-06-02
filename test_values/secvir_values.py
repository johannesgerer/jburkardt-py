#!/usr/bin/env python
#
def secvir_values ( n_data ):

#*****************************************************************************80
#
## SECVIR_VALUES returns some values of the second virial coefficient.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    21 February 2015
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
#    TJ270.H3, pages 24-25.
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
#    Output, real VIR, the second virial coefficient, in
#    m^3/kg.
#
  import numpy as np

  n_max = 19

  tc_vec = np.array ( ( \
        0.0E+00, \
        5.0E+00, \
       10.0E+00, \
       20.0E+00, \
       30.0E+00, \
       40.0E+00, \
       60.0E+00, \
       90.0E+00, \
      120.0E+00, \
      150.0E+00, \
      180.0E+00, \
      210.0E+00, \
      240.0E+00, \
      300.0E+00, \
      400.0E+00, \
      500.0E+00, \
      700.0E+00, \
     1000.0E+00, \
     2000.0E+00 ))

  vir_vec = np.array ( ( \
     -98.96E+00, \
     -90.08E+00, \
     -82.29E+00, \
     -69.36E+00, \
     -59.19E+00, \
     -51.07E+00, \
     -39.13E+00, \
     -27.81E+00, \
     -20.83E+00, \
     -16.21E+00, \
     -12.98E+00, \
     -10.63E+00, \
      -8.85E+00, \
      -6.39E+00, \
      -4.03E+00, \
      -2.71E+00, \
      -1.32E+00, \
      -0.39E+00, \
       0.53E+00 ))

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    tc = 0.0
    vir = 0.0
  else:
    tc = tc_vec[n_data]
    vir = vir_vec[n_data]
    n_data = n_data + 1

  return n_data, tc, vir

def secvir_values_test ( ):

#*****************************************************************************80
#
## SECVIR_VALUES_TEST demonstrates the use of SECVIR_VALUES.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    21 February 2015
#
#  Author:
#
#    John Burkardt
#
  print ''
  print 'SECVIR_VALUES_TEST:'
  print '  SECVIR_VALUES stores values of the second virial function.'
  print ''
  print '      TC         VIR'
  print ''

  n_data = 0

  while ( True ):

    n_data, tc, vir = secvir_values ( n_data )

    if ( n_data == 0 ):
      break

    print '  %12f %24.16f' % ( tc, vir )

  print ''
  print 'SECVIR_VALUES_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  secvir_values_test ( )
  timestamp ( )

