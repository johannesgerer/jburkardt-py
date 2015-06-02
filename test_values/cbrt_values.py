#!/usr/bin/env python
#
def cbrt_values ( n_data ):

#*****************************************************************************80
#
## CBRT_VALUES returns some values of the cube root function.
#
#  Discussion:
#
#    CBRT(X) = real number Y such that Y * Y * Y = X.
#
#    In Mathematica, the function can be evaluated by:
#
#      Sign[x] * ( Abs[x] )^(1/3)
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    19 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Milton Abramowitz, Irene Stegun,
#    Handbook of Mathematical Functions,
#    National Bureau of Standards, 1964,
#    ISBN: 0-486-61272-4,
#    LC: QA47.A34.
#
#    Stephen Wolfram,
#    The Mathematica Book,
#    Fourth Edition,
#    Cambridge University Press, 1999,
#    ISBN: 0-521-64314-7,
#    LC: QA76.95.W65.
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
#    Output real FX, the value of the function.
#
  import numpy as np

  n_max = 14

  fx_vec = np.array ( ( \
    0.0000000000000000E+00, \
   -0.0020082988563383484484E+00, \
    0.44814047465571647087E+00, \
   -0.46415888336127788924E+00, \
    0.73680629972807732116E+00, \
   -1.0000000000000000000E+00, \
    1.2599210498948731648E+00, \
   -1.4422495703074083823E+00, \
    1.4645918875615232630E+00, \
   -2.6684016487219448673E+00, \
    3.0723168256858472933E+00, \
   -4.1408177494228532500E+00, \
    4.5947008922070398061E+00, \
   -497.93385921817447440E+00 ) )

  x_vec = np.array ( ( \
     0.0000000000000000E+00, \
    -0.8100000073710001E-08, \
     0.9000000000000000E-01, \
    -0.1000000000000000E+00, \
     0.4000000000000000E+00, \
    -0.1000000000000000E+01, \
     0.2000000000000000E+01, \
    -0.3000000000000000E+01, \
     0.3141592653589793E+01, \
    -0.1900000000000000E+02, \
     0.2900000000000000E+02, \
    -0.7100000000000000E+02, \
     0.9700000000000000E+02, \
    -0.1234567890000000E+09 ) )

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

def cbrt_values_test ( ):

#*****************************************************************************80
#
## CBRT_VALUES_TEST demonstrates the use of CBRT_VALUES.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    19 January 2015
#
#  Author:
#
#    John Burkardt
#
  print ''
  print 'CBRT_VALUES_TEST:'
  print '  CBRT_VALUES stores values of the cube root function.'
  print ''
  print '      X         CBRT(X)'
  print ''

  n_data = 0

  while ( True ):

    n_data, x, fx = cbrt_values ( n_data )

    if ( n_data == 0 ):
      break

    print '  %12f  %24.16f' % ( x, fx )

  print ''
  print 'CBRT_VALUES_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  cbrt_values_test ( )
  timestamp ( )

