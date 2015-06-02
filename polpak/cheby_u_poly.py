#!/usr/bin/env python
#
def cheby_u_poly ( m, n, x ):

#*****************************************************************************80
#
## CHEBY_U_POLY evaluates Chebyshev polynomials U(n,x).
#
#  Differential equation:
#
#    (1-X*X) Y'' - 3 X Y' + N (N+2) Y = 0
#
#  First terms:
#
#    U(0,X) =   1
#    U(1,X) =   2 X
#    U(2,X) =   4 X^2 -   1
#    U(3,X) =   8 X^3 -   4 X
#    U(4,X) =  16 X^4 -  12 X^2 +  1
#    U(5,X) =  32 X^5 -  32 X^3 +  6 X
#    U(6,X) =  64 X^6 -  80 X^4 + 24 X^2 - 1
#    U(7,X) = 128 X^7 - 192 X^5 + 80 X^3 - 8X
#
#  Recursion:
#
#    U(0,X) = 1,
#    U(1,X) = 2 * X,
#    U(N,X) = 2 * X * U(N-1,X) - U(N-2,X)
#
#  Norm:
#
#    Integral ( -1 <= X <= 1 ) ( 1 - X^2 ) * U(N,X)^2 dX = PI/2
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    23 July 2004
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, the number of evaluation points.
#
#    Input, integer N, the highest polynomial to compute.
#
#    Input, real X(M), the evaluation points.
#
#    Output, real V(M,N+1), the values of the Chebyshev polynomials 
#    0 through N at X(1:M).
#
  import numpy as np
 
  v = np.zeros ( [ m, n + 1 ] )

  for i in range ( 0, m ):
    v[i,0] = 1.0
 
  if ( n < 1 ):
    return v

  for i in range ( 0, m ):
    v[i,1] = 2.0 * x[i]
 
  for j in range ( 1, n ):
    for i in range ( 0, m ):
      v[i,j+1] = 2.0 * x[i] * v[i,j] - v[i,j-1]
  
  return v

def cheby_u_poly_test ( ):

#*****************************************************************************80
#
## CHEBY_U_POLY_TEST tests CHEBY_U_POLY.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 January 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  from cheby_u_poly_values import cheby_u_poly_values

  n_max = 12
  xv = np.zeros ( 1 )

  print ''
  print 'CHEBY_U_POLY_TEST'
  print '  CHEBY_U_POLY evaluates the Chebyshev U polynomial.'
  print ''
  print '     N      X        Exact F       U(N)(X)'
  print ''

  n_data = 0

  while ( True ):

    [ n_data, n, x, fx ] = cheby_u_poly_values ( n_data )

    if ( n_data == 0 ):
      break

    m = 1
    xv[0] = x
    v = cheby_u_poly ( m, n, xv )
    fx2 = v[0,n]

    print '  %6d  %8g  %12g  %12g' % ( n, x, fx, fx2 )

 
  print ''
  print 'CHEBY_U_POLY_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  cheby_u_poly_test ( )
  timestamp ( )
