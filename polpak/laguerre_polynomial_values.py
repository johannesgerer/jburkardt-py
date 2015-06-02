#!/usr/bin/env python
#
def laguerre_polynomial_values ( n_data ):

#*****************************************************************************80
#
## LAGUERRE_POLYNOMIAL_VALUES returns some values of the Laguerre polynomial.
#
#  Discussion:
#
#    In Mathematica, the function can be evaluated by:
#
#      LaguerreL[n,x]
#
#  Differential equation:
#
#    X * Y'' + (1-X) * Y' + N * Y = 0
#
#  First terms:
#
#      1
#     -X   +  1
#   (  X^2 -  4 X   +   2 ) / 2
#   ( -X^3 +  9 X^2 -  18 X   +    6 ) / 6
#   (  X^4 - 16 X^3 +  72 X^2 -   96 X +      24 ) / 24
#   ( -X^5 + 25 X^4 - 200 X^3 +  600 X^2 -   600 X   +   120 ) / 120
#   (  X^6 - 36 X^5 + 450 X^4 - 2400 X^3 +  5400 X^2 -  4320 X   +   720 ) / 720
#   ( -X^7 + 49 X^6 - 882 X^5 + 7350 X^4 - 29400 X^3 + 52920 X^2 - 35280 X + 5040 ) / 5040
#
#  Recursion:
#
#    L(0)(X) = 1,
#    L(1)(X) = 1-X,
#    N * L(N)(X) = (2*N-1-X) * L(N-1)(X) - (N-1) * L(N-2)(X)
#
#  Orthogonality:
#
#    Integral ( 0 <= X < oo ) exp ( - X ) * L(N)(X) * L(M)(X) dX
#    = 0 if N /= M
#    = 1 if N == M
#
#  Special values:
#
#    L(N)(0) = 1.
#
#  Relations:
#
#    L(N)(X) = (-1)^N / N! * exp ( x ) * (d/dx)^n ( exp ( - x ) * X^n )  
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    17 February 2015
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
#    Output, integer N, the order of the polynomial.
#
#    Output, real X, the point where the polynomial is evaluated.
#
#    Output, real F, the value of the function.
#
  import numpy as np

  n_max = 17

  f_vec = np.array ( ( \
      0.1000000000000000E+01, \
      0.0000000000000000E+00, \
     -0.5000000000000000E+00, \
     -0.6666666666666667E+00, \
     -0.6250000000000000E+00, \
     -0.4666666666666667E+00, \
     -0.2569444444444444E+00, \
     -0.4047619047619048E-01, \
      0.1539930555555556E+00, \
      0.3097442680776014E+00, \
      0.4189459325396825E+00, \
      0.4801341790925124E+00, \
      0.4962122235082305E+00, \
     -0.4455729166666667E+00, \
      0.8500000000000000E+00, \
     -0.3166666666666667E+01, \
      0.3433333333333333E+02 ))

  n_vec = np.array ( ( \
     0,  1,  2, \
     3,  4,  5, \
     6,  7,  8, \
     9, 10, 11, \
    12,  5,  5, \
     5,  5 ))

  x_vec = np.array ( ( \
     1.0E+00, \
     1.0E+00, \
     1.0E+00, \
     1.0E+00, \
     1.0E+00, \
     1.0E+00, \
     1.0E+00, \
     1.0E+00, \
     1.0E+00, \
     1.0E+00, \
     1.0E+00, \
     1.0E+00, \
     1.0E+00, \
     0.5E+00, \
     3.0E+00, \
     5.0E+00, \
     1.0E+01 ))

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    n = 0
    x = 0.0
    f = 0.0
  else:
    n = n_vec[n_data]
    x = x_vec[n_data]
    f = f_vec[n_data]
    n_data = n_data + 1

  return n_data, n, x, f

def laguerre_polynomial_values_test ( ):

#*****************************************************************************80
#
## LAGUERRE_POLYNOMIAL_VALUES_TEST demonstrates LAGUERRE_POLYNOMIAL_VALUES.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    17 February 2015
#
#  Author:
#
#    John Burkardt
#
  print ''
  print 'LAGUERRE_POLYNOMIAL_VALUES_TEST:'
  print '  LAGUERRE_POLYNOMIAL_VALUES stores values of'
  print '  the Laguerre polynomials.'
  print ''
  print '     N    X            L(N)(X)'
  print ''

  n_data = 0

  while ( True ):

    [ n_data, n, x, f ] = laguerre_polynomial_values ( n_data );

    if ( n_data == 0 ):
      break

    print '  %4d  %12f  %24.16f' % (  n, x, f )

  print ''
  print 'LAGUERRE_POLYNOMIAL_VALUES_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  laguerre_polynomial_values_test ( )
  timestamp ( )
