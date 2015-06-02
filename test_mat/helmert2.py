#! /usr/bin/env python
#
def helmert2 ( n, x ):

#*****************************************************************************80
#
## HELMERT2 returns the HELMERT2 matrix.
#
#  Formula:
#
#    Row 1 = the vector, divided by its L2 norm.
#
#    Row 2 is computed by the requirements that it be orthogonal to row 1,
#    be nonzero only from columns 1 to 2, and have a negative diagonal.
#
#    Row 3 is computed by the requirements that it be orthogonal to
#    rows 1 and 2, be nonzero only from columns 1 to 3, and have a
#    negative diagonal, and so on.
#
#  Properties:
#
#    The first row of A should be the vector X, divided by its L2 norm.
#
#    A is orthogonal: A' * A = A * A' = I.
#
#    A is not symmetric: A' ~= A.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    HO Lancaster,
#    The Helmert Matrices,
#    American Mathematical Monthly,
#    Volume 72, 1965, pages 4-12.
#
#  Parameters:
#
#    Input, integer N, the order of A.
#
#    Input, real X(N), the vector that defines the first row.
#    X must not have 0 L2 norm, and its first entry must not be 0.
#
#    Output, real A(N,N), the matrix.
#
  import numpy as np
  from r8vec_norm_l2 import r8vec_norm_l2
  from sys import exit

  a = np.zeros ( ( n, n ) )

  x_norm_l2 = r8vec_norm_l2 ( n, x )

  if ( x_norm_l2 == 0.0 ):
    print ''
    print 'HELMERT2 - Fatal error!'
    print '  Input vector has zero L2 norm.'
    exit ( 'HELMERT2 - Fatal error!' );

  if ( x[0] == 0.0 ):
    print ''
    print 'HELMERT2 - Fatal error!'
    print '  Input vector has X[0] = 0.'
    exit ( 'HELMERT2 - Fatal error!' );

  w = np.zeros ( n )
  for i in range ( 0, n ):
    w[i] = ( x[i] / x_norm_l2 ) ** 2

  s = np.zeros ( n )
  s[0] = w[0]
  for i in range ( 1, n ):
    s[i] = s[i-1] + w[i]

  for j in range ( 0, n ):
    a[0,j] = np.sqrt ( w[j] )

  for i in range ( 1, n ):
    for j in range ( 0, i ):
      a[i,j] = np.sqrt ( w[i] * w[j] / ( s[i] * s[i-1] ) )
    a[i,i] = - np.sqrt ( s[i-1] / s[i] )

  return a

def helmert2_inverse ( n, x ):

#*****************************************************************************80
#
#% HELMERT2_INVERSE returns the inverse of the HELMERT2 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the order of A.
#
#    Input, real X(N), the vector that defines the first row.
#
#    Output, real A(N,N), the inverse matrix.
#
  import numpy as np

  a = helmert2 ( n, x )

  a = np.transpose ( a )

  return a

def helmert2_test ( ):

#*****************************************************************************80
#
## HELMERT2_TEST tests HELMERT2.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 March 2015
#
#  Author:
#
#    John Burkardt
#
  from r8mat_print import r8mat_print
  from r8vec_uniform_ab import r8vec_uniform_ab

  print ''
  print 'HELMERT2_TEST'
  print '  HELMERT2 computes the HELMERT2 matrix.'

  m = 5
  n = m
  r8_lo = -5.0
  r8_hi = +5.0
  seed = 123456789
  x, seed = r8vec_uniform_ab ( n, r8_lo, r8_hi, seed )
  a = helmert2 ( n, x )
 
  r8mat_print ( m, n, a, '  HELMERT2 matrix:' )

  print ''
  print 'HELMERT2_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  helmert2_test ( )
  timestamp ( )
