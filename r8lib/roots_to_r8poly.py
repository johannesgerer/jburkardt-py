#!/usr/bin/env python
#
def roots_to_r8poly ( n, x ):

#*****************************************************************************80
#
## ROOTS_TO_R8POLY converts polynomial roots to polynomial coefficients.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    16 April 2005
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of roots specified.
#
#    Input, real X(N), the roots.
#
#    Output, real C(1:N+1), the coefficients of the polynomial.
#
  import numpy as np
#
#  Initialize C to (0, 0, ..., 0, 1).
#  Essentially, we are setting up a divided difference table.
#
  c = np.zeros ( n + 1 )
  c[n] = 1.0
#
#  Convert to standard polynomial form by shifting the abscissas
#  of the divided difference table to 0.
#
  for j in range ( 1, n + 1 ):
    for i in range ( 1, n + 2 - j ):
      c[n-i] = c[n-i] - x[n+1-i-j] * c[n-i+1]

  return c

def roots_to_r8poly_test ( ):

#*****************************************************************************80
#
## ROOTS_TO_R8POLY_TEST tests ROOTS_TO_R8POLY.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    11 March 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  from r8poly_print import r8poly_print
  from r8vec_print import r8vec_print

  n = 5

  x = np.array ( [ \
   [  1.0 ], \
   [ -4.0 ], \
   [  3.0 ], \
   [  0.0 ], \
   [  3.0 ] ] );

  print ''
  print 'ROOTS_TO_R8POLY_TEST'
  print '  ROOTS_TO_R8POLY is given N real roots,'
  print '  and constructs the coefficient vector'
  print '  of the corresponding polynomial.'

  r8vec_print ( n, x, '  N real roots:' )

  c = roots_to_r8poly ( n, x )

  r8poly_print ( n, c, '  The polynomial:' )

  print ''
  print 'ROOTS_TO_R8POLY_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  roots_to_r8poly_test ( )
  timestamp ( )
