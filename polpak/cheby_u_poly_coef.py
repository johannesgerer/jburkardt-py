#!/usr/bin/env python
#
def cheby_u_poly_coef ( n ):

#*****************************************************************************80
#
## CHEBY_U_POLY_COEF evaluates coefficients of Chebyshev polynomials U(n,x).
#
#  First terms:
#
#    N/K     0     1      2      3       4     5      6    7      8    9   10
#
#     0      1
#     1      0     2
#     2     -1     0      4
#     3      0    -4      0      8
#     4      1     0    -12      0      16
#     5      0     6      0    -32       0    32
#     6     -1     0     24      0     -80     0     64
#     7      0    -8      0     80       0  -192      0   128
#
#  Recursion:
#
#    U(0)(X) = 1,
#    U(1)(X) = 2 * X,
#    U(N)(X) = 2 * X * U(N-1)(X) - U(N-2)(X)
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 January 2015
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
#    Output, real C[0:N,0:N], the coefficients of the Chebyshev T
#    polynomials.
#
  import numpy as np

  c = np.zeros ( [ n + 1, n + 1 ] )
 
  c[0,0] = 1.0

  if ( 0 < n ):
 
    c[1,1] = 2.0
 
    for i in range ( 1, n ):
      c[i+1,0] = - c[i-1,0]
      for j in range ( 1, i ):
        c[i+1,j] = 2.0 * c[i,j-1] - c[i-1,j]
      c[i+1,  i  ] = 2.0 * c[i,  i-1]
      c[i+1,  i+1] = 2.0 * c[i,  i  ]

  return c

def cheby_u_poly_coef_test ( ):

#*****************************************************************************80
#
## CHEBY_U_POLY_COEF_TEST tests CHEBY_U_POLY_COEF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 January 2015
#
#  Author:
#
#    John Burkardt
#
  n = 5

  print ''
  print 'CHEBY_U_POLY_COEF_TEST'
  print '  CHEBY_U_POLY_COEF determines the Chebyshev U'
  print '  polynomial coefficients.'

  c = cheby_u_poly_coef ( n )
 
  for i in range ( 0, n + 1 ):
    print ''
    print '  U(%d)' % ( i )
    print ''
    for j in range ( i, -1, -1 ):
      if ( j == 0 ):
        print '    %f' % ( c[i,j] )
      elif ( j == 1 ):
        print '    %f * x' % ( c[i,j] )
      else:
        print '    %f * x^%d' % ( c[i,j], j )

  print ''
  print 'CHEBY_U_POLY_COEF_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  cheby_u_poly_coef_test ( )
  timestamp ( )
