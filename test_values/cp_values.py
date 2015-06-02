#!/usr/bin/env python
#
def cp_values ( n_data ):

#*****************************************************************************80
#
## CP_VALUES returns some values of the specific heat at constant pressure.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    31 January 2015
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
#    TJ270.H3, pages 229-237.
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
#    Output, real CP, the specific heat at constant pressure,
#    in KJ/(kg K).
#
  import numpy as np

  n_max = 24

  cp_vec = np.array ( ( \
     4.228E+00, \
     2.042E+00, \
     1.975E+00, \
     2.013E+00, \
     2.040E+00, \
     2.070E+00, \
     2.135E+00, \
     2.203E+00, \
     2.378E+00, \
     2.541E+00, \
     2.792E+00, \
     2.931E+00, \
     4.226E+00, \
     4.223E+00, \
     4.202E+00, \
     4.177E+00, \
     4.130E+00, \
     4.089E+00, \
     4.053E+00, \
     4.021E+00, \
     3.909E+00, \
     3.844E+00, \
     3.786E+00, \
     2.890E+00  ))

  p_vec = np.array ( ( \
        1.0E+00, \
        1.0E+00, \
        1.0E+00, \
        1.0E+00, \
        1.0E+00, \
        1.0E+00, \
        1.0E+00, \
        1.0E+00, \
        1.0E+00, \
        1.0E+00, \
        1.0E+00, \
        1.0E+00, \
        5.0E+00, \
       10.0E+00, \
       50.0E+00, \
      100.0E+00, \
      200.0E+00, \
      300.0E+00, \
      400.0E+00, \
      500.0E+00, \
     1000.0E+00, \
     1500.0E+00, \
     2000.0E+00, \
     5000.0E+00 ))

  tc_vec = np.array ( ( \
        0.0E+00, \
      100.0E+00, \
      200.0E+00, \
      300.0E+00, \
      350.0E+00, \
      400.0E+00, \
      500.0E+00, \
      600.0E+00, \
      850.0E+00, \
     1100.0E+00, \
     1600.0E+00, \
     2000.0E+00, \
        0.0E+00, \
        0.0E+00, \
        0.0E+00, \
        0.0E+00, \
        0.0E+00, \
        0.0E+00, \
        0.0E+00, \
        0.0E+00, \
        0.0E+00, \
        0.0E+00, \
        0.0E+00, \
        0.0E+00 ))

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    tc = 0.0
    p = 0.0
    cp = 0.0
  else:
    tc = tc_vec[n_data]
    p = p_vec[n_data]
    cp = cp_vec[n_data]
    n_data = n_data + 1

  return n_data, tc, p, cp

def cp_values_test ( ):

#*****************************************************************************80
#
## CP_VALUES_TEST demonstrates the use of CP_VALUES.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    31 January 2015
#
#  Author:
#
#    John Burkardt
#
  print ''
  print 'CP_VALUES_TEST:'
  print '  CP_VALUES stores values of the specific heat CP as a function of.'
  print '  temperature and pressure.'
  print ''
  print '      T            P            CP(T,P)'
  print ''

  n_data = 0

  while ( True ):

    n_data, tc, p, cp = cp_values ( n_data )

    if ( n_data == 0 ):
      break

    print '  %12f  %12f  %24.16f' % ( tc, p, cp )

  print ''
  print 'CP_VALUES_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  cp_values_test ( )
  timestamp ( )

