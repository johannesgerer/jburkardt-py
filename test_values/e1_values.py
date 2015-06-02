#!/usr/bin/env python
#
def e1_values ( n_data ):

#*****************************************************************************80
#
## E1_VALUES returns some values of the exponential integral function E1(X).
#
#  Discussion:
#
#    The exponential integral E1(X) is defined by the formula:
#
#      E1(X) = integral ( 1 <= T <= Infinity ) exp ( -X*T ) / T dT
#
#    In Mathematica, the function can be evaluated by:
#
#      ExpIntegralE[1,x]
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 February 2015
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

  fx_vec = np.array ( (
     0.5597735947761608E+00, \
     0.4543795031894021E+00, \
     0.3737688432335091E+00, \
     0.3105965785455430E+00, \
     0.2601839393259996E+00, \
     0.2193839343955203E+00, \
     0.1859909045360402E+00, \
     0.1584084368514626E+00, \
     0.1354509578491291E+00, \
     0.1162193125713579E+00, \
     0.1000195824066327E+00, \
     0.8630833369753979E-01, \
     0.7465464440125305E-01, \
     0.6471312936386886E-01, \
     0.5620437817453485E-01, \
     0.4890051070806112E-01 ))

  x_vec = np.array ( (
     0.5E+00, \
     0.6E+00, \
     0.7E+00, \
     0.8E+00, \
     0.9E+00, \
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
    fx = 0.0
  else:
    x = x_vec[n_data]
    fx = fx_vec[n_data]
    n_data = n_data + 1

  return n_data, x, fx

def e1_values_test ( ):

#*****************************************************************************80
#
## E1_VALUES_TEST demonstrates the use of E1_VALUES.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 February 2015
#
#  Author:
#
#    John Burkardt
#
  print ''
  print 'E1_VALUES_TEST:'
  print '  E1_VALUES stores values of the exponential integral.'
  print ''
  print '      X         E1(X)'
  print ''

  n_data = 0

  while ( True ):

    n_data, x, fx = e1_values ( n_data )

    if ( n_data == 0 ):
      break

    print '  %12f  %24.16f' % ( x, fx )

  print ''
  print 'E1_VALUES_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  e1_values_test ( )
  timestamp ( )

