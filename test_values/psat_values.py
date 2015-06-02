#!/usr/bin/env python
#
def psat_values ( n_data ):

#*****************************************************************************80
#
## PSAT_VALUES returns some values of the saturation pressure.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    20 February 2015
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
#    TJ270.H3, pages 9-15.
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
#    Output, real P, the saturation pressure, in bar.
#
  import numpy as np

  n_max = 12

  p_vec = np.array ( ( \
     0.0061173E+00, \
     0.0065716E+00, \
     0.0087260E+00, \
     0.12344E+00, \
     1.0132E+00,  \
     2.3201E+00,  \
     4.7572E+00,  \
     15.537E+00,  \
     39.737E+00,  \
     85.838E+00,  \
     165.21E+00,  \
     220.55E+00 ))

  tc_vec = np.array ( ( \
     0.100000E-01, \
     0.100000E+01, \
     0.500000E+01, \
     0.500000E+02, \
     0.100000E+03, \
     0.125000E+03, \
     0.150000E+03, \
     0.200000E+03, \
     0.250000E+03, \
     0.300000E+03, \
     0.350000E+03, \
     0.373976E+03  ))

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    tc = 0.0
    p = 0.0
  else:
    tc = tc_vec[n_data]
    p = p_vec[n_data]
    n_data = n_data + 1

  return n_data, tc, p

def psat_values_test ( ):

#*****************************************************************************80
#
## PSAT_VALUES_TEST demonstrates the use of PSAT_VALUES.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    20 February 2015
#
#  Author:
#
#    John Burkardt
#
  print ''
  print 'PSAT_VALUES_TEST:'
  print '  PSAT_VALUES stores values of the PSAT function.'
  print ''
  print '      TC         P'
  print ''

  n_data = 0

  while ( True ):

    n_data, tc, p = psat_values ( n_data )

    if ( n_data == 0 ):
      break

    print '  %12f %24.16f' % ( tc, p )

  print ''
  print 'PSAT_VALUES_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  psat_values_test ( )
  timestamp ( )

