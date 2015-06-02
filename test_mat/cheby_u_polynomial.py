#! /usr/bin/env python
#
def cheby_u_polynomial ( n, x ):

#*****************************************************************************80
#
## CHEBY_U_POLYNOMIAL evaluates the Chebyshev polynomials of the second kind.
#
#  Differential equation:
#
#    (1-X*X) Y'' - 3 X Y' + N (N+2) Y = 0
#
#  First terms:
#
#    U(0)(X) =   1
#    U(1)(X) =   2 X
#    U(2)(X) =   4 X^2 -   1
#    U(3)(X) =   8 X^3 -   4 X
#    U(4)(X) =  16 X^4 -  12 X^2 +  1
#    U(5)(X) =  32 X^5 -  32 X^3 +  6 X
#    U(6)(X) =  64 X^6 -  80 X^4 + 24 X^2 - 1
#    U(7)(X) = 128 X^7 - 192 X^5 + 80 X^3 - 8X
#
#  Recursion:
#
#    U(0)(X) = 1,
#    U(1)(X) = 2 * X,
#    U(N)(X) = 2 * X * U(N-1)(X) - U(N-2)(X)
#
#  Norm:
#
#    Integral ( -1 <= X <= 1 ) ( 1 - X^2 ) * U(N)(X)^2 dX = PI/2
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    14 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the highest polynomial to compute.
#
#    Input, real X, the point at which the polynomials are to be computed.
#
#    Output, real CX(1:N+1), the values of the N+1 Chebyshev polynomials.
#
  import numpy as np

  cx = np.zeros ( n + 1 )

  cx[0] = 1.0

  if ( n < 1 ):
    return cx

  cx[1] = 2.0 * x

  for i in range ( 2, n + 1 ):
    cx[i] = 2.0 * x * cx[i-1] - cx[i-2]

  return cx

def cheby_u_polynomial_test ( ):

#*****************************************************************************80
#
## CHEBY_U_POLYNOMIAL_TEST tests CHEBY_U_POLYNOMIAL.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    14 December 2014
#
#  Author:
#
#    John Burkardt
#
  from r8vec_print import r8vec_print

  print ''
  print 'CHEBY_U_POLYNOMIAL_TEST'
  print '  CHEBY_U_POLYNOMIAL evaluates Chebyshev U polynomials at X.'

  n = 10
  x = 0.25
  c = cheby_u_polynomial ( n, x )

  r8vec_print ( n + 1, c, '  Chebyshev U polynomials:' )

  print ''
  print 'CHEBY_U_POLYNOMIAL_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  cheby_u_polynomial_test ( )
  timestamp ( )
