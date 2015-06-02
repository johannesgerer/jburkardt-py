#!/usr/bin/env python
#
def laguerre_poly_coef ( n ):

#*****************************************************************************80
#
## LAGUERRE_POLY_COEF evaluates the Laguerre polynomial coefficients.
#
#  First terms:
#
#    0: 1
#    1: 1  -1
#    2: 1  -2  1/2
#    3: 1  -3  3/2  1/6
#    4: 1  -4  4   -2/3  1/24
#    5: 1  -5  5   -5/3  5/24  -1/120
#
#  Recursion:
#
#    L(0) = ( 1,  0, 0, ..., 0 )
#    L(1) = ( 1, -1, 0, ..., 0 )
#    L(N) = (2*N-1-X) * L(N-1) - (N-1) * L(N-2) / N
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 July 2004
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
#  Parameters:
#
#    Input, integer N, the highest order polynomial to compute.
#    Note that polynomials 0 through N will be computed.
#
#    Output, real C(1:N+1,1:N+1), the coefficients of the Laguerre polynomials 
#    of degree 0 through N.  Each polynomial is stored as a row.
#
  import numpy as np

  c = np.zeros ( ( n + 1, n + 1 ) )

  for i in range ( 0, n + 1 ):
    c[i,0] = 1.0
 
  if ( 0 < n ):

    c[1,1] = -1.0
 
    for i in range ( 2, n + 1 ):
      for j in range ( 1, n + 1 ):
        c[i,j] = ( \
            float ( 2 * i - 1 ) * c[i-1,j] \
          + float (   - i + 1 ) * c[i-2,j] \
          -                       c[i-1,j-1] ) / float ( i )

  return c

def laguerre_poly_coef_test ( ):

#*****************************************************************************80
#
## LAGUERRE_POLY_COEF_TEST tests LAGUERRE_POLY_COEF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    18 February 2015
#
#  Author:
#
#    John Burkardt
#
  n = 5

  print ''
  print 'LAGUERRE_POLY_COEF_TEST'
  print '  LAGUERRE_POLY_COEF determines the Laguerre'
  print '  polynomial coefficients.'

  c = laguerre_poly_coef ( n )
 
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

  fact = 1.0

  for i in range ( 0, n + 1 ):

    if ( 0 < i ):
      fact = fact * i

    print ''
    print '  Factorially scaled L(%d)' % ( i )
    print ''
    for j in range ( i, -1, -1 ):
      if ( j == 0 ):
        print '    %f' % ( fact * c[i,j] )
      elif ( j == 1 ):
        print '    %f * x' % ( fact * c[i,j] )
      else:
        print '    %f * x^%d' % ( fact * c[i,j], j )


  print ''
  print 'LAGUERRE_POLY_COEF_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  laguerre_poly_coef_test ( )
  timestamp ( )
