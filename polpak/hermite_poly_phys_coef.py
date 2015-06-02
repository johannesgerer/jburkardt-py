#!/usr/bin/env python
#
def hermite_poly_phys_coef ( n ):

#*****************************************************************************80
#
## HERMITE_POLY_PHYS_COEF: coefficients of the physicist's Hermite polynomial H(n,x).
#
#  First terms:
#
#    N/K     0     1      2      3       4     5      6    7      8    9   10
#
#     0      1
#     1      0     2
#     2     -2     0      4
#     3      0   -12      0      8
#     4     12     0    -48      0      16
#     5      0   120      0   -160       0    32
#     6   -120     0    720      0    -480     0     64
#     7      0 -1680      0   3360       0 -1344      0   128
#     8   1680     0 -13440      0   13440     0  -3584     0    256
#     9      0 30240      0 -80640       0 48384      0 -9216      0 512
#    10 -30240     0 302400      0 -403200     0 161280     0 -23040   0 1024 
#
#  Recursion:
#
#    H(0,X) = 1,
#    H(1,X) = 2*X,
#    H(N,X) = 2*X * H(N-1,X) - 2*(N-1) * H(N-2,X)
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 February 2015
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
#    Output, real C(1:N+1,1:N+1), the coefficients of the Hermite
#    polynomials.
#
  import numpy as np

  c = np.zeros ( ( n + 1, n + 1 ) )

  c[0,0] = 1.0

  if ( 0 < n ):

    c[1,1] = 2.0
 
    for i in range ( 1, n ):
      c[i+1,0]     =  -2.0 * float ( i ) * c[i-1,0]
      for j in range ( 1, i ):
        c[i+1,j] =   2.0 * c[i,j-1] -2.0 * float ( i ) * c[i-1,j]
      c[i+1,i  ] =   2.0 * c[i  ,  i-1]
      c[i+1,i+1] =   2.0 * c[i  ,  i  ]

  return c

def hermite_poly_phys_coef_test ( ):

#*****************************************************************************80
#
## HERMITE_POLY_PHYS_COEF_TEST tests HERMITE_POLY_PHYS_COEF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 February 2015
#
#  Author:
#
#    John Burkardt
#
  n = 5

  print ''
  print 'HERMITE_POLY_PHYS_COEF_TEST'
  print '  HERMITE_POLY_PHYS_COEF determines the Hermite'
  print '  physicist\'s polynomial coefficients.'

  c = hermite_poly_phys_coef ( n )
 
  for i in range ( 0, n + 1 ):
    print ''
    print '  H(%d)' % ( i )
    print ''
    for j in range ( i, -1, -1 ):
      if ( j == 0 ):
        print '    %f' % ( c[i,j] )
      elif ( j == 1 ):
        print '    %f * x' % ( c[i,j] )
      else:
        print '    %f * x^%d' % ( c[i,j], j )

  print ''
  print 'HERMITE_POLY_PHYS_COEF_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  hermite_poly_phys_coef_test ( )
  timestamp ( )
