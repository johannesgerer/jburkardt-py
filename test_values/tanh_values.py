#!/usr/bin/env python
#
def tanh_values ( n_data ):

#*****************************************************************************80
#
## TANH_VALUES returns some values of the hyperbolic tangent function.
#
#  Discussion:
#
#    In Mathematica, the function can be evaluated by:
#
#      Tanh[x]
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
#    Output, real F, the value of the function.
#
  import numpy as np

  n_max = 18

  f_vec = np.array ( ( \
   -0.99990920426259513121, \
   -0.76159415595576488812, \
    0.00000000000000000000, \
    0.099667994624955817118, \
    0.19737532022490400074, \
    0.29131261245159090582, \
    0.37994896225522488527, \
    0.46211715726000975850, \
    0.53704956699803528586, \
    0.60436777711716349631, \
    0.66403677026784896368, \
    0.71629787019902442081, \
    0.76159415595576488812, \
    0.96402758007581688395, \
    0.99505475368673045133, \
    0.99932929973906704379, \
    0.99990920426259513121, \
    0.99999999587769276362 ))

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
    f = 0.0
  else:
    x = x_vec[n_data]
    f = f_vec[n_data]
    n_data = n_data + 1

  return n_data, x, f

def tanh_values_test ( ):

#*****************************************************************************80
#
## TANH_VALUES_TEST demonstrates the use of TANH_VALUES.
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
  print 'TANH_VALUES_TEST:'
  print '  TANH_VALUES stores values of the TANH function.'
  print ''
  print '      X         TANH(X)'
  print ''

  n_data = 0

  while ( True ):

    n_data, x, f = tanh_values ( n_data )

    if ( n_data == 0 ):
      break

    print '  %12g  %24.16g' % ( x, f )

  print ''
  print 'TANH_VALUES_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  tanh_values_test ( )
  timestamp ( )

