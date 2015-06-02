#!/usr/bin/env python
#
def legendre_poly_coef ( n ):

#*****************************************************************************80
#
## LEGENDRE_POLY_COEF evaluates the Legendre polynomial coefficients.
#
#  First terms:
#
#     1
#     0     1
#    -1/2   0      3/2
#     0    -3/2    0     5/2
#     3/8   0    -30/8   0     35/8
#     0    15/8    0   -70/8    0     63/8
#    -5/16  0    105/16  0   -315/16   0    231/16
#     0   -35/16   0   315/16   0   -693/16   0    429/16
#
#     1.00000
#     0.00000  1.00000
#    -0.50000  0.00000  1.50000
#     0.00000 -1.50000  0.00000  2.5000
#     0.37500  0.00000 -3.75000  0.00000  4.37500
#     0.00000  1.87500  0.00000 -8.75000  0.00000  7.87500
#    -0.31250  0.00000  6.56250  0.00000 -19.6875  0.00000  14.4375
#     0.00000 -2.1875   0.00000  19.6875  0.00000 -43.3215  0.00000  26.8125
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Milton Abramowitz and Irene Stegun,
#    Handbook of Mathematical Functions,
#    US Department of Commerce, 1964.
#
#    Daniel Zwillinger, editor,
#    CRC Standard Mathematical Tables and Formulae,
#    30th Edition,
#    CRC Press, 1996.
#
#  Parameters:
#
#    Input, integer N, the highest order polynomial to evaluate.
#    Note that polynomials 0 through N will be evaluated.
#
#    Output, real C(1:N+1,1:N+1), the coefficients of the Legendre polynomials 
#    of degree 0 through N.  Each polynomial is stored as a row.
#
  import numpy as np

  c = np.zeros ( ( n + 1, n + 1 ) )

  c[0,0] = 1.0

  if ( 0 < n ):

    c[1,1] = 1.0
 
    for i in range ( 2, n + 1 ):
      for j in range ( 0, i ):
        c[i,j] =          float (   - i + 1 ) * c[i-2,j] / float ( i )
      for j in range ( 1, i + 1 ):
        c[i,j] = c[i,j] + float ( i + i - 1 ) * c[i-1,j-1] / float ( i )

  return c

def legendre_poly_coef_test ( ):

#*****************************************************************************80
#
## LEGENDRE_POLY_COEF_TEST tests LEGENDRE_POLY_COEF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 February 2015
#
#  Author:
#
#    John Burkardt
#
  n = 5

  print ''
  print 'LEGENDRE_POLY_COEF_TEST'
  print '  LEGENDRE_POLY_COEF determines the Legendre'
  print '  polynomial coefficients.'

  c = legendre_poly_coef ( n )
 
  for i in range ( 0, n + 1 ):
    print ''
    print '  L(%d)' % ( i )
    print ''
    for j in range ( i, -1, -1 ):
      if ( j == 0 ):
        print '    %f' % ( c[i,j] )
      elif ( j == 1 ):
        print '    %f * x' % ( c[i,j] )
      else:
        print '    %f * x^%d' % ( c[i,j], j )

  print ''
  print 'LEGENDRE_POLY_COEF_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  legendre_poly_coef_test ( )
  timestamp ( )
