#! /usr/bin/env python
#
def chebyshev1_compute ( n ):

#*****************************************************************************80
#
## CHEBYSHEV1_COMPUTE computes a Gauss-Chebyshev type 1 quadrature rule.
#
#  Discussion:
#
#    The integral:
#
#      Integral ( -1 <= X <= 1 ) F(X) / sqrt ( 1 - x^2 ) dX
#
#    The quadrature rule:
#
#      Sum ( 1 <= I <= N ) W(I) * F ( X(I) )
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 February 2010
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Philip Davis, Philip Rabinowitz,
#    Methods of Numerical Integration,
#    Second Edition,
#    Dover, 2007,
#    ISBN: 0486453391,
#    LC: QA299.3.D28.
#
#  Parameters:
#
#    Input, integer N, the order.
#    N must be greater than 0.
#
#    Output, real X(N), the abscissas.
#
#    Output, real W(N), the weights.
#
  import numpy as np

  x = np.zeros ( n )
  w = np.zeros ( n )

  for i in range ( 0, n ):
    w[i] = np.pi / float ( n )

  for i in range ( 0, n ):
    x[i] = np.cos ( np.pi * float ( 2 * n - 1 - 2 * i ) / float ( 2 * n ) )

  return x, w

def chebyshev1_compute_test ( ):

#*****************************************************************************80
#
## CHEBYSHEV1_COMPUTE_TEST tests CHEBYSHEV1_COMPUTE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    15 April 2015
#
#  Author:
#
#    John Burkardt
#
  print ''
  print 'CHEBYSHEV1_COMPUTE_TEST'
  print '  CHEBYSHEV1_COMPUTE computes'
  print '  a Chebyshev Type 1 quadrature rule over [-1,1].'

  print ''
  print '     Index       X                       W'
  print ''

  for n in range ( 1, 11 ):

    [ x, w ] = chebyshev1_compute ( n )

    print ''

    for i in range ( 0, n ):
      print '  %2d  %24.16g  %24.16g' % ( i, x[i], w[i] )
#
#  Terminate.
#
  print ''
  print 'CHEBYSHEV1_COMPUTE_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  chebyshev1_compute_test ( )
  timestamp ( )
