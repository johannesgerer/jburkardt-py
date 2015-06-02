#!/usr/bin/env python
#
def ei_values ( n_data ):

#*****************************************************************************80
#
## EI_VALUES returns some values of the exponential integral function EI(X).
#
#  Definition:
#
#    The exponential integral EI(X) has the formula:
#
#      EI(X) = - integral ( -X <= T <= Infinity ) exp ( -T ) / T dT
#
#    In Mathematica, the function can be evaluated by:
#
#      ExpIntegralEi[x]
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    16 September 2004
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
     0.4542199048631736E+00, \
     0.7698812899373594E+00, \
     0.1064907194624291E+01, \
     0.1347396548212326E+01, \
     0.1622811713696867E+01, \
     0.1895117816355937E+01, \
     0.2167378279563403E+01, \
     0.2442092285192652E+01, \
     0.2721398880232024E+01, \
     0.3007207464150646E+01, \
     0.3301285449129798E+01, \
     0.3605319949019469E+01, \
     0.3920963201354904E+01, \
     0.4249867557487934E+01, \
     0.4593713686953585E+01, \
     0.4954234356001890E+01 ))

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

def ei_values_test ( ):

#*****************************************************************************80
#
## EI_VALUES_TEST demonstrates the use of EI_VALUES.
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
  print 'EI_VALUES_TEST:'
  print '  EI_VALUES stores values of the exponential integral.'
  print ''
  print '      X         EI(X)'
  print ''

  n_data = 0

  while ( True ):

    n_data, x, fx = ei_values ( n_data )

    if ( n_data == 0 ):
      break

    print '  %12f  %24.16f' % ( x, fx )

  print ''
  print 'EI_VALUES_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  ei_values_test ( )
  timestamp ( )

