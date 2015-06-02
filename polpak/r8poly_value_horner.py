#!/usr/bin/env python
#
def r8poly_value_horner ( m, c, x ):

#*****************************************************************************80
#
## R8POLY_VALUE_HORNER evaluates a polynomial using Horner's method.
#
#  Discussion:
#
#    The polynomial 
#
#      p(x) = c0 + c1 * x + c2 * x^2 + ... + cm * x^m
#
#    is to be evaluated at the value X.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    05 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, the degree.
#
#    Input, real C(0:M), the polynomial coefficients.  
#    C(I) is the coefficient of X^I.
#
#    Input, real X, the evaluation point.
#
#    Output, real VALUE, the polynomial value.
#
  value = c[m]
  for i in range ( m - 1, -1, -1 ):
    value = value * x + c[i]

  return value

def r8poly_value_horner_test ( ):

#*****************************************************************************80
#
## R8POLY_VALUE_HORNER_TEST tests R8POLY_VALUE_HORNER.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    05 January 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  from r8poly_print import r8poly_print
  from r8vec_linspace import r8vec_linspace

  m = 4;
  n = 16;
  c = np.array ( [ 24.0, -50.0, +35.0, -10.0, 1.0 ] )

  print ''
  print 'R8POLY_VALUE_HORNER_TEST'
  print '  R8POLY_VALUE_HORNER evaluates a polynomial at a point'
  print '  using Horners method.'

  r8poly_print ( m, c, '  The polynomial coefficients:' )

  x_lo = 0.0
  x_hi = 5.0
  x = r8vec_linspace ( n, x_lo, x_hi )

  print ''
  print '   I    X    P(X)'
  print ''

  for i in range ( 0, n ):
    p = r8poly_value_horner ( m, c, x[i] )
    print '  %2d  %8.4f  %14.6g' % ( i, x[i], p )

  print ''
  print 'R8POLY_VALUE_HORNER_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8poly_value_horner_test ( )
  timestamp ( )


