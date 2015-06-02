#!/usr/bin/env python
#
def bessel_y0_int_values ( n_data ):

#*****************************************************************************80
#
## BESSEL_Y0_INT_VALUES returns some values of the Bessel Y0 integral.
#
#  Discussion:
#
#    The function is defined by:
#
#      Y0_INT(x) = Integral ( 0 <= t <= x ) Y0(t) dt
#
#    The data was reported by McLeod.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    12 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Allan McLeod,
#    Algorithm 757, MISCFUN: A software package to compute uncommon
#    special functions,
#    ACM Transactions on Mathematical Software,
#    Volume 22, Number 3, September 1996, pages 288-301.
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

  n_max = 20

  fx_vec = np.array ( ( \
     -0.91442642860172110926E-02, \
     -0.29682047390397591290E-01, \
     -0.25391431276585388961E+00, \
     -0.56179545591464028187E+00, \
     -0.63706937660742309754E+00, \
     -0.28219285008510084123E+00, \
      0.38366964785312561103E+00, \
     -0.12595061285798929390E+00, \
      0.24129031832266684828E+00, \
      0.17138069757627037938E+00, \
      0.18958142627134083732E+00, \
      0.17203846136449706946E+00, \
     -0.16821597677215029611E+00, \
     -0.93607927351428988679E-01, \
      0.88229711948036648408E-01, \
     -0.89324662736274161841E-02, \
     -0.54814071000063488284E-01, \
     -0.94958246003466381588E-01, \
     -0.19598064853404969850E-01, \
     -0.83084772357154773468E-02 ) )

  x_vec = np.array ( ( \
       0.0019531250E+00, \
       0.0078125000E+00, \
       0.1250000000E+00, \
       0.5000000000E+00, \
       1.0000000000E+00, \
       2.0000000000E+00, \
       4.0000000000E+00, \
       6.0000000000E+00, \
      10.0000000000E+00, \
      16.0000000000E+00, \
      16.2500000000E+00, \
      17.0000000000E+00, \
      20.0000000000E+00, \
      25.0000000000E+00, \
      30.0000000000E+00, \
      40.0000000000E+00, \
      50.0000000000E+00, \
      70.0000000000E+00, \
     100.0000000000E+00, \
     125.0000000000E+00 ) )

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

def bessel_y0_int_values_test ( ):

#*****************************************************************************80
#
## BESSEL_Y0_INT_VALUES_TEST demonstrates the use of BESSEL_Y0_INT_VALUES.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    12 January 2015
#
#  Author:
#
#    John Burkardt
#
  print ''
  print 'BESSEL_Y0_INT_VALUES_TEST:'
  print '  BESSEL_Y0_INT_VALUES stores values of the Bessel Y integral. of order 0.'
  print ''
  print '      X           Int_Y(0,X)'
  print ''

  n_data = 0

  while ( True ):

    n_data, x, fx = bessel_y0_int_values ( n_data )

    if ( n_data == 0 ):
      break

    print '  %12f  %24.16g' % ( x, fx )

  print ''
  print 'BESSEL_Y0_INT_VALUES_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  bessel_y0_int_values_test ( )
  timestamp ( )
