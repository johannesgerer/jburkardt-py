#! /usr/bin/env python
#
def triangle_poly_integral ( d, p, t ):

#*****************************************************************************80
#
## TRIANGLE_POLY_INTEGRAL: polynomial integral over a triangle.
#
#  Location:
#
#    http://people.sc.fsu.edu/~jburkardt/py_src/triangle_integrals/triangle_poly_integral.py
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
#    Input, real T(2,3), the vertices of the triangle.
#
#    Output, real Q, the integral.
#
  from i4_to_pascal import i4_to_pascal
  from triangle_monomial_integral import triangle_monomial_integral

  m = ( ( d + 1 ) * ( d + 2 ) ) / 2

  q = 0.0
  for k in range ( 1, m + 1 ):
    km1 = k - 1
    i, j = i4_to_pascal ( k )
    qk = triangle_monomial_integral ( i, j, t )
    q = q + p[km1] * qk

  return q

def triangle_poly_integral_test ( ):

#*****************************************************************************80
#
## TRIANGLE_POLY_INTEGRAL_TEST estimates integrals over a triangle.
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
  from poly_print import poly_print

  print ''
  print 'TRIANGLE_POLY_INTEGRAL_TEST'
  print '  TRIANGLE_POLY_INTEGRAL returns the integral Q of'
  print '  a polynomial over the interior of a triangle.'
#
#  Test 1:
#  Integrate x over reference triangle.
#
  t = np.array ( [ \
     [ 0.0, 0.0 ], \
     [ 1.0, 0.0 ], \
     [ 0.0, 1.0 ] ] )

  d = 1
  p = np.array ( [ 0.0, 1.0, 0.0 ] )

  print ''
  print '  Triangle vertices:'
  print '    (X1,Y1) = (%g,%g)' % ( t[0,0], t[0,1] )
  print '    (X2,Y2) = (%g,%g)' % ( t[1,0], t[1,1] )
  print '    (X3,Y3) = (%g,%g)' % ( t[2,0], t[2,1] )

  print ''
  poly_print ( d, p, '  Integrand p(x,y)' )

  q = triangle_poly_integral ( d, p, t )
  q2 = 1.0 / 6.0

  print ''
  print '  Computed Q = %g' % ( q )
  print '  Exact Q    = %g' % ( q2 )
#
#  Test 2:
#  Integrate xy over a general triangle.
#
  t = np.array ( [ \
     [ 0.0, 0.0 ], \
     [ 1.0, 0.0 ], \
     [ 1.0, 2.0 ] ] )

  d = 2
  p = np.array ( [ 0.0, 0.0, 0.0, 0.0, 1.0, 0.0 ] )

  print ''
  print '  Triangle vertices:'
  print '    (X1,Y1) = (%g,%g)' % ( t[0,0], t[0,1] )
  print '    (X2,Y2) = (%g,%g)' % ( t[1,0], t[1,1] )
  print '    (X3,Y3) = (%g,%g)' % ( t[2,0], t[2,1] )

  print ''
  poly_print ( d, p, '  Integrand p(x,y)' )

  q = triangle_poly_integral ( d, p, t )
  q2 = 0.5

  print ''
  print '  Computed Q = %g' % ( q )
  print '  Exact Q    = %g' % ( q2 )
#
#  Test 3:
#  Integrate 2-3x+xy over a general triangle.
#
  t = np.array ( [ \
     [ 0.0, 0.0 ], \
     [ 1.0, 0.0 ], \
     [ 1.0, 3.0 ] ] )

  d = 2
  p = np.array ( [ 2.0, -3.0, 0.0, 0.0, 1.0, 0.0 ] )

  print ''
  print '  Triangle vertices:'
  print '    (X1,Y1) = (%g,%g)' % ( t[0,0], t[0,1] )
  print '    (X2,Y2) = (%g,%g)' % ( t[1,0], t[1,1] )
  print '    (X3,Y3) = (%g,%g)' % ( t[2,0], t[2,1] )

  print ''
  poly_print ( d, p, '  Integrand p(x,y)' )

  q = triangle_poly_integral ( d, p, t )
  q2 = 9.0 / 8.0

  print ''
  print '  Computed Q = %g' % ( q )
  print '  Exact Q    = %g' % ( q2 )
#
#  Test 4:
#  Integrate -40y + 6x^2 over a general triangle.
#
  t = np.array ( [ \
     [ 0.0, 3.0 ], \
     [ 1.0, 1.0 ], \
     [ 5.0, 3.0 ] ] )

  d = 2
  p = np.array ( [ 0.0, 0.0,-40.0, 6.0, 0.0, 0.0 ] )

  print ''
  print '  Triangle vertices:'
  print '    (X1,Y1) = (%g,%g)' % ( t[0,0], t[0,1] )
  print '    (X2,Y2) = (%g,%g)' % ( t[1,0], t[1,1] )
  print '    (X3,Y3) = (%g,%g)' % ( t[2,0], t[2,1] )

  print ''
  poly_print ( d, p, '  Integrand p(x,y)' )

  q = triangle_poly_integral ( d, p, t )
  q2 = - 935.0 / 3.0

  print ''
  print '  Computed Q = %g' % ( q )
  print '  Exact Q    = %g' % ( q2 )
#
#  Terminate.
#
  print ''
  print 'TRIANGLE_POLY_INTEGRAL_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  triangle_poly_integral_test ( )
  timestamp ( )
