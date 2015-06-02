#! /usr/bin/env python
#
def triangle_monomial_integral ( i, j, t ):

#*****************************************************************************80
#
## TRIANGLE_MONOMIAL_INTEGRAL integrates a monomial over an arbitrary triangle.
#
#  Location:
#
#    http://people.sc.fsu.edu/~jburkardt/py_src/triangle_integrals/triangle_monomial_integral.py
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
#    Input, integer I, J, the exponents of X and Y in the monomial.
#    0 <= I, J.
#
#    Input, real T(2,3), the vertices of the triangle.
#
#    Output, real Q, the integral of X^I * Y^J over triangle T.
#
  import numpy as np
  from poly_power_linear import poly_power_linear
  from poly_product import poly_product
  from rs_to_xy_map import rs_to_xy_map
  from triangle_area import triangle_area
  from triangle01_poly_integral import triangle01_poly_integral
#
#  Get map coefficients from reference RS triangle to general XY triangle.
#    R = a+b*X+c*Y
#    S = d+e*X+f*Y
#
  a, b, c, d, e, f = rs_to_xy_map ( t )
#
#  Compute
#    P1(R,S) = (a+b*R+c*S)^i.
#    P2(R,S) = (d+e*R+f*S)^j.
#
  d1 = 1
  p1 = np.array ( [ a, b, c ] )
  dp1, pp1 = poly_power_linear ( d1, p1, i )

  d2 = 1
  p2 = np.array ( [ d, e, f ] )
  dp2, pp2 = poly_power_linear ( d2, p2, j )
#
#  Compute the product 
#    P3(R,S) = (a+b*R+c*S)^i * (d+e*R+f*S)^j.
#
  d3, p3 = poly_product ( dp1, pp1, dp2, pp2 )
#
#  Compute the integral of P3(R,S) over the reference triangle.
#
  q = triangle01_poly_integral ( d3, p3 )
#
#  Multiply by the area of the physical triangle T(X,Y) divided by
#  the area of the reference triangle.
#
  q = q * triangle_area ( t ) / 0.5

  return q
  
def triangle_monomial_integral_test ( ):

#*****************************************************************************80
#
## TRIANGLE_MONOMIAL_INTEGRAL_TEST estimates integrals over a triangle.
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

  print ''
  print 'TRIANGLE_MONOMIAL_INTEGRAL_TEST'
  print '  TRIANGLE_MONOMIAL_INTEGRAL returns the integral Q of'
  print '  a monomial X^I Y^J over the interior of a triangle.'
#
#  Test 1:
#
  t = np.array ( [ \
     [ 0.0, 0.0 ], \
     [ 1.0, 0.0 ], \
     [ 0.0, 1.0 ] ] )

  i = 1
  j = 0

  print ''
  print '  Triangle vertices:'
  print '    (X1,Y1) = (%g,%g)' % ( t[0,0], t[0,1] )
  print '    (X2,Y2) = (%g,%g)' % ( t[1,0], t[1,1] )
  print '    (X3,Y3) = (%g,%g)' % ( t[2,0], t[2,1] )
  print '  Integrand = x^%d * y^%d\n' % ( i, j )

  q = triangle_monomial_integral ( i, j, t )
  q2 = 1.0 / 6.0

  print '  Computed Q = %g' % ( q )
  print '  Exact Q    = %g' % ( q2 )
#
#  Test 2:
#
  t = np.array ( [ \
     [ 0.0, 0.0 ], \
     [ 1.0, 0.0 ], \
     [ 1.0, 2.0 ] ] )

  i = 1
  j = 1

  print ''
  print '  Triangle vertices:'
  print '    (X1,Y1) = (%g,%g)' % ( t[0,0], t[0,1] )
  print '    (X2,Y2) = (%g,%g)' % ( t[1,0], t[1,1] )
  print '    (X3,Y3) = (%g,%g)' % ( t[2,0], t[2,1] )
  print '  Integrand = x^%d * y^%d\n' % ( i, j )


  q = triangle_monomial_integral ( i, j, t )
  q2 = 0.5

  print '  Computed Q = %g' % ( q )
  print '  Exact Q    = %g' % ( q2 )
#
#  Test 3:
#
  t = np.array ( [ \
     [ -3.0, 0.0 ], \
     [  6.0, 0.0 ], \
     [  0.0, 3.0 ] ] )

  i = 1
  j = 0

  print ''
  print '  Triangle vertices:'
  print '    (X1,Y1) = (%g,%g)' % ( t[0,0], t[0,1] )
  print '    (X2,Y2) = (%g,%g)' % ( t[1,0], t[1,1] )
  print '    (X3,Y3) = (%g,%g)' % ( t[2,0], t[2,1] )
  print '  Integrand = x^%d * y^%d\n' % ( i, j )

  q = triangle_monomial_integral ( i, j, t )
  q2 = 13.5

  print '  Computed Q = %g' % ( q )
  print '  Exact Q    = %g' % ( q2 )
#
#  Test 4:
#
  t = np.array ( [ \
     [ 0.0, 0.0 ], \
     [ 4.0, 0.0 ], \
     [ 0.0, 1.0 ] ] )

  i = 1
  j = 1

  print ''
  print '  Triangle vertices:'
  print '    (X1,Y1) = (%g,%g)' % ( t[0,0], t[0,1] )
  print '    (X2,Y2) = (%g,%g)' % ( t[1,0], t[1,1] )
  print '    (X3,Y3) = (%g,%g)' % ( t[2,0], t[2,1] )
  print '  Integrand = x^%d * y^%d\n' % ( i, j )

  q = triangle_monomial_integral ( i, j, t )
  q2 = 2.0 / 3.0

  print '  Computed Q = %g' % ( q )
  print '  Exact Q    = %g' % ( q2 )

#
#  Terminate.
#
  print ''
  print 'TRIANGLE_MONOMIAL_INTEGRAL_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  triangle_monomial_integral_test ( )
  timestamp ( )
