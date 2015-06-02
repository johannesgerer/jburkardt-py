#!/usr/bin/env python
#
def ci_values ( n_data ):

#*****************************************************************************80
#
## CI_VALUES returns some values of the cosine integral function.
#
#  Discussion:
#
#    The cosine integral is defined by
#
#      CI(X) = - integral ( X <= T < Infinity ) ( cos ( T ) ) / T  dT
#
#    In Mathematica, the function can be evaluated by:
#
#      CosIntegral[x]
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    29 January 2015
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

  n_max = 16

  fx_vec = np.array ( ( \
     -0.1777840788066129E+00, \
     -0.2227070695927976E-01, \
      0.1005147070088978E+00, \
      0.1982786159524672E+00, \
      0.2760678304677729E+00, \
      0.3374039229009681E+00, \
      0.4204591828942405E+00, \
      0.4620065850946773E+00, \
      0.4717325169318778E+00, \
      0.4568111294183369E+00, \
      0.4229808287748650E+00, \
      0.2858711963653835E+00, \
      0.1196297860080003E+00, \
     -0.3212854851248112E-01, \
     -0.1409816978869304E+00, \
     -0.1934911221017388E+00 ) )

  x_vec = np.array ( ( \
      0.5E+00, \
      0.6E+00, \
      0.7E+00, \
      0.8E+00, \
      0.9E+00, \
      1.0E+00, \
      1.2E+00, \
      1.4E+00, \
      1.6E+00, \
      1.8E+00, \
      2.0E+00, \
      2.5E+00, \
      3.0E+00, \
      3.5E+00, \
      4.0E+00, \
      4.5E+00 ) )

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

def ci_values_test ( ):

#*****************************************************************************80
#
## CI_VALUES_TEST demonstrates the use of CI_VALUES.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    29 January 2015
#
#  Author:
#
#    John Burkardt
#
  print ''
  print 'CI_VALUES_TEST:'
  print '  CI_VALUES stores values of the cosine integral function.'
  print ''
  print '      X         CI(X)'
  print ''

  n_data = 0

  while ( True ):

    n_data, x, fx = ci_values ( n_data )

    if ( n_data == 0 ):
      break

    print '  %12f  %24.16f' % ( x, fx )

  print ''
  print 'CI_VALUES_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  ci_values_test ( )
  timestamp ( )

