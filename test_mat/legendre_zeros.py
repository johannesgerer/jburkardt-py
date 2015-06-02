#! /usr/bin/env python
#
def legendre_zeros ( n ):

#*****************************************************************************80
#
## LEGENDRE_ZEROS computes the zeros of the Legendre polynomial.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    16 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the degree of the polynomial.
#
#    Output, real X(N), the zeros of the polynomial.
#
  import numpy as np

  x = np.zeros ( n );

  e1 = float ( n * ( n + 1 ) )

  m = ( n + 1 ) // 2

  for i in range ( 1, m + 1 ):

    t = float ( 4 * i - 1 ) * np.pi / float ( 4 * n + 2 )
    x0 = np.cos ( t ) * ( 1.0 - ( 1.0 - 1.0 / float ( n ) ) / float ( 8 * n * n ) )

    pkm1 = 1.0
    pk = x0

    for k in range ( 2, n + 1 ):
      pkp1 = 2.0 * x0 * pk - pkm1 - ( x0 * pk - pkm1 ) / float ( k )
      pkm1 = pk
      pk = pkp1

    d1 = float ( n ) * ( pkm1 - x0 * pk )

    dpn = d1 / ( 1.0 - x0 * x0 )

    d2pn = ( 2.0 * x0 * dpn - e1 * pk ) / ( 1.0 - x0 * x0 )

    d3pn = ( 4.0 * x0 * d2pn + ( 2.0 - e1 ) * dpn ) / ( 1.0 - x0 * x0 )

    d4pn = ( 6.0 * x0 * d3pn + ( 6.0 - e1 ) * d2pn ) / ( 1.0 - x0 * x0 )

    u = pk / dpn
    v = d2pn / dpn
#
#  Initial approximation H:
#
    h = - u * ( 1.0 + 0.5 * u * ( v + u * ( v * v - d3pn / ( 3.0 * dpn ) ) ) )
#
#  Refine H using one step of Newton's method:
#
    p = pk + h * ( dpn + 0.5 * h * ( d2pn + h / 3.0 \
      * ( d3pn + 0.25 * h * d4pn ) ) )

    dp = dpn + h * ( d2pn + 0.5 * h * ( d3pn + h * d4pn / 3.0 ) )

    h = h - p / dp

    xtemp = x0 + h

    x[n-i] =   xtemp
    x[i-1] = - xtemp

    fx = d1 - h * e1 * ( pk + 0.5 * h * ( dpn + h / 3.0 \
      * ( d2pn + 0.25 * h * ( d3pn + 0.2 * h * d4pn ) ) ) )

  if ( ( n % 2 ) == 1 ):
    x[m-1] = 0.0;

  return x

def legendre_zeros_test ( ):

#*****************************************************************************80
#
## LEGENDRE_ZEROS_TEST tests LEGENDRE_ZEROS.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    16 February 2015
#
#  Author:
#
#    John Burkardt
#
  from r8vec_print import r8vec_print

  print ''
  print 'LEGENDRE_ZEROS_TEST'
  print '  LEGENDRE_ZEROS computes the zeros of the N-th Legendre polynomial.'

  for n in range ( 1, 8 ):
    l = legendre_zeros ( n )
    r8vec_print ( n, l, '  Legendre zeros:' )

  print ''
  print 'FRANK_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  legendre_zeros_test ( )
  timestamp ( )
