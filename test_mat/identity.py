#! /usr/bin/env python
#
def identity ( m, n ):

#*****************************************************************************80
#
## IDENTITY returns the IDENTITY matrix.
#
#  Formula:
#
#    if ( I = J )
#      A(I,J) = 1
#    else
#      A(I,J) = 0
#
#  Example:
#
#    M = 4, N = 5
#
#    1 0 0 0 0
#    0 1 0 0 0
#    0 0 1 0 0
#    0 0 0 1 0
#
#  Rectangular properties:
#
#    A is integral: int ( A ) = A.
#
#    A is a zero/one matrix.
#
#  Square Properties:
#
#    A is nonsingular.
#
#    A is involutional: A * A = I.
#
#    A is diagonal.
#
#    Because A is diagonal, it has property A.
#
#    A is symmetric: A' = A.
#
#    A is a circulant matrix: each row is shifted once to get the next row.
#
#    Because A is symmetric, it is normal.
#
#    Because A is normal, it is diagonalizable.
#
#    LAMBDA(1:N) = 1
#
#    The matrix of eigenvectors of A is A.
#
#    det ( A ) = 1.
#
#    A is unimodular.
#
#    For any vector v, A*v = v.
#
#    For any matrix B, A*B = B*A=B.
#
#    A is persymmetric: A(I,J) = A(N+1-J,N+1-I).
#
#    A is centrosymmetric: A(I,J) = A(N+1-I,N+1-J).
#
#    The family of matrices is nested as a function of N.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    14 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, N, the number of rows and columns of 
#    the matrix.
#
#    Output, real A(M,N), the matrix.
#
  import numpy as np

  a = np.zeros ( [ m, n ] )

  for i in range ( 0, m ):
    for j in range ( 0, n ):
      if ( i == j ):
        a[i,j] = 1.0

  return a

def identity_condition ( n ):

#*****************************************************************************80
#
## IDENTITY_CONDITION returns the L1 condition of the IDENTITY matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 February 2015
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
  a_norm = 1;
  b_norm = 1;
  value = a_norm * b_norm;

  return value

def identity_condition_test ( ):

#*****************************************************************************80
#
## IDENTITY_CONDITION_TEST tests IDENTITY_CONDITION.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 February 2015
#
#  Author:
#
#    John Burkardt
#
  from identity import identity
  from r8mat_print import r8mat_print
 
  print ''
  print 'IDENTITY_CONDITION_TEST'
  print '  IDENTITY_CONDITION computes the condition of the IDENTITY matrix.'
  print ''

  m = 4
  n = m

  a = identity ( m, n )
  r8mat_print ( m, n, a, '  IDENTITY matrix:' )

  value = identity_condition ( n )

  print ''
  print '  Value =  %g' % ( value )

  print ''
  print 'IDENTITY_CONDITION_TEST'
  print '  Normal end of execution.'

  return

def identity_determinant ( n ):

#*****************************************************************************80
#
## IDENTITY_DETERMINANT returns the determinant of the IDENTITY matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    14 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the order of the matrix.
#
#    Output, real VALUE, the determinant.
#
  value = 1.0

  return value

def identity_determinant_test ( ):

#*****************************************************************************80
#
## IDENTITY_DETERMINANT_TEST tests IDENTITY_DETERMINANT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    14 February 2015
#
#  Author:
#
#    John Burkardt
#
  from identity import identity
  from r8mat_print import r8mat_print
 
  print ''
  print 'IDENTITY_DETERMINANT_TEST'
  print '  IDENTITY_DETERMINANT computes the determinant of the IDENTITY matrix.'
  print ''

  m = 4
  n = m

  a = identity ( m, n )
  r8mat_print ( m, n, a, '  IDENTITY matrix:' )

  value = identity_determinant ( n )

  print ''
  print '  Value =  %g' % ( value )

  print ''
  print 'IDENTITY_DETERMINANT_TEST'
  print '  Normal end of execution.'

  return

def identity_eigen_right ( n ):

#*****************************************************************************80
#
## IDENTITY_EIGEN_RIGHT returns the right eigenvectors of the IDENTITY matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    16 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the order of the matrix.
#
#    Output, real A(N,N), the matrix.
#
  import numpy as np

  a = np.zeros ( ( n, n ) )

  for i in range ( 0, n ):
    a[i,i] = 1.0

  return a

def identity_eigenvalues ( n ):

#*****************************************************************************80
#
## IDENTITY_EIGENVALUES returns the eigenvalues of the IDENTITY matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    16 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the order of A.
#
#    Output, real LAM(N), the eigenvalues.
#
  import numpy as np

  lam = np.ones ( n )

  return lam

def identity_inverse ( n ):

#*****************************************************************************80
#
## IDENTITY_INVERSE returns the inverse of the IDENTITY matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    17 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the order of the matrix.
#
#    Output, real A(N,N), the matrix.
#
  import numpy as np

  a = np.zeros ( [ n, n ] )

  for i in range ( 0, n ):
    for j in range ( 0, n ):
      if ( i == j ):
        a[i,j] = 1.0

  return a

def identity_test ( ):

#*****************************************************************************80
#
## IDENTITY_TEST tests IDENTITY.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    14 February 2015
#
#  Author:
#
#    John Burkardt
#
  from r8mat_print import r8mat_print

  print ''
  print 'IDENTITY_TEST'
  print '  IDENTITY computes the IDENTITY matrix.'

  m = 4
  n = m

  a = identity ( m, n )
  r8mat_print ( m, n, a, '  IDENTITY matrix:' )

  print ''
  print 'IDENTITY_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  identity_test ( )
  timestamp ( )
