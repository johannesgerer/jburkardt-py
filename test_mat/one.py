#! /usr/bin/env python
#
def one ( m, n ):

#*****************************************************************************80
#
## ONE returns the ONE matrix.
#
#  Discussion:
#
#    The matrix is sometimes symbolized by "J".
#
#  Example:
#
#    N = 5
#
#    1 1 1 1 1
#    1 1 1 1 1
#    1 1 1 1 1
#    1 1 1 1 1
#    1 1 1 1 1
#
#  Properties:
#
#    Every entry of A is 1.
#
#    A is symmetric.
#
#    A is Toeplitz: constant along diagonals.
#
#    A is Hankel: constant along antidiagonals.
#
#    A is a circulant matrix: each row is shifted once to get the next row.
#
#    A has constant row sums.
#
#    A has constant column sums.
#
#    If 1 < N, A is singular.
#
#    If 1 < N, det ( A ) = 0.
#
#    LAMBDA(1:N-1) = 0
#    LAMBDA(N) = N
#
#    The eigenvector associated with LAMBDA = N is ( 1, 1, ..., 1 ).
#
#    A * A = N * A
#
#    The family of matrices is nested as a function of N.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    20 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, N, the order of A.
#
#    Output, real A(M,N), the matrix.
#
  import numpy as np

  a = np.ones ( ( m, n ) )
 
  return a

def one_determinant ( n ):

#*****************************************************************************80
#
## ONE_DETERMINANT returns the determinant of the ONE matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    20 February 2015
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
  if ( n == 1 ):
    value = 1.0
  else:
    value = 0.0

  return value

def one_determinant_test ( ):

#*****************************************************************************80
#
## ONE_DETERMINANT_TEST tests ONE_DETERMINANT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    20 February 2015
#
#  Author:
#
#    John Burkardt
#
  from one import one
  from r8mat_print import r8mat_print
 
  print ''
  print 'ONE_DETERMINANT_TEST'
  print '  ONE_DETERMINANT computes the determinant of the ONE matrix.'
  print ''

  m = 4
  n = m

  a = one ( m, n )
  r8mat_print ( m, n, a, '  ONE matrix:' )

  value = one_determinant ( n )

  print ''
  print '  Value =  %g' % ( value )

  print ''
  print 'ONE_DETERMINANT_TEST'
  print '  Normal end of execution.'

  return

def one_eigen_right ( n ):

#*****************************************************************************80
#
## ONE_EIGEN_RIGHT returns the right eigenvectors of the ONE matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    19 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the order of the matrix.
#
#    Output, real X(N,N), the right eigenvectors.
#
  import numpy as np

  x = np.zeros ( ( n, n ) )
 
  for j in range ( 0, n - 1 ):
    x[  0,j] = +1.0
    x[j+1,j] = -1.0

  for i in range ( 0, n ):
    x[i,n-1] = 1.0

  return x

def one_eigenvalues ( n ):

#*****************************************************************************80
#
## ONE_EIGENVALUES returns the eigenvalues of the ONE matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    19 March 2015
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

  lam[n-1] = float ( n )

  return lam

def one_null_left ( m, n ):

#*****************************************************************************80
#
## ONE_NULL_LEFT returns a left null vector for the ONE matrix.
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
#    Output, real X(M), a left null vector.
#
  import numpy as np

  x = np.zeros ( m )

  x[0] = 1
  x[m-1] = -1

  return x

def one_null_right ( m, n ):

#*****************************************************************************80
#
## ONE_NULL_RIGHT returns a right null vector for the ONE matrix.
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
#    Output, real X(N), a right null vector.
#
  import numpy as np

  x = np.zeros ( n )

  x[0] = 1.0
  x[n-1] = -1.0

  return x

def one_test ( ):

#*****************************************************************************80
#
## ONE_TEST tests ONE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    20 February 2015
#
#  Author:
#
#    John Burkardt
#
  from r8mat_print import r8mat_print

  print ''
  print 'ONE_TEST'
  print '  ONE computes the ONE matrix.'

  m = 4
  n = m

  a = one ( m, n )
  r8mat_print ( m, n, a, '  ONE matrix:' )

  print ''
  print 'ONE_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  one_test ( )
  one_determinant_test ( )
  timestamp ( )
