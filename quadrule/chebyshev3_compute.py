#! /usr/bin/env python
#
def chebyshev3_compute ( n ):

#*****************************************************************************80
#
## CHEBYSHEV3_COMPUTE computes a closed Gauss-Chebyshev (first kind) quadrature.
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
#    If N points are used, then Gauss-Chebyshev quadrature
#    will compute the integral exactly, whenever F(X) is a polynomial
#    of degree 2*N-3 or less.
#
#    The abscissas include -1 and 1.
#
#    If the order is doubled, the abscissas of the new rule include
#    all the points of the old rule.  This fact can be used to
#    efficiently implement error estimation.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    17 April 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Daniel Zwillinger, editor,
#    Standard Mathematical Tables and Formulae,
#    30th Edition,
#    CRC Press, 1996.
#
#  Parameters:
#
#    Input, integer N, the order.
#    2 <= N.
#
#    Output, real X(N), the abscissas.
#
#    Output, real W(N), the weights.
#
  import numpy as np

  x = np.zeros ( n )
  w = np.zeros ( n )

  if ( n == 1 ):

    x[0] = 0.0
    w[0] = np.pi

  else:

    for i in range ( 0, n ):
      angle = float ( i ) * np.pi / float ( n - 1 )
      x[i] = np.cos ( angle )

    for i in range ( 0, n ):
      w[i] = np.pi / float ( n - 1 )

    w[0]   = 0.5 * w[0]
    w[n-1] = 0.5 * w[n-1]

  return x, w

def chebyshev3_compute_test ( ):

#*****************************************************************************80
#
## CHEBYSHEV3_COMPUTE_TEST tests CHEBYSHEV3_COMPUTE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    17 April 2015
#
#  Author:
#
#    John Burkardt
#
  print ''
  print 'CHEBYSHEV3_COMPUTE_TEST'
  print '  CHEBYSHEV3_COMPUTE computes'
  print '  a Chebyshev Type 3 quadrature rule over [-1,1].'

  print ''
  print '     Index       X                       W'
  print ''

  for n in range ( 1, 11 ):

    [ x, w ] = chebyshev3_compute ( n )

    print ''

    for i in range ( 0, n ):
      print '  %2d  %24.16g  %24.16g' % ( i, x[i], w[i] )
#
#  Terminate.
#
  print ''
  print 'CHEBYSHEV3_COMPUTE_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  chebyshev3_compute_test ( )
  timestamp ( )
