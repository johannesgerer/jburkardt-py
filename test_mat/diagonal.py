#! /usr/bin/env python
#
def diagonal ( m, n, x ):

#*****************************************************************************80
#
## DIAGONAL returns a DIAGONAL matrix.
#
#  Formula:
#
#    if ( I = J )
#      A(I,J) = X(I)
#    else
#      A(I,J) = 0
#
#  Example:
#
#    M = 5, N = 5, X = ( 1, 2, 3, 4, 5 )
#
#    1 0 0 0 0
#    0 2 0 0 0
#    0 0 3 0 0
#    0 0 0 4 0
#    0 0 0 0 5
#
#  Square Properties:
#
#    A is banded, with bandwidth 1.
#
#    A is nonsingular if, and only if, each X(I) is nonzero.
#
#    The inverse of A is a diagonal matrix with diagonal values 1/X(I).
#
#    A is symmetric: A' = A.
#
#    Because A is symmetric, it is normal.
#
#    Because A is normal, it is diagonalizable.
#
#    LAMBDA(1:N) = X(1:N).
#
#    The matrix of eigenvectors of A is the identity matrix.
#
#    det ( A ) = product ( 1 <= I <= N ) X(I).
#
#    Because A is diagonal, it has property A (bipartite).
#
#    The family of matrices is nested as a function of N.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    17 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, N, the number of rows and columns of A.
#
#    Input, real X(min(M,N)), the diagonal entries of A.
#
#    Output, real A(M,N), the matrix.
#
  import numpy as np

  a = np.zeros ( [ m, n ] )

  for j in range ( 0, n ):
    for i in range ( 0, m ):
      if ( i == j ):
        a[i,j] = x[i]

  return a

def diagonal_condition ( n, x ):

#*****************************************************************************80
#
## DIAGONAL_CONDITION computes the L1 condition of the DIAGONAL matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    18 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the order of the matrix.
#
#    Input, real X(N), the diagonal elements.
#
#    Output, real COND, the L1 condition.
#
  import numpy as np

  cond = np.max ( np.abs ( x ) ) / np.min ( np.abs ( x ) )

  return cond

def diagonal_condition_test ( ):

#*****************************************************************************80
#
## DIAGONAL_CONDITION_TEST tests DIAGONAL_CONDITION.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    18 January 2015
#
#  Author:
#
#    John Burkardt
#
  from diagonal import diagonal
  from r8vec_uniform_ab import r8vec_uniform_ab
  from r8mat_print import r8mat_print

  print ''
  print 'DIAGONAL_CONDITION_TEST'
  print '  DIAGONAL_CONDITION computes the DIAGONAL condition.'

  m = 5
  n = m
  x_lo = -5.0
  x_hi = +10.0
  seed = 123456789
  x, seed = r8vec_uniform_ab ( n, x_lo, x_hi, seed )

  a = diagonal ( m, n, x )

  r8mat_print ( m, n, a, '  DIAGONAL matrix:' )

  value = diagonal_condition ( n, x )

  print '  Value =  %g' % ( value )

  print ''
  print 'DIAGONAL_CONDITION_TEST'
  print '  Normal end of execution.'

  return

def diagonal_determinant ( n, x ):

#*****************************************************************************80
#
## DIAGONAL_DETERMINANT computes the determinant of the DIAGONAL matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    17 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the order of the matrix.
#
#    Input, real X(N-1), the diagonal elements.
#
#    Output, real VALUE, the determinant.
#
  value = 1.0
  for i in range ( 0, n ):
    value = value * x[i]

  return value

def diagonal_determinant_test ( ):

#*****************************************************************************80
#
## DIAGONAL_DETERMINANT_TEST tests DIAGONAL_DETERMINANT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    17 January 2015
#
#  Author:
#
#    John Burkardt
#
  from diagonal import diagonal
  from r8vec_uniform_ab import r8vec_uniform_ab
  from r8mat_print import r8mat_print

  print ''
  print 'DIAGONAL_DETERMINANT_TEST'
  print '  DIAGONAL_DETERMINANT computes the DIAGONAL determinant.'

  m = 5
  n = m
  r8_lo = -5.0
  r8_hi = +5.0
  seed = 123456789
  x, seed = r8vec_uniform_ab ( n, r8_lo, r8_hi, seed )

  a = diagonal ( m, n, x )

  r8mat_print ( m, n, a, '  DIAGONAL matrix:' )

  value = diagonal_determinant ( n, x )

  print '  Value =  %g' % ( value )

  print ''
  print 'DIAGONAL_DETERMINANT_TEST'
  print '  Normal end of execution.'

  return

def diagonal_eigen_left ( n, d ):

#*****************************************************************************80
#
## DIAGONAL_EIGEN_LEFT returns left eigenvectors of the DIAGONAL matrix.
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
#    Input, real D(N), the diagonal entries.
#
#    Output, real A(N,N), the matrix.
#
  import numpy as np

  a = np.zeros ( ( n, n ) )

  for i in range ( 0, n ):
    a[i,i] = 1.0

  return a

def diagonal_eigen_right ( n, d ):

#*****************************************************************************80
#
## DIAGONAL_EIGEN_RIGHT returns right eigenvectors of the DIAGONAL matrix.
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
#    Input, real D(N), the diagonal entries.
#
#    Output, real A(N,N), the matrix.
#
  import numpy as np

  a = np.zeros ( ( n, n ) )

  for i in range ( 0, n ):
    a[i,i] = 1.0

  return a

def diagonal_eigenvalues ( n, x ):

#*****************************************************************************80
#
## DIAGONAL_EIGENVALUES returns the eigenvalues of the DIAGONAL matrix.
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
#    Input, integer N, the order of A.
#
#    Input, real X(N), the diagonal entries.
#
#    Output, real LAM(N), the eigenvalues.
#
  import numpy as np

  lam = np.copy ( x )

  return lam

def diagonal_inverse ( n, x ):

#*****************************************************************************80
#
## DIAGONAL_INVERSE returns the inverse of the DIAGONAL matrix.
#
#  Discussion:
#
#    The diagonal entries must be nonzero.
#
#  Example:
#
#    M = 5, N = 5, X = ( 1, 2, 3, 4, 5 )
#
#    1  0   0   0   0
#    0 1/2  0   0   0
#    0  0  1/3  0   0
#    0  0   0  1/4  0
#    0  0   0   0  1/5
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
#    Input, integer N , the number of rows and columns 
#    of the matrix.
#
#    Input, real X(N), the diagonal entries of the matrix.
#
#    Output, real A(N,N), the inverse of the matrix.
#
  import numpy as np

  a = np.zeros ( ( n, n ) )

  for i in range ( 0, n ):
    a[i,i] = 1.0 / x[i]

  return a

def diagonal_test ( ):

#*****************************************************************************80
#
## DIAGONAL_TEST tests DIAGONAL.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    17 January 2015
#
#  Author:
#
#    John Burkardt
#
  from r8vec_uniform_ab import r8vec_uniform_ab
  from r8mat_print import r8mat_print

  print ''
  print 'DIAGONAL_TEST'
  print '  DIAGONAL computes the DIAGONAL matrix.'

  m = 5
  n = m
  r8_lo = -5.0
  r8_hi = +5.0
  seed = 123456789
  x, seed = r8vec_uniform_ab ( n, r8_lo, r8_hi, seed )

  a = diagonal ( m, n, x )
 
  r8mat_print ( m, n, a, '  DIAGONAL matrix:' )

  print ''
  print 'DIAGONAL_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  diagonal_test ( )
  timestamp ( )
