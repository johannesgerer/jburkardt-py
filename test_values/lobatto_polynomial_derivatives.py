#!/usr/bin/env python

def lobatto_polynomial_derivatives ( n_data ):

#*****************************************************************************80
#
## LOBATTO_POLYNOMIAL_DERIVATIVES: derivatives of completed Lobatto polynomials.
#
#  Discussion:
#
#    In Mathematica, the completed Lobatto polynomial can be evaluated by:
#
#      n * LegendreP [ n - 1, x ] - n * x * LegendreP [ n, x ]
#
#    The derivative is:
#
#        n * D[LegendreP [ n - 1, x ], {x} ] 
#      - n * LegendreP [ n, x ] 
#      - n * x * D[LegendreP [ n, x ], {x}]
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    18 November 2014
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
#    Output, integer N, the order of the function.
#
#    Output, real X, the point where the function is evaluated.
#
#    Output, real FX, the value of the function.
#
  import numpy as np

  n_max = 31;

  fx_vec = np.array ( ( \
     -0.5, \
      2.437500000000000, \
      4.031250000000000, \
     -3.154296875000000, \
    -10.19165039062500, \
     -1.019622802734375, \
     15.67544555664063, \
     10.97668933868408, \
    -15.91419786214828, \
    -24.33202382177114, \
     12.00000000000000, \
      5.670000000000000, \
      0.9600000000000000, \
     -2.310000000000000, \
     -4.320000000000000, \
     -5.250000000000000, \
     -5.280000000000000, \
     -4.590000000000000, \
     -3.360000000000000, \
     -1.770000000000000, \
      0.0, \
      1.770000000000000, \
      3.360000000000000, \
      4.590000000000000, \
      5.280000000000000, \
      5.250000000000000, \
      4.320000000000000, \
      2.310000000000000, \
     -0.9600000000000000, \
     -5.670000000000000, \
    -12.00000000000000 ))

  n_vec = np.array ( ( \
     1,  2, \
     3,  4,  5, \
     6,  7,  8, \
     9, 10,  3, \
     3,  3,  3, \
     3,  3,  3, \
     3,  3,  3, \
     3,  3,  3, \
     3,  3,  3, \
     3,  3,  3, \
     3,  3 ))

  x_vec = np.array ( ( \
    0.25, \
    0.25, \
    0.25, \
    0.25, \
    0.25, \
    0.25, \
    0.25, \
    0.25, \
    0.25, \
    0.25, \
   -1.00, \
   -0.90, \
   -0.80, \
   -0.70, \
   -0.60, \
   -0.50, \
   -0.40, \
   -0.30, \
   -0.20, \
   -0.10, \
    0.00, \
    0.10, \
    0.20, \
    0.30, \
    0.40, \
    0.50, \
    0.60, \
    0.70, \
    0.80, \
    0.90, \
    1.00 ))

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

def lobatto_polynomial_derivatives_test ( ):

#*****************************************************************************80
#
## LOBATTO_POLYNOMIAL_DERIVATIVES_TEST tests LOBATTO_POLYNOMIAL_DERIVATIVES.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    18 November 2014
#
#  Author:
#
#    John Burkardt
#
  print ''
  print 'LOBATTO_POLYNOMIAL_DERIVATIVES_TEST:'
  print '  LOBATTO_POLYNOMIAL_DERIVATIVES stores derivatives of'
  print '  the completed Lobatto polynomials.'
  print ''
  print '     N    X            Lo\'(N)(X)'
  print ''

  n_data = 0

  while ( True ):

    n_data, n, x, fx = lobatto_polynomial_derivatives ( n_data )

    if ( n_data == 0 ):
      break

    print '  %4d  %12f  %24.16f' % (  n, x, fx )

  print ''
  print 'LOBATTO_POLYNOMIAL_DERIVATIVES_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  lobatto_polynomial_derivatives_test ( )
  timestamp ( )
