#!/usr/bin/env python
#
def int_values ( n_data ):

#*****************************************************************************80
#
## INT_VALUES returns some values of the "integer part" function.
#
#  Discussion:
#
#    INT(X) = returns the integer part of a real number.
#
#    The result is returned as a real number.
#
#    The result is computed by rounding the absolute value of the
#    input towards 0, and then restoring the sign.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    16 February 2015
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
#    Output real F, the value of the function.
#
  import numpy as np

  n_max = 25;

  f_vec = np.array ( ( \
     -2.00E+00, \
     -1.00E+00, \
     -1.00E+00, \
     -1.00E+00, \
     -1.00E+00, \
     -1.00E+00, \
      0.00E+00, \
      0.00E+00, \
      0.00E+00, \
      0.00E+00, \
      0.00E+00, \
      0.00E+00, \
      0.00E+00, \
      0.00E+00, \
      0.00E+00, \
      0.00E+00, \
      0.00E+00, \
      0.00E+00, \
      0.00E+00, \
      1.00E+00, \
      1.00E+00, \
      1.00E+00, \
      1.00E+00, \
      1.00E+00, \
      2.00E+00 ))

  x_vec = np.array ( ( \
     -2.01E+00, \
     -1.99E+00, \
     -1.50E+00, \
     -1.10E+00, \
     -1.01E+00, \
     -1.00E+00, \
     -0.99E+00, \
     -0.90E+00, \
     -0.51E+00, \
     -0.50E+00, \
     -0.49E+00, \
     -0.01E+00, \
      0.00E+00, \
      0.01E+00, \
      0.49E+00, \
      0.50E+00, \
      0.51E+00, \
      0.90E+00, \
      0.99E+00, \
      1.00E+00, \
      1.01E+00, \
      1.10E+00, \
      1.50E+00, \
      1.99E+00, \
      2.01E+00 ))

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

def int_values_test ( ):

#*****************************************************************************80
#
## INT_VALUES_TEST demonstrates the use of INT_VALUES.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    16 February 2015
#
#  Author:
#
#    John Burkardt
#
  print ''
  print 'INT_VALUES_TEST:'
  print '  INT_VALUES stores values of the integer part function.'
  print ''
  print '      X         INT(X)'
  print ''

  n_data = 0

  while ( True ):

    n_data, x, fx = int_values ( n_data )

    if ( n_data == 0 ):
      break

    print '  %12f  %24.16f' % ( x, fx )

  print ''
  print 'INT_VALUES_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  int_values_test ( )
  timestamp ( )

