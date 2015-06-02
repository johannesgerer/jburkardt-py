#!/usr/bin/env python
#
def cardan_poly_coef ( n, s ):

#*****************************************************************************80
#
## CARDAN_POLY_COEF computes the coefficients of the N-th Cardan polynomial.
#
#  First terms:
#
#    2
#    0       1
#   -2 S     0      1
#    0      -3 S    0      1
#    2 S^2   0     -4 S    0      1
#    0       5 S^2  0     -5 S    0       1
#   -2 S^3   0      9 S^2  0     -6 S     0       1
#    0       7 S^3  0     14 S^2  0      -7 S     0       1
#    2 S^4   0    -16 S^3  0     20 S^2   0      -8 S     0        1
#    0       9 S^4  0    -30 S^3  0      27 S^2   0      -9 S      0     1
#   -2 S^5   0     25 S^4  0    -50 S^3   0      35 S^2   0      -10 S   0   1
#    0     -11 S^5  0     55 S^4  0     -77 S^3   0     +44 S^2    0   -11 S 0 1
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Thomas Osler,
#    Cardan Polynomials and the Reduction of Radicals,
#    Mathematics Magazine, 
#    Volume 74, Number 1, February 2001, pages 26-32.
#
#  Parameters:
#
#    Input, integer N, the order of the polynomial
#
#    Input, real S, the value of the parameter, which must be positive.
#
#    Output, real C(1:N+1), the coefficients.  C(1) is the constant term,
#    and C(N+1) is the coefficient of X^N.
#
  import numpy as np

  c = np.zeros ( n + 1 )

  if ( n < 0 ):
    return c
 
  c[0] = 2.0

  if ( n == 0 ):
    return c

  cm1 = np.zeros ( n + 1 )
  cm2 = np.zeros ( n )

  for i in range ( 0, n + 1 ):
    cm1[i] = c[i]

  c[0] = 0.0
  c[1] = 1.0

  for i in range ( 1, n ):

    for j in range ( 0, i ):
      cm2[j] = cm1[j]
    for j in range ( 0, i + 1 ):
      cm1[j] = c[j]

    c[0] = 0.0
    for j in range ( 1, i + 2 ):
      c[j] = cm1[j-1]
    for j in range ( 0, i ):
      c[j] = c[j] - s * cm2[j]

  return c

def cardan_poly_coef_test ( ):

#*****************************************************************************80
#
## CARDAN_POLY_COEF_TEST tests CARDAN_POLY_COEF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 February 2015
#
#  Author:
#
#    John Burkardt
#
  n_max = 10
  s = 1.0

  print ''
  print 'CARDAN_POLY_COEF_TEST'
  print '  CARDAN_POLY_COEF returns the coefficients of a Cardan polynomial.'
  print ''
  print '  We use the parameter S = %g' % ( s )
  print ''
  print '  Table of polyomial coefficients:'
  print ''

  for n in range ( 0, n_max + 1 ):

    c = cardan_poly_coef ( n, s )
    print '  %2d:  ' % ( n ),
    for i in range ( 0, n + 1 ):
      print '  %9f' % ( c[i] ),
    print ''

  print ''
  print 'CARDAN_POLY_COEF_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  cardan_poly_coef_test ( )
  timestamp ( )
