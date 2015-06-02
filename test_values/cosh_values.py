#!/usr/bin/env python
#
def cosh_values ( n_data ):

#*****************************************************************************80
#
## returns some values of the hyperbolic cosine function.
#
#  Discussion:
#
#    In Mathematica, the function can be evaluated by:
#
#      Cosh[x]
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
#    Output, real FX, the value of the function.
#
  import numpy as np

  n_max = 18

  fx_vec = np.array ( ( \
      74.209948524787844444, \
       1.5430806348152437785, \
       1.0000000000000000000, \
       1.0050041680558035990, \
       1.0200667556190758463, \
       1.0453385141288604850, \
       1.0810723718384548093, \
       1.1276259652063807852, \
       1.1854652182422677038, \
       1.2551690056309430182, \
       1.3374349463048445980, \
       1.4330863854487743878, \
       1.5430806348152437785, \
       3.7621956910836314596, \
      10.067661995777765842, \
      27.308232836016486629, \
      74.209948524787844444, \
   11013.232920103323140 ))

  x_vec = np.array ( ( \
   -5.0, \
   -1.0, \
    0.0, \
    0.1, \
    0.2, \
    0.3, \
    0.4, \
    0.5, \
    0.6, \
    0.7, \
    0.8, \
    0.9, \
    1.0, \
    2.0, \
    3.0, \
    4.0, \
    5.0, \
   10.0 ))

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

def cosh_values_test ( ):

#*****************************************************************************80
#
## COSH_VALUES_TEST demonstrates the use of COSH_VALUES.
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
  print 'COSH_VALUES_TEST:'
  print '  COSH_VALUES stores values of the hyperbolic cosine function.'
  print ''
  print '      X         COSH(X)'
  print ''

  n_data = 0

  while ( True ):

    n_data, x, fx = cosh_values ( n_data )

    if ( n_data == 0 ):
      break

    print '  %12f  %24.16f' % ( x, fx )

  print ''
  print 'COSH_VALUES_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  cosh_values_test ( )
  timestamp ( )

