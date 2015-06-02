#!/usr/bin/env python

def gud_values ( n_data ):

#*****************************************************************************80
#
## GUD_VALUES returns some values of the Gudermannian function.
#
#  Discussion:
#
#    The Gudermannian function relates the hyperbolic and trigonomentric
#    functions.  For any argument X, there is a corresponding value
#    GD so that
#
#      SINH(X) = TAN(GD).
#
#    This value GD is called the Gudermannian of X and symbolized
#    GD(X).  The inverse Gudermannian function is given as input a value 
#    GD and computes the corresponding value X.
#
#    GD(X) = 2 * arctan ( exp ( X ) ) - PI / 2
#
#    In Mathematica, the function can be evaluated by:
#
#      2 * Atan[Exp[x]] - Pi/2
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    15 December 2014
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
#    Daniel Zwillinger, editor,
#    CRC Standard Mathematical Tables and Formulae,
#    30th Edition,
#    CRC Press, 1996.
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

  n_max = 13

  fx_vec = np.array ( ( \
     -0.1301760336046015E+01, \
     -0.8657694832396586E+00, \
      0.0000000000000000E+00, \
      0.9983374879348662E-01, \
      0.1986798470079397E+00, \
      0.4803810791337294E+00, \
      0.8657694832396586E+00, \
      0.1131728345250509E+01, \
      0.1301760336046015E+01, \
      0.1406993568936154E+01, \
      0.1471304341117193E+01, \
      0.1510419907545700E+01, \
      0.1534169144334733E+01 ) )

  x_vec = np.array ( ( \
     -2.0E+00, \
     -1.0E+00, \
      0.0E+00, \
      0.1E+00, \
      0.2E+00, \
      0.5E+00, \
      1.0E+00, \
      1.5E+00, \
      2.0E+00, \
      2.5E+00, \
      3.0E+00, \
      3.5E+00, \
      4.0E+00 ) )

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

def gud_values_test ( ):

#*****************************************************************************80
#
## GUD_VALUE_TEST demonstrates the use of GUD_VALUES.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    15 December 2014
#
#  Author:
#
#    John Burkardt
#
  print ''
  print 'GUD_VALUES:'
  print '  GUD_VALUES stores values of the Gudermannian function.'
  print ''
  print '      X              GUD(X)'
  print ''

  n_data = 0

  while ( True ):

    n_data, x, fx = gud_values ( n_data )

    if ( n_data == 0 ):
      break

    print '  %12f  %24.16f' % ( x, fx )

  print ''
  print 'GUD_VALUES_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  gud_values_test ( )
  timestamp ( )


