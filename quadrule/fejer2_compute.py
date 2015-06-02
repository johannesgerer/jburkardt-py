#! /usr/bin/env python
#
def fejer2_compute ( n ):

#*****************************************************************************80
#
## FEJER2_COMPUTE computes a Fejer type 2 quadrature rule.
#
#  Discussion:
#
#    This method uses a direct approach.  The paper by Waldvogel
#    exhibits a more efficient approach using Fourier transforms.
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
#  Reference:
#
#    Philip Davis, Philip Rabinowitz,
#    Methods of Numerical Integration,
#    Second Edition,
#    Dover, 2007,
#    ISBN: 0486453391,
#    LC: QA299.3.D28.
#
#    Walter Gautschi,
#    Numerical Quadrature in the Presence of a Singularity,
#    SIAM Journal on Numerical Analysis,
#    Volume 4, Number 3, 1967, pages 357-362.
#
#    Joerg Waldvogel,
#    Fast Construction of the Fejer and Clenshaw-Curtis Quadrature Rules,
#    BIT Numerical Mathematics,
#    Volume 43, Number 1, 2003, pages 1-18.
#
#  Parameters:
#
#    Input, integer N, the order.
#
#    Output, real X(N), the abscissas.
#
#    Output, real W(N), the weights.
#
  import numpy as np

  if ( n == 1 ):

    x = np.array ( [ 0.0 ] )
    w = np.array ( [ 2.0 ] )

  elif ( n == 2 ):

    x = np.array ( [ -0.5, +0.5 ] )
    w = np.array ( [  1.0,  1.0 ] )

  else:

    theta = np.zeros ( n )

    for i in range ( 0, n ):
      theta[i] = float ( n - i ) * np.pi / float ( n + 1 )

    x = np.zeros ( n )
    for i in range ( 0, n ):
      x[i] = np.cos ( theta[i] )

    w = np.zeros ( n )

    for i in range ( 0, n ):

      w[i] = 1.0
      jhi = ( ( n - 1 ) // 2 )
      for j in range ( 0, jhi ):
        angle = 2.0 * float ( j + 1 ) * theta[i]
        w[i] = w[i] - 2.0 * np.cos ( angle ) / float ( 4 * ( j + 1 ) ** 2 - 1 )
        p = 2 *  ( ( n + 1 ) // 2 ) - 1

      w[i] = w[i] - np.cos ( float ( p + 1 ) * theta[i] ) / float ( p )

    for i in range ( 0, n ):
      w[i] = 2.0 * w[i] / float ( n + 1 )

  return x, w

def fejer2_compute_test ( ):

#*****************************************************************************80
#
## FEJER2_COMPUTE_TEST tests FEJER2_COMPUTE.
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
  print 'FEJER2_COMPUTE_TEST'
  print '  FEJER2_COMPUTE computes the abscissas and weights'
  print '  of a Fejer type 2 quadrature rule.'
  print ''
  print '    Order  W             X'
  print ''

  for n in range ( 1, 11 ):

    x, w = fejer2_compute ( n )

    print ''
    print '  %8d' % ( n )

    for i in range ( 0, n ):
      print '            %12g  %12g' % ( w[i], x[i] )
#
#  Terminate.
#
  print ''
  print 'FEJER2_COMPUTE_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  fejer2_compute_test ( )
  timestamp ( )
