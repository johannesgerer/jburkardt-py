#! /usr/bin/env python
#
def poly_power ( d1, p1, n ):

#*****************************************************************************80
#
## POLY_POWER computes a power of a polynomial.
#
#  Location:
#
#    http://people.sc.fsu.edu/~jburkardt/py_src/triangle_integrals/poly_power.py
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
#    Input, integer D1, the degree of the polynomial.
#
#    Input, real P1(M1), the polynomial coefficients.
#    M1 = ((D1+1)*(D1+2))/2.
#
#    Input, integer N, the nonnegative integer power.
#
#    Output, integer D2, the degree of the power polynomial.
#    D2 = N * D1.
#
#    Output, real P2(M2), the polynomial power.
#    M2 = ((D2+1)*(D2+2))/2.
#
  import numpy as np
  from poly_product import poly_product
#
#  Create P2, a polynomial representation of 1.
#
  d2 = 0
  m2 = ( ( d2 + 1 ) * ( d2 + 2 ) ) / 2
  p2 = np.zeros ( m2 )
  p2[0] = 1.0
#
#  Iterate N times:
#    P2 <= P2 * P1
#
  for i in range ( 0, n ):
    d2, p2 = poly_product ( d2, p2, d1, p1 )

  return d2, p2

def poly_power_test ( ):

#*****************************************************************************80
#
## POLY_POWER_TEST tests POLY_POWER.
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
  print 'POLY_POWER_TEST:'
  print '  POLY_POWER computes the N-th power of an X,Y polynomial.'
#
#  P1 = ( 1 + 2 x + 3 y )
#  P2 = P1^2 = 1 + 4x + 6y + 4x^2 + 12xy + 9y^2 
#
  d1 = 1
  p1 = np.array ( [ 1.0, 2.0, 3.0 ] )
  n = 2

  print ''
  poly_print ( d1, p1, '  p1(x,y)' )

  d2, p2 = poly_power ( d1, p1, n )
  print ''
  poly_print ( d2, p2, '  p2(x,y) = p1(x,y)^2' )

  d3 = 2
  p3 = np.array ( [ 1.0, 4.0, 6.0, 4.0, 12.0, 9.0 ] )
  print ''
  poly_print ( d3, p3, '  p3(x,y)=correct answer' )
#
#  P1 = ( 1 - 2 x + 3 y - 4 x^2 + 5 xy - 6 y^2 )
#  P2 = P1^3 =
#    1
#    -6x +9y
#    +0x^2 - 21xy + 9y^2
#    +40x^3 - 96x^2y  + 108x^y2 - 81y^3
#    +0x^4 + 84x^3y - 141 x^2y^2 +171xy^3 - 54y^4
#    -96x^5 + 384x^4y -798x^3y^2 + 1017 x^2y^3 - 756 xy^4 + 324 y^5
#    -64x^6 + 240x^5y - 588x^4y^2 + 845 x^3y^3 - 882 x^2y^4 +540 xy^5 - 216y^6
#
  d1 = 2
  p1 = np.array ( [ 1.0, -2.0, 3.0, -4.0, +5.0, -6.0 ] )
  n = 3

  print ''
  poly_print ( d1, p1, '  p1(x,y)' )

  d2, p2 = poly_power ( d1, p1, n )
  print ''
  poly_print ( d2, p2, '  p2(x,y) = p1(x,y)^3' )

  d3 = 6
  p3 = np.array ( [ \
      1.0, \
     -6.0,  9.0, \
      0.0, -21.0,    9.0, \
     40.0, -96.0,  108.0,  -81.0, \
      0.0,  84.0, -141.0,  171.0,  -54.0, \
    -96.0, 384.0, -798.0, 1017.0, -756.0, 324.0, \
    -64.0, 240.0, -588.0,  845.0, -882.0, 540.0, -216.0 ] );
  print ''
  poly_print ( d3, p3, '  p3(x,y)=correct answer' )
#
#  Terminate.
#
  print ''
  print 'POLY_POWER_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  poly_power_test ( )
  timestamp ( )
