#!/usr/bin/env python
#
def bpab ( n, x, a, b ):

#*****************************************************************************80
#
## BPAB evaluates at X the Bernstein polynomials based in [A,B].
#
#  Formula:
#
#    BERN(N,I)(X) = [N!/(I!*(N-I)!)] * (B-X)^(N-I) * (X-A)^I / (B-A)^N
#
#  First values:
#
#    B(0,0)(X) =   1
#
#    B(1,0)(X) = (      B-X              ) / (B-A)
#    B(1,1)(X) = (                X-A    ) / (B-A)
#
#    B(2,0)(X) = (     (B-X)^2           ) / (B-A)^2
#    B(2,1)(X) = ( 2 * (B-X)   * (X-A)   ) / (B-A)^2
#    B(2,2)(X) = (               (X-A)^2 ) / (B-A)^2
#
#    B(3,0)(X) = (     (B-X)^3           ) / (B-A)^3
#    B(3,1)(X) = ( 3 * (B-X)^2 * (X-A)   ) / (B-A)^3
#    B(3,2)(X) = ( 3 * (B-X)   * (X-A)^2 ) / (B-A)^3
#    B(3,3)(X) = (               (X-A)^3 ) / (B-A)^3
#
#    B(4,0)(X) = (     (B-X)^4           ) / (B-A)^4
#    B(4,1)(X) = ( 4 * (B-X)^3 * (X-A)   ) / (B-A)^4
#    B(4,2)(X) = ( 6 * (B-X)^2 * (X-A)^2 ) / (B-A)^4
#    B(4,3)(X) = ( 4 * (B-X)   * (X-A)^3 ) / (B-A)^4
#    B(4,4)(X) = (               (X-A)^4 ) / (B-A)^4
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 July 2004
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the degree of the Bernstein polynomials to be used.
#    For any N, there is a set of N+1 Bernstein polynomials, each of
#    degree N, which form a basis for polynomials on [A,B].
#
#    Input, real X, the point at which the polynomials are to be evaluated.
#
#    Input, real A, B, the endpoints of the interval on which the
#    polynomials are to be based.  A and B should not be equal.
#
#    Output, real BERN(0:N), the values of the N+1 Bernstein polynomials at X.
#
  import numpy as np
  from sys import exit

  if ( b == a ):
    print ''
    print 'BPAB - Fatal error!'
    print '  A = B = %f' % ( a )
    exit ( 'BPAB - Fatal error!' )

  bern = np.zeros ( n + 1 )

  if ( n == 0 ):
 
    bern[0] = 1.0;
 
  else:
 
    bern[0] = ( b - x ) / ( b - a );
    bern[1] = ( x - a ) / ( b - a );
 
    for i in range ( 1, n ):
      bern[i+1] = ( x - a ) * bern[i] / ( b - a )
      for j in range ( i - 1, -1, -1 ):
        bern[j+1] = ( ( b - x ) * bern[j+1] + ( x - a ) * bern[j] ) / ( b - a )
      bern[0] = ( b - x ) * bern[0] / ( b - a )

  return bern

def bpab_test ( ):

#*****************************************************************************80
#
## BPAB_TEST tests BPAB.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    01 January 2015
#
#  Author:
#
#    John Burkardt
#
  n = 10
  x = 0.3
  a = 0.0
  b = 1.0
  bern = bpab ( n, x, a, b )

  print ''
  print 'BPAB_TEST'
  print '  BPAB computes Bernstein polynomials;'
  print ''
  print '  The Bernstein polynomials of degree %d' % ( n )
  print '  based on the interval [%f,%f]' % ( a, b )
  print '  evaluated at X = %g' % ( x )
  print ''
  print '   I        Bern(I,X)'
  print ''
  
  for i in range ( 0, n + 1 ):
    print '  %2d  %12g' % ( i, bern[i] )
 
  print ''
  print 'BPAB_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  bpab_test ( )
  timestamp ( )
