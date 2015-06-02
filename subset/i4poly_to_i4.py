#! /usr/bin/env python
#
def i4poly_to_i4 ( n, a, x ):

#*****************************************************************************80
#
## I4POLY_TO_I4 evaluates an integer polynomial.
#
#  Discussion:
#
#    The power sum form is:
#
#      p(x) = a(0) + a(1)*x + ... + a(n-1)*x^(n-1) + a(n)*x^(n)
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 May 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the degree of the polynomial.
#
#    Input, integer A[0:N], the polynomial coefficients.
#    A(1) is the constant term and
#    A(N+1) is the coefficient of X^N.
#
#    Input, integer X, the point at which the polynomial is to be evaluated.
#
#    Output, integer VALUE, the value of the polynomial.
#
  value = 0

  for i in range ( n, -1, -1 ):
    value = value * x + a[i]

  return value

def i4poly_to_i4_test ( ):

#*****************************************************************************80
#
## I4POLY_TO_I4_TEST tests I4POLY_TO_I4
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 May 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  from i4_to_i4poly import i4_to_i4poly

  test_num = 9

  base_test = np.array ( [ 2, 2, 2, 3, 4, 5, 6, 23, 24 ] )
  intval_test = np.array ( [ 1, 6, 23, 23, 23, 23, 23, 23, 23 ] )

  print ''
  print 'I4POLY_TO_I4_TEST'
  print '  I4POLY_TO_I4 evaluates an integer polynomial.'
  print ''
  print '       I    BASE  DEGREE  Coefficients'
  print ''

  degree_max = 10

  for test in range ( 0, test_num ):
    intval = intval_test[test]
    base = base_test[test]
    a, degree = i4_to_i4poly ( intval, base, degree_max )
    print '  %6d  %6d  %6d' % ( intval, base, degree ),
    for i in range ( degree, -1, -1 ):
      print '  %6d' % (a[i] ),
    print ''

  print ''
  print '  Now let I4_TO_I4POLY convert I to a polynomial,'
  print '  use I4POLY_TO_I4 to evaluate it, and compare.'
  print ''
  print '       I    I2'
  print ''

  for test in range ( 0, test_num ):
    intval = intval_test[test]
    base = base_test[test]
    a, degree = i4_to_i4poly ( intval, base, degree_max )
    intval2 = i4poly_to_i4 ( degree, a, base )
    print '  %6d  %6d' % ( intval, intval2 )
#
#  Terminate.
#
  print ''
  print 'I4POLY_TO_I4_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  i4poly_to_i4_test ( )
  timestamp ( )

