#! /usr/bin/env python
#
def poly_product ( d1, p1, d2, p2 ):

#*****************************************************************************80
#
#% POLY_PRODUCT computes P3(x,y) = P1(x,y) * P2(x,y) for polynomials.
#
#  Location:
#
#    http://people.sc.fsu.edu/~jburkardt/py_src/triangle_integrals/poly_product.py
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 April 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer D1, the degree of factor 1.
#
#    Input, real P1(M1), the factor 1 coefficients.
#    M1 = ((D1+1)*(D1+2))/2.
#
#    Input, integer D2, the degree of factor 2.
#
#    Input, real P2(M2), the factor2 coefficients.
#    M2 = ((D2+1)*(D2+2))/2.
#
#    Output, integer D3, the degree of the result.
#
#    Output, real P3(M3), the result coefficients.
#    M3 = ((D3+1)*(D3+2))/2.
#
  import numpy as np
  from i4_to_pascal import i4_to_pascal
  from pascal_to_i4 import pascal_to_i4

  d3 = d1 + d2
  m3 = ( ( d3 + 1 ) * ( d3 + 2 ) ) / 2
  p3 = np.zeros ( m3 )
#
#  Consider each entry in P1:
#    P1(K1) * X^I1 * Y^J1
#  and multiply it by each entry in P2:
#    P2(K2) * X^I2 * Y^J2
#  getting 
#    P3(K3) = P3(K3) + P1(K1) * P2(X2) * X^(I1+I2) * Y(J1+J2)
#
  m1 = ( ( d1 + 1 ) * ( d1 + 2 ) ) / 2
  m2 = ( ( d2 + 1 ) * ( d2 + 2 ) ) / 2

  for k1m1 in range ( 0, m1 ):
    k1 = k1m1 + 1
    i1, j1 = i4_to_pascal ( k1 )
    for k2m1 in range ( 0, m2 ):
      k2 = k2m1 + 1
      i2, j2 = i4_to_pascal ( k2 )
      i3 = i1 + i2
      j3 = j1 + j2
      k3 = pascal_to_i4 ( i3, j3 )
      k3m1 = k3 - 1
      p3[k3m1] = p3[k3m1] + p1[k1m1] * p2[k2m1]

  return d3, p3

def poly_product_test ( ):

#*****************************************************************************80
#
## POLY_PRODUCT_TEST tests POLY_PRODUCT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 April 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  from poly_print import poly_print

  print ''
  print 'POLY_PRODUCT_TEST:'
  print '  POLY_PRODUCT computes the product of two X,Y polynomials.'
#
#  P1 = ( 1 + 2 x + 3 y )
#  P2 = ( 4 + 5 x )
#  P3 = 4 + 13x + 12y + 10x^2 + 15xy + 0y^2 
#
  d1 = 1
  p1 = np.array ( [ 1.0, 2.0, 3.0 ] )
  print ''
  poly_print ( d1, p1, '  p1(x,y)' )

  d2 = 1
  p2 = np.array ( [ 4.0, 5.0, 0.0 ] )
  print ''
  poly_print ( d2, p2, '  p2(x,y)' )

  d3, p3 = poly_product ( d1, p1, d2, p2 )
  print ''
  poly_print ( d3, p3, '  p3(x,y) = p1(x,y) * p2(x,y)' )

  dc = 2
  pc = np.array ( [ 4.0, 13.0, 12.0, 10.0, 15.0, 0.0 ] )
  print ''
  poly_print ( dc, pc, '  Correct answer: p3(x,y)=p1(x,y)*p2(x,y)' )
#
#  P1 = ( 1 - 2 x + 3 y - 4x^2 + 5xy - 6y^2)
#  P2 = ( 7 + 3x^2 )
#  P3 = 7 
#    - 14x + 21y 
#    - 25 x^2 + 35 xy -  42y^2 
#    -  6x^3  + 9x^2y +  0xy^2   + 0y^3
#    - 12x^4 + 15x^3y - 18x^2y^2 + 0 xy^3 + 0y^4
#
  d1 = 2
  p1 = np.array ( [ 1.0, -2.0, 3.0, -4.0, +5.0, -6.0 ] )
  print ''
  poly_print ( d1, p1, '  p1(x,y)' )

  d2 = 2
  p2 = np.array ( [ 7.0, 0.0, 0.0, 3.0, 0.0, 0.0 ] )
  print ''
  poly_print ( d2, p2, '  p2(x,y)' )

  d3, p3 = poly_product ( d1, p1, d2, p2 )
  print ''
  poly_print ( d3, p3, '  p3(x,y) = p1(x,y) * p2(x,y)' )

  dc = 4
  pc = np.array ( [ \
      7.0, \
    -14.0,  21.0, \
    -25.0, +35.0, -42.0, \
     -6.0,   9.0,   0.0, 0.0, \
    -12.0, +15.0, -18.0, 0.0, 0.0 ] )
  print ''
  poly_print ( dc, pc, '  Correct answer: p3(x,y)=p1(x,y)*p2(x,y)' )

#
#  Terminate.
#
  print ''
  print 'POLY_PRODUCT_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  poly_product_test ( )
  timestamp ( )
