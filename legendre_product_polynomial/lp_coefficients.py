#!/usr/bin/env python

def lp_coefficients ( n ):

#*****************************************************************************80
#
## LP_COEFFICIENTS: coefficients of Legendre polynomials P(n,x).
#
#  First terms:
#
#     1
#     0     1
#    -1/2   0      3/2
#     0    -3/2    0     5/2
#     3/8   0    -30/8   0     35/8
#     0    15/8    0   -70/8    0     63/8
#    -5/16  0    105/16  0   -315/16   0    231/16
#     0   -35/16   0   315/16   0   -693/16   0    429/16
#
#     1.00000
#     0.00000  1.00000
#    -0.50000  0.00000  1.50000
#     0.00000 -1.50000  0.00000  2.5000
#     0.37500  0.00000 -3.75000  0.00000  4.37500
#     0.00000  1.87500  0.00000 -8.75000  0.00000  7.87500
#    -0.31250  0.00000  6.56250  0.00000 -19.6875  0.00000  14.4375
#     0.00000 -2.1875   0.00000  19.6875  0.00000 -43.3215  0.00000  26.8125
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    30 October 2014
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
#    Daniel Zwillinger, editor,
#    CRC Standard Mathematical Tables and Formulae,
#    30th Edition,
#    CRC Press, 1996.
#
#  Parameters:
#
#    Input, int N, the highest order polynomial to evaluate.
#    Note that polynomials 0 through N will be evaluated.
#
#    Output, int O, the number of coefficients.
#
#    Output, double C[(N+2)/2], the coefficients of the Legendre
#    polynomial of degree N.
#
#    Output, int F[(N+2)/2], the exponents.
#
  import numpy as np

  ctable = np.zeros ( ( n + 1, n + 1 ), dtype = np.float64 )

  for i in range ( 0, n + 1 ):
    for j in range ( 0, n + 1 ):
      ctable[i][j] = 0.0

  ctable[0][0] = 1.0

  if ( 0 < n ):
    ctable[1][1] = 1.0

    for i in range ( 2, n + 1 ):
      for j in range ( 0, i - 1 ):
        ctable[i][j] = ( - i + 1 ) * ctable[i-2][j] / i
      for j in range ( 1, i + 1 ):
        ctable[i][j] = ctable[i][j] + ( i + i - 1 ) * ctable[i-1][j-1] / i
#
#  Extract the nonzero data from the alternating columns of the last row.
#
  o = ( n + 2 ) // 2

  c = np.zeros ( o, dtype = np.float64 )
  f = np.zeros ( o, dtype = np.int32 )

  k = o
  for j in range ( n, -1, -2 ):
    k = k - 1
    c[k] = ctable[n][j]
    f[k] = j

  return o, c, f

def lp_coefficients_test ( ):

#*****************************************************************************80
#
## LP_COEFFICIENTS_TEST tests LP_COEFFICIENTS.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    30 October 2014
#
#  Author:
#
#    John Burkardt
#
  from polynomial_print import polynomial_print
  import numpy as np

  m = 1
  n_max = 10

  print ''
  print 'LP_COEFFICIENTS_TEST'
  print '  LP_COEFFICIENTS: coefficients of Legendre polynomial P(n,x).'
  print ''

  for n in range ( 0, n_max + 1 ):

    o, c, f = lp_coefficients ( n )

    e = np.zeros ( o, dtype = np.int32 )

    for i in range ( 0, o ):
      e[i] = f[i] + 1

    label = '  P(' + repr ( n ) + ',x) = '
    polynomial_print ( m, o, c, e, label )

  print ''
  print 'LP_COEFFICIENTS_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp

  timestamp ( )
  lp_coefficients_test ( )
  timestamp ( )
