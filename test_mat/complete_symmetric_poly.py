#!/usr/bin/env python

def complete_symmetric_poly ( n, r, x ):

#*****************************************************************************80
#
## COMPLETE_SYMMETRIC_POLY evaluates a complete symmetric polynomial.
#
#  Discussion:
#
#    N\R  0   1         2               3
#      +--------------------------------------------------------
#    0 |  1   0         0               0
#    1 |  1   X1        X1^2            X1^3
#    2 |  1   X1+X2     X1^2+X1X2+X2^2  X1^3+X1^2X2+X1X2^2+X2^3
#    3 |  1   X1+X2+X3  ...
#
#    If X = ( 1, 2, 3, 4, 5, ... ) then
#
#    N\R  0     1     2     3     4 ...
#      +--------------------------------------------------------
#    0 |  1     0     0     0     0
#    1 |  1     1     1     1     1
#    2 |  1     3     7    15    31
#    3 |  1     6    25    90   301
#    4 |  1    10    65   350  1701
#    5 |  1    15   140  1050  6951
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of variables.
#    0 <= N.
#
#    Input, integer R, the degree of the polynomial.
#    0 <= R.
#
#    Input, real X(N), the value of the variables.
#
#    Output, real VALUE, the value of TAU(N,R)(X).
#
  import numpy as np
  from sys import exit

  if ( n < 0 ):
    print ''
    print 'COMPLETE_SYMMETRIC_POLY - Fatal error!'
    print '  N < 0.'
    exit ( 'COMPLETE_SYMMETRIC_POLY - Fatal error!' )

  if ( r < 0 ):
    print ''
    print 'COMPLETE_SYMMETRIC_POLY - Fatal error!'
    print '  R < 0.'
    exit ( 'COMPLETE_SYMMETRIC_POLY - Fatal error!' )

  tau_length = max ( n, r ) + 1
  tau = np.zeros ( tau_length )

  tau[0] = 1.0
  for nn in range ( 0, n ):
    for rr in range ( 1, r + 1 ):
      tau[rr] = tau[rr] + x[nn] * tau[rr-1]

  value = tau[r]

  return value

def complete_symmetric_poly_test ( ):

#*****************************************************************************80
#
## COMPLETE_SYMMETRIC_POLY_TEST tests COMPLETE_SYMMETRIC_POLY.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    27 January 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  from r8vec_print import r8vec_print

  print ''
  print 'COMPLETE_SYMMETRIC_POLY_TEST'
  print '  COMPLETE_SYMMETRIC_POLY evaluates a complete symmetric'
  print '  polynomial in a given set of variables X.'
 
  n = 5
  x = np.array ( [ 1.0, 2.0, 3.0, 4.0, 5.0 ] )
  r8vec_print ( n, x, '  Variable vector X:' )

  print ''
  print '   N\\R     0       1       2       3       4       5'
  print ''

  for nn in range ( 0, n + 1 ):
    print '  %2d' % ( nn ),
    for rr in range ( 0, 6 ):
      value = complete_symmetric_poly ( nn, rr, x )
      print '  %6d' % ( value ),
    print ''

  print ''
  print 'COMPLETE_SYMMETRIC_POLY_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  complete_symmetric_poly_test ( )
  timestamp ( )
