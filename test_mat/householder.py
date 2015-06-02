#! /usr/bin/env python
#
def householder ( n, x ):

#*****************************************************************************80
#
## HOUSEHOLDER constructs a HOUSEHOLDER matrix.
#
#  Discussion:
#
#    A Householder matrix is also called an elementary reflector.
#
#  Formula:
#
#     A = I - ( 2 * X * X' ) / ( X' * X )
#
#  Example:
#
#    N = 5, X = ( 1, 1, 1, 0, -1 )
#
#   1/2 -1/2 -1/2  0  1/2
#  -1/2  1/2 -1/2  0  1/2
#  -1/2 -1/2  1/2  0  1/2
#    0    0    0   1   0
#   1/2  1/2  1/2  0  1/2
#
#  Properties:
#
#    A is symmetric: A' = A.
#
#    Because A is symmetric, it is normal.
#
#    Because A is normal, it is diagonalizable.
#
#    A is orthogonal: A' * A = A * A' = I.
#
#    inverse ( A ) = A.
#
#    det ( A ) = -1.
#
#    A is unimodular.
#
#    If Y and Z are nonzero vectors of equal length, and
#      X = ( Y - Z ) / NORM(Y-Z),
#    then
#      A * Y = Z.
#
#    A represents a reflection through the plane which
#    is perpendicular to the vector X.  In particular, A*X = -X.
#
#    LAMBDA(1) = -1;
#    LAMBDA(2:N) = +1.
#
#    If X is the vector used to define H, then X is the eigenvector
#    associated with the eigenvalue -1.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Gene Golub, Charles Van Loan,
#    Matrix Computations, second edition,
#    Johns Hopkins University Press, Baltimore, Maryland, 1989.
#
#    Pete Stewart,
#    Introduction to Matrix Computations,
#    Academic Press, 1973,
#
#    James Wilkinson,
#    The Algebraic Eigenvalue Problem,
#    Oxford University Press, 1965.
#
#  Parameters:
#
#    Input, integer N, the order of A.
#
#    Input, real X(N), the vector that defines the 
#    Householder matrix.
#
#    Output, real A(N,N), the matrix.
#
  import numpy as np

  a = np.zeros ( ( n, n ) )

  for i in range ( 0, n ):
    a[i,i] = 1.0

  xdot = 0.0
  for i in range ( 0, n ):
    xdot = xdot + x[i] * x[i]

  if ( 0.0 < xdot ):

    for i in range ( 0, n ):
      for j in range ( 0, n ):
        a[i,j] = a[i,j] - 2.0 * x[i] * x[j] / xdot

  return a

def householder_determinant ( n, x ):

#*****************************************************************************80
#
## HOUSEHOLDER_DETERMINANT computes the determinant of the HOUSEHOLDER matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the order of the matrix.
#
#    Input, real X(N), the vector.
#
#    Output, real VALUE, the determinant.
#
  value = -1.0
 
  return value

def householder_determinant_test ( ):

#*****************************************************************************80
#
## HOUSEHOLDER_DETERMINANT_TEST tests HOUSEHOLDER_DETERMINANT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 February 2015
#
#  Author:
#
#    John Burkardt
#
  from householder import householder
  from r8vec_uniform_ab import r8vec_uniform_ab
  from r8mat_print import r8mat_print

  print ''
  print 'HOUSEHOLDER_DETERMINANT_TEST'
  print '  HOUSEHOLDER_DETERMINANT computes the HOUSEHOLDER determinant.'

  n = 5
  r8_lo = -5.0
  r8_hi = +5.0
  seed = 123456789
  x, seed = r8vec_uniform_ab ( n, r8_lo, r8_hi, seed )

  a = householder ( n, x )
  m = n
  r8mat_print ( m, n, a, '  HOUSEHOLDER matrix:' )

  value = householder_determinant ( n, x )

  print ''
  print '  Value =  %g' % ( value )

  print ''
  print 'HOUSEHOLDER_DETERMINANT_TEST'
  print '  Normal end of execution.'

  return

def householder_inverse ( n, x ):

#*****************************************************************************80
#
## HOUSEHOLDER_INVERSE returns the inverse of a HOUSEHOLDER matrix.
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
#    Input, real X(N), the vector that defines the 
#    Householder matrix.
#
#    Output, real A(N,N), the eigenvalues.
#
  a = householder ( n, x )

  return a

def householder_test ( ):

#*****************************************************************************80
#
## HOUSEHOLDER_TEST tests HOUSEHOLDER.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 February 2015
#
#  Author:
#
#    John Burkardt
#
  from r8vec_uniform_ab import r8vec_uniform_ab
  from r8mat_print import r8mat_print

  print ''
  print 'HOUSEHOLDER_TEST'
  print '  HOUSEHOLDER computes the HOUSEHOLDER matrix.'

  n = 5
  r8_lo = -5.0
  r8_hi = +5.0
  seed = 123456789
  x, seed = r8vec_uniform_ab ( n, r8_lo, r8_hi, seed )

  a = householder ( n, x )
  m = n
  r8mat_print ( m, n, a, '  HOUSEHOLDER matrix:' )

  print ''
  print 'HOUSEHOLDER_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  householder_test ( )
  timestamp ( )
