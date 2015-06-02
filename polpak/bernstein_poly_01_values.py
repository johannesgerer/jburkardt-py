#!/usr/bin/env python
#
def bernstein_poly_01_values ( n_data ):

#*****************************************************************************80
#
## BERNSTEIN_POLY_01_VALUES returns some values of the Bernstein polynomials.
#
#  Discussion:
#
#    The Bernstein polynomials are assumed to be based on [0,1].
#
#    The formula for the Bernstein polynomials is
#
#      B(N,I)(X) = [N!/(I!*(N-I)!)] * (1-X)^(N-I) * X^I
#
#    In Mathematica, the function can be evaluated by:
#
#      Binomial[n,i] * (1-x)^(n-i) * x^i
#
#  First values:
#
#    B(0,0)(X) = 1
#
#    B(1,0)(X) =      1-X
#    B(1,1)(X) =               X
#
#    B(2,0)(X) =     (1-X)^2
#    B(2,1)(X) = 2 * (1-X)   * X
#    B(2,2)(X) =               X^2
#
#    B(3,0)(X) =     (1-X)^3
#    B(3,1)(X) = 3 * (1-X)^2 * X
#    B(3,2)(X) = 3 * (1-X)   * X^2
#    B(3,3)(X) =               X^3
#
#    B(4,0)(X) =     (1-X)^4
#    B(4,1)(X) = 4 * (1-X)^3 * X
#    B(4,2)(X) = 6 * (1-X)^2 * X^2
#    B(4,3)(X) = 4 * (1-X)   * X^3
#    B(4,4)(X) =               X^4
#
#  Special values:
#
#    B(N,I)(X) has a unique maximum value at X = I/N.
#
#    B(N,I)(X) has an I-fold zero at 0 and and N-I fold zero at 1.
#
#    B(N,I)(1/2) = C(N,K) / 2^N
#
#    For a fixed X and N, the polynomials add up to 1:
#
#      Sum ( 0 <= I <= N ) B(N,I)(X) = 1
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
#    Output, integer N, the degree of the polynomial.
#
#    Output, integer K, the index of the polynomial.
#
#    Output, real X, the argument of the polynomial.
#
#    Output, real F, the value of the polynomial B(N,K)(X).
#
  import numpy as np

  n_max = 15

  f_vec = np.array ( ( \
     0.1000000000000000E+01, \
     0.7500000000000000E+00, \
     0.2500000000000000E+00, \
     0.5625000000000000E+00, \
     0.3750000000000000E+00, \
     0.6250000000000000E-01, \
     0.4218750000000000E+00, \
     0.4218750000000000E+00, \
     0.1406250000000000E+00, \
     0.1562500000000000E-01, \
     0.3164062500000000E+00, \
     0.4218750000000000E+00, \
     0.2109375000000000E+00, \
     0.4687500000000000E-01, \
     0.3906250000000000E-02 ) )

  k_vec = np.array ( ( \
    0, \
    0, 1, \
    0, 1, 2, \
    0, 1, 2, 3, \
    0, 1, 2, 3, 4 ))

  n_vec = np.array ( ( \
    0, \
    1, 1, \
    2, 2, 2, \
    3, 3, 3, 3, \
    4, 4, 4, 4, 4 ))

  x_vec = np.array ( ( \
     0.25E+00, \
     0.25E+00, \
     0.25E+00, \
     0.25E+00, \
     0.25E+00, \
     0.25E+00, \
     0.25E+00, \
     0.25E+00, \
     0.25E+00, \
     0.25E+00, \
     0.25E+00, \
     0.25E+00, \
     0.25E+00, \
     0.25E+00, \
     0.25E+00  ) )

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    n = 0
    k = 0
    x = 0.0
    f = 0.0
  else:
    n = n_vec[n_data]
    k = k_vec[n_data]
    x = x_vec[n_data]
    f = f_vec[n_data]
    n_data = n_data + 1

  return n_data, n, k, x, f

def bernstein_poly_01_values_test ( ):

#*****************************************************************************80
#
## BERNSTEIN_POLY_01_VALUES_TEST tests BERNSTEIN_POLY_01_VALUES.
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
  print 'BERNSTEIN_POLY_01_VALUES_TEST:'
  print '  BERNSTEIN_POLY_01_VALUES stores values of Bernstein polynomials.'
  print ''
  print '      N       K            X            F'
  print ''

  n_data = 0

  while ( True ):

    n_data, n, k, x, f = bernstein_poly_01_values ( n_data )

    if ( n_data == 0 ):
      break

    print '  %6d  %6d  %12f  %24.16g' % ( n, k, x, f )

  print ''
  print 'BERNSTEIN_POLY_01_VALUES_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  bernstein_poly_01_values_test ( )
  timestamp ( )
