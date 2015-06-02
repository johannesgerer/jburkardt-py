#!/usr/bin/env python
#
def trigamma_values ( n_data ):

#*****************************************************************************80
#
## TRIGAMMA_VALUES returns some values of the TriGamma function.
#
#  Discussion:
#
#    In Mathematica, the function can be evaluated by:
#
#      PolyGamma[1,x]
#
#    TriGamma(X) = d^2 ln ( Gamma ( X ) ) / d X^2
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
#    Output, real F, the value of the function.
#
  import numpy as np

  n_max = 11

  f_vec = np.array ( ( \
     0.1644934066848226E+01, \
     0.1433299150792759E+01, \
     0.1267377205423779E+01, \
     0.1134253434996619E+01, \
     0.1025356590529597E+01, \
     0.9348022005446793E+00, \
     0.8584318931245799E+00, \
     0.7932328301639984E+00, \
     0.7369741375017002E+00, \
     0.6879720582426356E+00, \
     0.6449340668482264E+00 ))

  x_vec = np.array ( ( \
    1.0E+00, \
    1.1E+00, \
    1.2E+00, \
    1.3E+00, \
    1.4E+00, \
    1.5E+00, \
    1.6E+00, \
    1.7E+00, \
    1.8E+00, \
    1.9E+00, \
    2.0E+00 ))

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

def trigamma_values_test ( ):

#*****************************************************************************80
#
## TRIGAMMA_VALUES_TEST demonstrates the use of TRIGAMMA_VALUES.
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
  print 'TRIGAMMA_VALUES_TEST:'
  print '  TRIGAMMA_VALUES stores values of the TRIGAMMA function.'
  print ''
  print '      X         TRIGAMMA(X)'
  print ''

  n_data = 0

  while ( True ):

    n_data, x, f = trigamma_values ( n_data )

    if ( n_data == 0 ):
      break

    print '  %12f  %24.16f' % ( x, f )

  print ''
  print 'TRIGAMMA_VALUES_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  trigamma_values_test ( )
  timestamp ( )

