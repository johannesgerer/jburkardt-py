#!/usr/bin/env python
#
def bernoulli_poly ( n, x ):

#*****************************************************************************80
#
## BERNOULLI_POLY evaluates the Bernoulli polynomial of order N at X.
#
#  Discussion:
#
#    Thanks to Bart Vandewoestyne for pointing out an error in the previous
#    documentation, 31 January 2008.
#
#    Special values of the Bernoulli polynomial include:
#
#      B(N,0) = B(N,1) = B(N), the N-th Bernoulli number.
#
#      B'(N,X) = N * B(N-1,X)
#
#      B(N,X+1) - B(N,X) = N * X^(N-1)
#      B(N,X) = (-1)^N * B(N,1-X)
#
#    A formula for the Bernoulli polynomial in terms of the Bernoulli
#    numbers is:
#
#      B(N,X) = sum ( 0 <= K <= N ) B(K) * C(N,K) * X^(N-K)
#
#    The first few polynomials include:
#
#      B(0,X) = 1
#      B(1,X) = X    - 1/2
#      B(2,X) = X^2 -   X      +  1/6
#      B(3,X) = X^3 - 3/2*X^2 +  1/2*X
#      B(4,X) = X^4 - 2*X^3   +      X^2 - 1/30
#      B(5,X) = X^5 - 5/2*X^4 +  5/3*X^3 - 1/6*X
#      B(6,X) = X^6 - 3*X^5   +  5/2*X^4 - 1/2*X^2 + 1/42
#      B(7,X) = X^7 - 7/2*X^6 +  7/2*X^5 - 7/6*X^3 + 1/6*X
#      B(8,X) = X^8 - 4*X^7   + 14/3*X^6 - 7/3*X^4 + 2/3*X^2 - 1/30
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the order of the Bernoulli polynomial to
#    be evaluated.  N must be 0 or greater.
#
#    Input, real X, the value of X at which the polynomial is to
#    be evaluated.
#
#    Output, real BX, the value of B(N,X).
#
  import numpy as np
  from bernoulli_number import bernoulli_number
  from comb_row_next import comb_row_next

  b = bernoulli_number ( n );
#
#  Get row N of Pascal's triangle.
#
  c = np.zeros ( n + 1 )

  for i in range ( 0, n + 1 ):
    c = comb_row_next ( i, c )
 
  bx = 1.0
  for i in range ( 1, n + 1 ):
    bx = bx * x + b[i] * c[i]

  return bx

def bernoulli_poly_test ( ):

#*****************************************************************************80
#
## BERNOULLI_POLY_TEST tests BERNOULLI_POLY.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 December 2014
#
#  Author:
#
#    John Burkardt
#
  n = 15
  x = 0.2

  print ''
  print 'BERNOULLI_POLY_TEST'
  print '  BERNOULLI_POLY computes Bernoulli polynomials;'
  print ''
  print '  X = %g' % ( x )
  print ''
  print '   I      B(I,X)'
  print ''

  for i in range ( 1, n + 1 ):

    bx = bernoulli_poly ( i, x )
    print '  %2d  %14g' % ( i, bx )

 
  print ''
  print 'BERNOULLI_POLY_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  bernoulli_poly_test ( )
  timestamp ( )
