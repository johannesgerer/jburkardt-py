#! /usr/bin/env python
#
def hartley ( n ):

#*****************************************************************************80
#
## HARTLEY returns the HARTLEY matrix.
#
#  Formula:
#
#    A(I,J) = SIN ( 2*PI*(i-1)*(j-1)/N ) + COS( 2*PI*(i-1)*(j-1)/N )
#
#  Example:
#
#    N = 5
#
#    1.0000    1.0000    1.0000    1.0000    1.0000
#    1.0000    1.2601   -0.2212   -1.3968   -0.6420
#    1.0000   -0.2212   -0.6420    1.2601   -1.3968
#    1.0000   -1.3968    1.2601   -0.6420   -0.2212
#    1.0000   -0.6420   -1.3968   -0.2212    1.2601
#
#  Properties:
#
#    A is symmetric: A' = A.
#
#    Because A is symmetric, it is normal.
#
#    Because A is normal, it is diagonalizable.
#
#    A arises in the Hartley transform.
#
#    A * A = N * I, in other words, A is "almost" involutional,
#    and inverse ( A ) = ( 1 / N ) * A.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    11 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    D Bini, P Favati,
#    On a matrix algebra related to the discrete Hartley transform,
#    SIAM Journal on Matrix Analysis and Applications,
#    Volume 14, 1993, pages 500-507.
#
#  Parameters:
#
#    Input, integer N, the order of A.
#
#    Output, real A(N,N), the matrix.
#
  import numpy as np

  a = np.zeros ( ( n, n ) )

  for i in range ( 0, n ):
    for j in range ( 0, n ):

      angle = 2.0 * np.pi * float ( i * j ) / float ( n )

      a[i,j] = np.sin ( angle ) + np.cos ( angle )

  return a

def hartley_condition ( n ):

#*****************************************************************************80
#
## HARTLEY_CONDITION computes the L1 condition of the HARTLEY matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    05 April 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the order of the matrix.
#
#    Output, real VALUE, the L1 condition.
#
  a_norm = ( float ) ( n )
  b_norm = 1.0
  value = a_norm * b_norm

  return value

def hartley_determinant ( n ):

#*****************************************************************************80
#
## HARTLEY_DETERMINANT computes the determinant of the HARTLEY matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    11 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the order of the matrix.
#
#    Output, real DETERM, the determinant.
#
  from math import sqrt

  if ( ( n % 2 ) == 1 ):
    determ = sqrt ( float ( n ** n ) )
  else:
    determ = - sqrt ( float ( n ** n ) )

  return determ

def hartley_determinant_test ( ):

#*****************************************************************************80
#
## HARTLEY_DETERMINANT_TEST tests HARTLEY_DETERMINANT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    11 February 2015
#
#  Author:
#
#    John Burkardt
#
  from hartley import hartley
  from r8mat_print import r8mat_print

  print ''
  print 'HARTLEY_DETERMINANT_TEST'
  print '  HARTLEY_DETERMINANT computes the HARTLEY determinant.'

  m = 5
  n = m
 
  a = hartley ( n )

  r8mat_print ( m, n, a, '  HARTLEY matrix:' )

  value = hartley_determinant ( n )

  print '  Value =  %g' % ( d )

  print ''
  print 'HARTLEY_DETERMINANT_TEST'
  print '  Normal end of execution.'

  return

def hartley_inverse ( n ):

#*****************************************************************************80
#
## HARTLEY_INVERSE returns the inverse of the HARTLEY matrix.
#
#  Formula:
#
#    A(I,J) = (1/N) * SIN ( 2*PI*(i-1)*(j-1)/N ) + COS( 2*PI*(i-1)*(j-1)/N )
#
#  Properties:
#
#    A is symmetric: A' = A.
#
#    Because A is symmetric, it is normal.
#
#    Because A is normal, it is diagonalizable.
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
#    D Bini, P Favati,
#    On a matrix algebra related to the discrete Hartley transform,
#    SIAM Journal on Matrix Analysis and Applications,
#    Volume 14, 1993, pages 500-507.
#
#  Parameters:
#
#    Input, integer N, the order of A.
#
#    Output, real A(N,N), the matrix.
#
  import numpy as np

  a = np.zeros ( ( n, n ) )

  for i in range ( 0, n ):
    for j in range ( 0, n ):

      angle = 2.0 * np.pi * float ( i * j ) / float ( n )

      a[i,j] = ( np.sin ( angle ) + np.cos ( angle ) ) / float ( n )

  return a

def hartley_test ( ):

#*****************************************************************************80
#
## HARTLEY_TEST tests HARTLEY.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    11 February 2015
#
#  Author:
#
#    John Burkardt
#
  from r8mat_print import r8mat_print

  print ''
  print 'HARTLEY_TEST'
  print '  HARTLEY computes the HARTLEY matrix.'

  m = 5
  n = m

  a = hartley ( n )
 
  r8mat_print ( m, n, a, '  HARTLEY matrix:' )

  print ''
  print 'HARTLEY_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  hartley_test ( )
  timestamp ( )
