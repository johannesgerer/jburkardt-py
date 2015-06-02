#! /usr/bin/env python
#
def triangle01_monomial_integral ( i, j ):

#*****************************************************************************80
#
## TRIANGLE01_MONOMIAL_INTEGRAL: monomial integrals in the unit triangle.
#
#  Location:
#
#    http://people.sc.fsu.edu/~jburkardt/py_src/triangle_integrals/triangle01_monomial_integral.py
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    23 April 2015
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
#    Output, real Q, the integral.
#
  k = 0
  q = 1.0

  for l in range ( 1, i + 1 ):
    k = k + 1
    q = q * float ( l ) / float ( k )

  for l in range ( 1, j + 1 ):
    k = k + 1
    q = q * float ( l ) / float ( k )

  for l in range ( 1, 3 ):
    k = k + 1
    q = q / float ( k )

  return q

def triangle01_monomial_integral_test ( ):

#*****************************************************************************80
#
## TRIANGLE01_MONOMIAL_INTEGRAL_TEST estimates integrals over the unit triangle.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    23 April 2015
#
#  Author:
#
#    John Burkardt
#
  print ''
  print 'TRIANGLE01_MONOMIAL_INTEGRAL_TEST'
  print '  TRIANGLE01_MONOMIAL_INTEGRAL returns the integral Q of'
  print '  a monomial X^I Y^J over the interior of the unit triangle.'

  print ''
  print '   I   J         Q(I,J)'

  for d in range ( 0, 6 ):
    print ''
    for i in range ( 0, d + 1 ):
      j = d - i
      q = triangle01_monomial_integral ( i, j )
      print '  %2d  %2d  %14.6g' % ( i, j, q )
#
#  Terminate.
#
  print ''
  print 'TRIANGLE01_MONOMIAL_INTEGRAL_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  triangle01_monomial_integral_test ( )
  timestamp ( )
