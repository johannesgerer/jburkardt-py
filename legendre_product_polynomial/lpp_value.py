#!/usr/bin/env python

def lpp_value ( m, n, o, x ):

#*****************************************************************************80
#
## LPP_VALUE evaluates a Legendre Product Polynomial at several points X.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    31 October 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, int M, the spatial dimension.
#
#    Input, int N, the number of evaluation points.
#
#    Input, int O[M], the degree of the polynomial factors.
#    0 <= O(*).
#
#    Input, double X[M][N], the evaluation points.
#
#    Output, double V[N], the value of the Legendre Product 
#    Polynomial of degree O at the points X.
#
  from lp_value import lp_value
  import numpy as np

  v = np.zeros ( n, dtype = np.float64 )

  for j in range ( 0, n ):
    v[j] = 1.0

  xi = np.zeros ( n, dtype = np.float64 )
 
  for i in range ( 0, m ):
    for j in range ( 0, n ):
      xi[j] = x[i][j]
    vi = lp_value ( n, o[i], xi )
    for j in range ( 0, n ):
      v[j] = v[j] * vi[j]

  return v

def lpp_value_test ( ):

#*****************************************************************************80
#
## LPP_VALUE_TEST tests LPP_VALUE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    31 October 2014
#
#  Author:
#
#    John Burkardt
#
  from comp_unrank_grlex import comp_unrank_grlex
  from lpp_to_polynomial import lpp_to_polynomial
  from polynomial_value import polynomial_value
  from r8mat_uniform_ab import r8mat_uniform_ab

  print ''
  print 'LPP_VALUE_TEST:'
  print '  LPP_VALUE evaluates a Legendre product polynomial.'

  m = 3
  n = 1
  xlo = -1.0
  xhi = +1.0
  seed = 123456789
  x, seed = r8mat_uniform_ab ( m, n, xlo, xhi, seed )

  print ''
  print '  Evaluate at X = ',
  for j in range ( 0, n ):
    for i in range ( 0, m ):
      print '%g  ' % ( x[i][j] ),
  print ''
  print ''
  print '  Rank  I1  I2  I3:  L(I1,X1)*L(I2,X2)*L(I3,X3)    P(X1,X2,X3)'
  print ''

  for rank in range ( 1, 21 ):
    l = comp_unrank_grlex ( m, rank )
#
#  Evaluate the LPP directly.
#
    v1 = lpp_value ( m, n, l, x )
#
#  Convert the LPP to a polynomial.
#
    o_max = 1
    for i in range ( 0, m ):
      o_max = o_max * ( l[i] + 2 ) // 2
 
    o, c, e = lpp_to_polynomial ( m, l, o_max )
#
#  Evaluate the polynomial.
#
    v2 = polynomial_value ( m, o, c, e, n, x )
#
#  Compare results.
#
    print '  %4d  %2d  %2d  %2d  %14.6g  %14.6g' % \
      ( rank, l[0], l[1], l[2], v1[0], v2[0] )

  print ''
  print 'LPP_VALUE_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp

  timestamp ( )
  lpp_value_test ( )
  timestamp ( )
