#!/usr/bin/env python
#
def sin_power_int_values ( n_data ):

#*****************************************************************************80
#
## SIN_POWER_INT_VALUES returns some values of the sine power integral.
#
#  Discussion:
#
#    The function has the form
#
#      SIN_POWER_INT(A,B,N) = Integral ( A <= T <= B ) ( sin(T) )^N dt
#
#    In Mathematica, the function can be evaluated by:
#
#      Integrate [ ( Sin[x] )^n, { x, a, b } ]
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
#    Output, real A, B, the limits of integration.
#
#    Output, integer N, the power.
#
#    Output, real F, the value of the function.
#
  import numpy as np

  n_max = 10

  a_vec = np.array ( ( \
      0.10E+02, \
      0.00E+00, \
      0.00E+00, \
      0.00E+00, \
      0.00E+00, \
      0.00E+00, \
      0.00E+00, \
      0.10E+01, \
      0.00E+00, \
      0.00E+00 ))

  b_vec = np.array ( ( \
      0.20E+02, \
      0.10E+01, \
      0.10E+01, \
      0.10E+01, \
      0.10E+01, \
      0.10E+01, \
      0.20E+01, \
      0.20E+01, \
      0.10E+01, \
      0.10E+01 ))

  f_vec = np.array ( ( \
     0.10000000000000000000E+02, \
     0.45969769413186028260E+00, \
     0.27267564329357957615E+00, \
     0.17894056254885809051E+00, \
     0.12402556531520681830E+00, \
     0.88974396451575946519E-01, \
     0.90393123848149944133E+00, \
     0.81495684202992349481E+00, \
     0.21887522421729849008E-01, \
     0.17023439374069324596E-01 ))

  n_vec = np.array ( ( \
     0, \
     1, \
     2, \
     3, \
     4, \
     5, \
     5, \
     5, \
    10, \
    11 ))

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    a = 0.0
    b = 0.0
    f = 0.0
    n = 0
  else:
    a = a_vec[n_data]
    b = b_vec[n_data]
    f = f_vec[n_data]
    n = n_vec[n_data]
    n_data = n_data + 1

  return n_data, a, b, n, f

def sin_power_int_values_test ( ):

#*****************************************************************************80
#
## SIN_POWER_INT_VALUES_TEST tests SIN_POWER_INT_VALUES.
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
  print 'SIN_POWER_INT_VALUES_TEST:'
  print '  SIN_POWER_INT_VALUES stores values of the cosine power integral.'
  print ''
  print '        A             B            N           F'
  print ''

  n_data = 0

  while ( True ):

    n_data, a, b, n, f = sin_power_int_values ( n_data )

    if ( n_data == 0 ):
      break

    print '  %12f  %12f  %6d  %24.16g' % ( a, b, n, f )

  print ''
  print 'SIN_POWER_INT_VALUES_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  sin_power_int_values_test ( )
  timestamp ( )
