#! /usr/bin/env python
#
def triangle01_poly_integral ( d, p ):

#*****************************************************************************80
#
## TRIANGLE01_POLY_INTEGRAL: polynomial integral over the unit triangle.
#
#  Location:
#
#    http://people.sc.fsu.edu/~jburkardt/py_src/triangle_integrals/triangle01_poly_integral.py
#
#  Discussion:
#
#    The unit triangle is T = ( (0,0), (1,0), (0,1) ).
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
#    Input, integer D, the degree of the polynomial.
#
#    Input, real P(M), the polynomial coefficients.
#    M = ((D+1)*(D+2))/2.
#
#    Output, real Q, the integral.
#
  from i4_to_pascal import i4_to_pascal
  from triangle01_monomial_integral import triangle01_monomial_integral

  m = ( ( d + 1 ) * ( d + 2 ) ) / 2

  q = 0.0
  for k in range ( 1, m + 1 ):
    km1 = k - 1
    i, j = i4_to_pascal ( k )
    qk = triangle01_monomial_integral ( i, j )
    q = q + p[km1] * qk

  return q

def triangle01_poly_integral_test ( ):

#*****************************************************************************80
#
## TRIANGLE01_POLY_INTEGRAL_TEST: polynomial integrals over the unit triangle.
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
  import numpy as np
  from i4_to_pascal import i4_to_pascal
  from poly_print import poly_print
  from triangle01_monomial_integral import triangle01_monomial_integral

  d_max = 6
  k_max = ( ( d_max + 1 ) * ( d_max + 2 ) ) / 2
  qm = np.zeros ( k_max )
  for k in range ( 1, k_max + 1 ):
    km1 = k - 1
    i, j = i4_to_pascal ( k )
    qm[km1] = triangle01_monomial_integral ( i, j )

  print ''
  print 'TRIANGLE01_POLY_INTEGRAL_TEST'
  print '  TRIANGLE01_POLY_INTEGRAL returns the integral Q of'
  print '  a polynomial P(X,Y) over the interior of the unit triangle.'

  d = 1
  m = ( ( d + 1 ) * ( d + 2 ) ) / 2
  p = np.array ( [ 1.0, 2.0, 3.0 ] )
  print ''
  poly_print ( d, p, '  p(x,y)' )
  q = triangle01_poly_integral ( d, p )
  print ''
  print '  Q =         %g' % ( q )
  q2 = np.dot ( p, qm[0:m] )
  print '  Q (exact) = %g' % ( q2 )

  d = 2
  m = ( ( d + 1 ) * ( d + 2 ) ) / 2
  p = np.array ( [ 0.0, 0.0, 0.0, 0.0, 1.0, 0.0 ] )
  print ''
  poly_print ( d, p, '  p(x,y)' )
  q = triangle01_poly_integral ( d, p )
  print ''
  print '  Q =         %g' % ( q )
  q2 = np.dot ( p, qm[0:m] )
  print '  Q (exact) = %g' % ( q2 )

  d = 2
  m = ( ( d + 1 ) * ( d + 2 ) ) / 2
  p = np.array ( [ 1.0, -2.0, 3.0, -4.0, 5.0, -6.0 ] )
  print ''
  poly_print ( d, p, '  p(x,y)' )
  q = triangle01_poly_integral ( d, p )
  print ''
  print '  Q =         %g' % ( q )
  q2 = np.dot ( p, qm[0:m] )
  print '  Q (exact) = %g' % ( q2 )
#
#  Terminate.
#
  print ''
  print 'TRIANGLE01_POLY_INTEGRAL_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  triangle01_poly_integral_test ( )
  timestamp ( )
