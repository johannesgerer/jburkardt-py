#!/usr/bin/env python
#
def cheby_t_poly_zero ( n ):

#*****************************************************************************80
#
## CHEBY_T_POLY_ZERO returns zeroes of Chebyshev polynomials T(n,x).
#
#  Discussion:
#
#    The I-th zero of T(n,x) is cos((2*I-1)*PI/(2*N)), I = 1 to N
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    21 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the order of the polynomial.
#
#    Output, real Z(N), the zeroes of T(N)(X).
#
  import numpy as np

  z = np.zeros ( n )

  for i in range ( 0, n ):
    angle = ( 2 * i + 1 ) * np.pi / float ( 2 * n )
    z[i] = np.cos ( angle )

  return z

def cheby_t_poly_zero_test ( ):

#*****************************************************************************80
#
## CHEBY_T_POLY_ZERO_TEST tests CHEBY_T_POLY_ZERO.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    21 January 2015
#
#  Author:
#
#    John Burkardt
#
  from cheby_t_poly import cheby_t_poly

  n_max = 4

  print ''
  print 'CHEBY_T_POLY_ZERO_TEST:'
  print '  CHEBY_T_POLY_ZERO returns zeroes of T(N,X).'
  print ''
  print '         N         X        T(N,X)'
  print ''

  for n in range ( 1, n_max + 1 ):

    z = cheby_t_poly_zero ( n )

    fx = cheby_t_poly ( n, n, z )

    for i in range ( 0, n ):
      print '  %8d  %11g  %14g' % ( n, z[i], fx[i,n] )

    print ''

  print ''
  print 'CHEBY_T_POLY_ZERO_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  cheby_t_poly_zero_test ( )
  timestamp ( )
