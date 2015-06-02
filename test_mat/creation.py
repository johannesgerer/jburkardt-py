#! /usr/bin/env python
#
def creation ( m, n ):

#*****************************************************************************80
#
## CREATION returns the CREATION matrix.
#
#  Example:
#
#    M = 5, N = 5
#
#    0  0  0  0  0
#    1  0  0  0  0
#    0  2  0  0  0
#    0  0  3  0  0
#    0  0  0  4  0
#
#  Properties:
#
#    A is integral: int ( A ) = A.
#
#    A is strictly lower triangular.
#
#  Square properties:
#
#    A is generally not symmetric: A' /= A.
#
#    A is singular.
#
#    A has the null vector ( 0, 0, ..., 0, 1 ).
#
#    det ( A ) = 0.
#
#    LAMBDA(1:N) = 0
#
#    A is zero except for the first lower diagonal. A^2 is zero except for
#    the second lower diagonal.  A^(N-1) is the last nonzero power of A,
#    with a single nonzero entry in the (N,1) position.
#
#    The family of matrices is nested as a function of N.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, the number of rows of A.
#
#    Input, integer N, the number of columns of A.
#
#    Output, real A(N,N), the matrix.
#
  import numpy as np

  a = np.zeros ( [ m, n ] )

  for j in range ( 0, n ):
    for i in range ( 0, m ):

      if ( i == j + 1 ):
        a[i,j] = j + 1
      else:
        a[i,j] = 0.0

  return a

def creation_determinant ( n ):

#*****************************************************************************80
#
## CREATION_DETERMINANT computes the determinant of the CREATION matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 January 2015
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
  determ = 0.0

  return determ

def creation_determinant_test ( ):

#*****************************************************************************80
#
## CREATION_DETERMINANT_TEST tests CREATION_DETERMINANT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 January 2015
#
#  Author:
#
#    John Burkardt
#
  from r8mat_print import r8mat_print

  print ''
  print 'CREATION_DETERMINANT_TEST'
  print '  CREATION_DETERMINANT computes the CREATION determinant.'

  n = 5
  m = n
  a = creation ( m, n, )
  r8mat_print ( m, n, a, '  CREATION matrix:' )

  value = creation_determinant ( n )

  print '  Value =  %g' % ( value )

  print ''
  print 'CREATION_DETERMINANT_TEST'
  print '  Normal end of execution.'

  return

def creation_null_left ( m, n ):

#*****************************************************************************80
#
## CREATION_NULL_LEFT returns a left null vector for the CREATION matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    15 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, N, the order of the matrix.
#
#    Output, real X(M), the vector.
#
  import numpy as np

  x = np.zeros ( m )
  x[0] = 1.0

  return x

def creation_null_right ( m, n ):

#*****************************************************************************80
#
## CREATION_NULL_RIGHT returns a right null vector for the CREATION matrix.
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
#    Output, real X(N), the vector.
#
  import numpy as np

  x = np.zeros ( n )
  x[n-1] = 1.0

  return x

def creation_test ( ):

#*****************************************************************************80
#
## CREATION_TEST tests CREATION.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 January 2015
#
#  Author:
#
#    John Burkardt
#
  from r8mat_print import r8mat_print

  print ''
  print 'CREATION_TEST'
  print '  CREATION computes the CREATION matrix.'

  m = 5
  n = 4
  a = creation ( m, n )
  r8mat_print ( m, n, a, '  CREATION matrix:' )

  print ''
  print 'CREATION_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  creation_test ( )
  creation_determinant_test ( )
  timestamp ( )
