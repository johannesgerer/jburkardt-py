#! /usr/bin/env python
#
def poly_power_linear ( d1, p1, n ):

#*****************************************************************************80
#
## POLY_POWER_LINEAR computes the polynomial ( a + b*x + c*y ) ^ n.
#
#  Location:
#
#    http://people.sc.fsu.edu/~jburkardt/py_src/triangle_integrals/poly_power_linear.py
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
#    Input, integer D1, the degree of the linear polynomial,
#    which should be 1.
#
#    Input, real P1(M1), the coefficients of the linear polynomial.
#    M1 = ( (D1+1)*(D1+2) ) / 2, which should be 3.
#
#    Input, integer N, the power to which the polynomial is to be raised.
#    0 <= N.
#
#    Output, integer D2, the degree of the power polyynomial, which
#    should be D2 = N * D1 = N.
#
#    Output, real P2(M2), the coefficients of the power polynomial.
#    M2 = ( (D2+1)*(D2+2) ) / 2, which should be ((N+1)*(N+2))/2.
#
  import numpy as np
  from pascal_to_i4 import pascal_to_i4
  from sys import exit
  from trinomial import trinomial

  if ( d1 < 0 ):
    print ''
    print 'POLY_POWER_LINEAR - Fatal error!'
    print '  D1 < 0.'
    exit ( 'POLY_POWER_LINEAR - Fatal error!' )

  if ( n < 0 ):
    print ''
    print 'POLY_POWER_LINEAR - Fatal error!'
    print '  N < 0.'
    exit ( 'POLY_POWER_LINEAR - Fatal error!' )

  d2 = n * d1
  m2 = ( ( d2 + 1 ) * ( d2 + 2 ) ) / 2
  p2 = np.zeros ( m2 )

  if ( d1 == 0 ):
    p2[0] = p1[0] ** n
    return d2, p2

  if ( n == 0 ):
    p2[0] = 1.0
    return d2, p2
#
#  Use the Trinomial formula.
#
  for i in range ( 0, n + 1 ):
    for j in range ( 0, n - i + 1 ):
      for k in range ( 0, n - i - j + 1 ):
#
#  We store X^J Y^K in location L.
#
        l = pascal_to_i4 ( j, k )
        lm1 = l - 1
        p2[lm1] = trinomial ( i, j, k ) * p1[0] ** i * p1[1] ** j * p1[2] ** k

  return d2, p2

def poly_power_linear_test ( ):

#*****************************************************************************80
#
## POLY_POWER_LINEAR_TEST tests POLY_POWER_LINEAR.
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
  print 'POLY_POWER_LINEAR_TEST:'
  print '  POLY_POWER_LINEAR computes the N-th power of'
  print '  a linear polynomial in X and Y.'
#
#  P = ( 1 + 2 x + 3 y )^2
#
  d1 = 1
  p1 = np.array ( [ 1.0, 2.0, 3.0 ] )
  print ''
  poly_print ( d1, p1, '  p1(x,y)' )

  dp, pp = poly_power_linear ( d1, p1, 2 )
  print ''
  poly_print ( dp, pp, '  p1(x,y)^n' )

  dc = 2
  pc = np.array ( [ 1.0, 4.0, 6.0, 4.0, 12.0, 9.0 ] )
  print ''
  poly_print ( dc, pc, '  Correct answer: p1(x,y)^2' )
#
#  P = ( 2 - x + 3 y )^3
#
  d1 = 1
  p1 = np.array ( [ 2.0, -1.0, 3.0 ] )
  print ''
  poly_print ( d1, p1, '  p1(x,y)' )

  dp, pp = poly_power_linear ( d1, p1, 3 )
  print ''
  poly_print ( dp, pp, '  p1(x,y)^3' )

  dc = 3
  pc = np.array ( [ 8.0, -12.0, 36.0, 6.0, -36.0, 54.0, -1.0, 9.0, -27.0, 27.0 ] )
  print ''
  poly_print ( dc, pc, '  Correct answer: p1(x,y)^n' )
#
#  Terminate.
#
  print ''
  print 'POLY_POWER_LINEAR_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  poly_power_linear_test ( )
  timestamp ( )
