#! /usr/bin/env python
#
def zero ( m, n ):

#*****************************************************************************80
#
## ZERO returns the ZERO matrix.
#
#  Formula:
#
#    A(I,J) = 0
#
#  Example:
#
#    M = 4, N = 5
#
#    0 0 0 0 0
#    0 0 0 0 0
#    0 0 0 0 0
#    0 0 0 0 0
#
#  Properties:
#
#    A is integral.
#
#    A is Toeplitz: constant along diagonals.
#
#    A is a Hankel matrix: constant along anti-diagonals.
#
#    A is a circulant matrix: each row is shifted once to get the next row.
#
#    A is an anticirculant matrix.
#
#    A is singular.
#
#    A is symmetric: A' = A.
#
#    Because A is symmetric, it is normal.
#
#    Because A is normal, it is diagonalizable.
#
#    LAMBDA(1:N) = 0.
#
#    The matrix of eigenvectors of A is I.
#
#    det ( A ) = 0.
#
#    For any vector v, A*v = 0.
#
#    For any matrix B, A*B = B*A = 0.
#
#    A is persymmetric: A(I,J) = A(N+1-J,N+1-I).
#
#    The family of matrices is nested as a function of N.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 February 2015
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

  return a

def zero_determinant ( n ):

#*****************************************************************************80
#
## ZERO_DETERMINANT returns the determinant of the ZERO matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 February 2015
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
  value = 0.0

  return value

def zero_determinant_test ( ):

#*****************************************************************************80
#
## ZERO_DETERMINANT_TEST tests ZERO_DETERMINANT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 March 2015
#
#  Author:
#
#    John Burkardt
#
  from zero import zero
  from r8mat_print import r8mat_print

  print ''
  print 'ZERO_DETERMINANT_TEST'
  print '  ZERO_DETERMINANT computes the determinant of the ZERO matrix.'
  print ''

  m = 4
  n = m

  a = zero ( m, n )
  r8mat_print ( m, n, a, '  ZERO matrix:' )

  value = zero_determinant ( n )

  print ''
  print '  Value =  %g' % ( value )

  print ''
  print 'ZERO_DETERMINANT_TEST'
  print '  Normal end of execution.'

  return

def zero_eigen_right ( n ):

#*****************************************************************************80
#
## ZERO_EIGEN_RIGHT returns the right eigenvectors of the ZERO matrix.
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

def zero_eigenvalues ( n ):

#*****************************************************************************80
#
## ZERO_EIGENVALUES returns the eigenvalues of the ZERO matrix.
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
#    Output, real LAM(N), the eigenvalues.
#
  import numpy as np

  lam = np.zeros ( n )

  return lam

def zero_null_left ( m, n ):

#*****************************************************************************80
#
## ZERO_NULL_LEFT returns a left null vector of the ZERO matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    07 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, N, the order of the matrix.
#
#    Output, real X(M), the left null vector.
#
  import numpy as np

  x = np.ones ( m )

  return x

def zero_null_right ( m, n ):

#*****************************************************************************80
#
## ZERO_NULL_RIGHT returns a right null vector of the ZERO matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    12 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, N, the order of the matrix.
#
#    Output, real X(N), the right null vector.
#
  import numpy as np

  x = np.ones ( n )

  return x

def zero_test ( ):

#*****************************************************************************80
#
## ZERO_TEST tests ZERO.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 February 2015
#
#  Author:
#
#    John Burkardt
#
  from r8mat_print import r8mat_print

  print ''
  print 'ZERO_TEST'
  print '  ZERO computes the ZERO matrix.'

  m = 4
  n = m

  a = zero ( m, n )
  r8mat_print ( m, n, a, '  ZERO matrix:' )

  print ''
  print 'ZERO_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  zero_test ( )
  zero_determinant_test ( )
  timestamp ( )
