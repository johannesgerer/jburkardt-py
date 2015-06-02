#!/usr/bin/env python
#
def bernoulli_poly_values ( n_data ):

#*****************************************************************************80
#
## BERNOULLI_POLY_VALUES returns some values of the Bernoulli polynomials.
#
#  Discussion:
#
#    In Mathematica, the function can be evaluated by:
#
#      BernoulliB[n,x]
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 December 2014
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
#    Output, integer N, the order of the Bernoulli polynomial.
#
#    Output, real X, the argument of the Bernoulli polynomial.
#
#    Output, real FX, the value of the Bernoulli polynomial.
#
  import numpy as np

  n_max = 27

  fx_vec = np.array ( ( \
     0.1000000000000000E+01, \
     -0.3000000000000000E+00, \
      0.6666666666666667E-02, \
      0.4800000000000000E-01, \
     -0.7733333333333333E-02, \
     -0.2368000000000000E-01, \
      0.6913523809523810E-02, \
      0.2490880000000000E-01, \
     -0.1014997333333333E-01, \
     -0.4527820800000000E-01, \
      0.2332631815757576E-01, \
     -0.3125000000000000E+00, \
     -0.1142400000000000E+00, \
     -0.0176800000000000E+00, \
      0.0156800000000000E+00, \
      0.0147400000000000E+00, \
      0.0000000000000000E+00, \
     -0.1524000000000000E-01, \
     -0.2368000000000000E-01, \
     -0.2282000000000000E-01, \
     -0.1376000000000000E-01, \
      0.0000000000000000E+01, \
      0.1376000000000000E-01, \
      0.2282000000000000E-01, \
      0.2368000000000000E-01, \
      0.1524000000000000E-01, \
      0.0000000000000000E+01 ) )

  n_vec = np.array ( ( \
     0, \
     1, \
     2, \
     3, \
     4, \
     5, \
     6, \
     7, \
     8, \
     9, \
    10, \
     5, \
     5, \
     5, \
     5, \
     5, \
     5, \
     5, \
     5, \
     5, \
     5, \
     5, \
     5, \
     5, \
     5, \
     5, \
     5 ))

  x_vec = np.array ( ( \
      0.2E+00, \
      0.2E+00, \
      0.2E+00, \
      0.2E+00, \
      0.2E+00, \
      0.2E+00, \
      0.2E+00, \
      0.2E+00, \
      0.2E+00, \
      0.2E+00, \
      0.2E+00, \
     -0.5E+00, \
     -0.4E+00, \
     -0.3E+00, \
     -0.2E+00, \
     -0.1E+00, \
      0.0E+00, \
      0.1E+00, \
      0.2E+00, \
      0.3E+00, \
      0.4E+00, \
      0.5E+00, \
      0.6E+00, \
      0.7E+00, \
      0.8E+00, \
      0.9E+00, \
      1.0E+00  ) )

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    n = 0
    x = 0.0
    fx = 0.0
  else:
    n = n_vec[n_data]
    x = x_vec[n_data]
    fx = fx_vec[n_data]
    n_data = n_data + 1

  return n_data, n, x, fx

def bernoulli_poly_values_test ( ):

#*****************************************************************************80
#
## BERNOULLI_POLY_VALUES_TEST demonstrates the use of BERNOULLI_POLY_VALUES.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 December 2014
#
#  Author:
#
#    John Burkardt
#
  print ''
  print 'BERNOULLI_POLY_VALUES_TEST:'
  print '  BERNOULLI_POLY_VALUES stores values of the Bernoulli polynomials.'
  print ''
  print '      N            X            FX'
  print ''

  n_data = 0

  while ( True ):

    n_data, n, x, fx = bernoulli_poly_values ( n_data )

    if ( n_data == 0 ):
      break

    print '  %6d  %12f  %24.16g' % ( n, x, fx )

  print ''
  print 'BERNOULLI_POLY_VALUES_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  bernoulli_poly_values_test ( )
  timestamp ( )

