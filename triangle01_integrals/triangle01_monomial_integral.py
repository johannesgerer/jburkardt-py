#! /usr/bin/env python
#
def triangle01_monomial_integral ( i, j ):

#*****************************************************************************80
#
## TRIANGLE01_MONOMIAL_INTEGRAL: monomial integrals in the unit triangle in 2D.
#
#  Discussion:
#
#    The monomial is F(X,Y) = X^E(1) * Y^E(2).
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    18 April 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer I, J, the exponents.  
#    Each exponent must be nonnegative.
#
#    Output, real INTEGRAL, the integral.
#
  from sys import exit

  if ( i < 0 or j < 0 ):
    print ''
    print 'TRIANGLE01_MONOMIAL_INTEGRAL - Fatal error!'
    print '  All exponents must be nonnegative.'
    exit ( 'TRIANGLE01_MONOMIAL_INTEGRAL - Fatal error!' )

  k = 0
  integral = 1.0

  for l in range ( 1, i + 1 ):
    k = k + 1
    integral = integral * float ( l ) / float ( k )

  for l in range ( 1, j + 1 ):
    k = k + 1
    integral = integral * float ( l ) / float ( k )

  for l in range ( 0, 2 ):
    k = k + 1
    integral = integral / float ( k )

  return integral

def triangle01_monomial_integral_test01 ( ):

#*****************************************************************************80
#
## TRIANGLE01_MONOMIAL_INTEGRAL_TEST01 tests TRIANGLE01_MONOMIAL_INTEGRAL.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    18 April 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ''
  print 'TRIANGLE01_MONOMIAL_INTEGRAL_TEST01'
  print '  TRIANGLE01_MONOMIAL_INTEGRAL computes the integral of'
  print '  a monomial X^I Y^J over the unit triangle.'

  print ''
  print '   I   J    Integral(X^I Y^J)'
  for d in range ( 0, 5 ):
    print ''
    for i in range ( 0, d + 1 ):
      j = d - i
      q = triangle01_monomial_integral ( i, j )
      print '  %2d  %2d  %14.6g' % ( i, j, q )
#
#  Terminate.
#
  print ''
  print 'TRIANGLE01_MONOMIAL_INTEGRAL_TEST01:'
  print '  Normal end of execution.'

  return

def triangle01_monomial_integral_test02 ( ):

#*****************************************************************************80
#
## TRIANGLE01_MONOMIAL_INTEGRAL_TEST02 estimates integrals over the unit triangle in 2D.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    18 April 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  from monomial_value import monomial_value
  from triangle01_sample import triangle01_sample

  m = 2
  n = 4192
  test_num = 20

  print ''
  print 'TRIANGLE01_MONOMIAL_INTEGRAL_TEST02'
  print '  Estimate monomial integrals using Monte Carlo'
  print '  over the interior of the unit triangle in 2D.'
#
#  Get sample points.
#
  seed = 123456789
  x, seed = triangle01_sample ( n, seed )

  print ''
  print '  Number of sample points used is %d' % ( n )
#
#  Randomly choose X, Y exponents.
#
  print ''
  print '  We restrict this test to randomly chosen even exponents.'
  print ''
  print '  Ex  Ey     MC-Estimate      Exact           Error'
  print ''

  e = np.zeros ( 2, dtype = np.int32 )

  for i in range ( 0, 5 ):
    e[0] = i
    for j in range ( 0, 5 ):
      e[1] = j

      value = monomial_value ( m, n, e, x )

      result = 0.5 * sum ( value[:] ) / float ( n )
      exact = triangle01_monomial_integral ( i, j )
      error = abs ( result - exact )

      print '  %2d  %2d  %14.6g  %14.6g  %10.2e' \
        % ( e[0], e[1], result, exact, error )
#
#  Terminate.
#
  print ''
  print 'TRIANGLE01_MONOMIAL_INTEGRAL_TEST02:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  triangle01_monomial_integral_test01 ( )
  triangle01_monomial_integral_test02 ( )
  timestamp ( )
