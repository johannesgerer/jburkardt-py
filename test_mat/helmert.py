#! /usr/bin/env python
#
def helmert ( n ):

#*****************************************************************************80
#
## HELMERT returns the HELMERT matrix.
#
#  Formula:
#
#    If I = 1 then
#      A(I,J) = 1 / sqrt ( N )
#    else if J < I then
#      A(I,J) = 1 / sqrt ( I * ( I - 1 ) )
#    else if J = I then
#      A(I,J) = (1-I) / sqrt ( I * ( I - 1 ) )
#    else
#      A(I,J) = 0
#
#  Discussion:
#
#    The matrix given above by Helmert is the classic example of
#    a family of matrices which are now called Helmertian or
#    Helmert matrices.
#
#    A matrix is a (standard) Helmert matrix if it is orthogonal,
#    and the elements which are above the diagonal and below the
#    first row are zero.
#
#    If the elements of the first row are all strictly positive,
#    then the matrix is a strictly Helmertian matrix.
#
#    It is possible to require in addition that all elements below
#    the diagonal be strictly positive, but in the reference, this
#    condition is discarded as being cumbersome and not useful.
#
#    A Helmert matrix can be regarded as a change of basis matrix
#    between a pair of orthonormal coordinate bases.  The first row
#    gives the coordinates of the first new basis vector in the old
#    basis.  Each later row describes combinations of (an increasingly
#    extensive set of) old basis vectors that constitute the new
#    basis vectors.
#
#    Helmert matrices have important applications in statistics.
#
#  Example:
#
#    N = 5
#
#    0.4472    0.4472    0.4472    0.4472    0.4472
#    0.7071   -0.7071         0         0         0
#    0.4082    0.4082   -0.8165         0         0
#    0.2887    0.2887    0.2887   -0.8660         0
#    0.2236    0.2236    0.2236    0.2236   -0.8944
#
#  Properties:
#
#    A is generally not symmetric: A' ~= A.
#
#    A is orthogonal: A' * A = A * A' = I.
#
#    Because A is orthogonal, it is normal: A' * A = A * A'.
#
#    A is not symmetric: A' ~= A.
#
#    det ( A ) = (-1)^(N+1)
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
#    HO Lancaster,
#    The Helmert Matrices,
#    American Mathematical Monthly,
#    Volume 72, 1965, pages 4-12.
#
#  Parameters:
#
#    Input, integer N, the order of A.
#
#    Output, real A(N,N), the matrix.
#
  import numpy as np

  a = np.zeros ( ( n, n ) )
#
#  A begins with the first row, diagonal, and lower triangle set to 1.
#
  for i in range ( 0, n ):
    for j in range ( 0, n ):

      if ( i == 0 ):
        a[i,j] = 1.0 / np.sqrt ( n )
      elif ( j < i ):
        a[i,j] = 1.0 / np.sqrt ( float ( i * ( i + 1 ) ) )
      elif ( i == j ):
        a[i,j] = float ( - i ) / np.sqrt ( float ( i * ( i + 1 ) ) )

  return a

def helmert_determinant ( n ):

#*****************************************************************************80
#
## HELMERT_DETERMINANT computes the determinant of the HELMERT matrix.
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
  if ( ( n % 2 ) == 0 ):
    determ = - 1.0
  else:
    determ = 1.0

  return determ

def helmert_determinant_test ( ):

#*****************************************************************************80
#
## HELMERT_DETERMINANT_TEST tests HELMERT_DETERMINANT.
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
  from helmert import helmert
  from r8mat_print import r8mat_print

  print ''
  print 'HELMERT_DETERMINANT_TEST'
  print '  HELMERT_DETERMINANT computes the HELMERT determinant.'

  m = 5
  n = m
 
  a = helmert ( n )

  r8mat_print ( m, n, a, '  HELMERT matrix:' )

  value = helmert_determinant ( n )

  print ''
  print '  Value =  %g' % ( value )

  print ''
  print 'HELMERT_DETERMINANT_TEST'
  print '  Normal end of execution.'

  return

def helmert_inverse ( n ):

#*****************************************************************************80
#
## HELMERT_INVERSE returns the inverse of the HELMERT matrix.
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
#    Output, real A(N,N), the inverse matrix.
#
  import numpy as np

  a = helmert ( n )

  a = np.transpose ( a )

  return a

def helmert_test ( ):

#*****************************************************************************80
#
## HELMERT_TEST tests HELMERT.
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
  print 'HELMERT_TEST'
  print '  HELMERT computes the HELMERT matrix.'

  m = 5
  n = m

  a = helmert ( n )
 
  r8mat_print ( m, n, a, '  HELMERT matrix:' )

  print ''
  print 'HELMERT_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  helmert_test ( )
  timestamp ( )
