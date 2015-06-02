#! /usr/bin/env python
#
def dif1 ( m, n ):

#*****************************************************************************80
#
## DIF1 returns the DIF1 matrix.
#
#  Discussion:
#
#    DIF1 is the first difference matrix.
#
#    For a set of N points X(I) with equal spacing H, and a set of data
#    values Y(I) associated with those points, the product 
#    1/(2*H) * A * Y returns an approximation to the first derivative
#    of Y(X) at the interior points X(2:N-1).
#
#  Example:
#
#    N = 5
#
#    0 +1  .  .  .
#   -1  0 +1  .  .
#    . -1  0 +1  .
#    .  . -1  0 +1
#    .  .  . -1  0
#
#  Rectangular Properties:
#
#    A is banded, with bandwidth 3.
#
#    A is tridiagonal.
#
#    Because A is tridiagonal, it has property A (bipartite).
#
#    A is integral: int ( A ) = A.
#
#    A is Toeplitz: constant along diagonals.
#
#  Square Properties:
#
#    A is antisymmetric: A' = -A.
#
#    Because A is antisymmetric, it is normal.
#
#    Because A is normal, it is diagonalizable.
#
#    If N is even, then A is nonsingular.
#    If N is odd, then A is singular.
#
#    If N is even, det ( A ) = 1.0.
#    If N is odd, det ( A ) = 0.0.
#
#    If N is odd, a null vector is ( 1, 0, 1, 0, ..., 1, 0, 1 )..
#
#    The family of matrices is nested as a function of N.
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
#    Input, integer M, N, the number of rows and columns of A.
#
#    Output, real A(M,N), the matrix.
#
  import numpy as np

  a = np.zeros ( [ m, n ] )

  for i in range ( 0, m ):
      
    if ( 0 <= i - 1 ):
      a[i,i-1] = -1.0

    if ( i + 1 <= n - 1 ):
      a[i,i+1] = +1.0

  return a

def dif1_determinant ( n ):

#*****************************************************************************80
#
## DIF1_DETERMINANT computes the determinant of the DIF1 matrix.
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
#    Output, real DETERM, the determinant.
#
  if ( ( n % 2 ) == 0 ):
    determ = 1.0
  else:
    determ = 0.0

  return determ

def dif1_determinant_test ( ):

#*****************************************************************************80
#
## DIF1_DETERMINANT_TEST tests DIF1_DETERMINANT.
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
  from dif1 import dif1
  from r8mat_print import r8mat_print

  print ''
  print 'DIF1_DETERMINANT_TEST'
  print '  DIF1_DETERMINANT computes the DIF1 determinant.'

  m = 5
  n = m
 
  a = dif1 ( m, n )

  r8mat_print ( m, n, a, '  DIF1 matrix:' )

  value = dif1_determinant ( n )

  print '  Value =  %g' % ( value )

  print ''
  print 'DIF1_DETERMINANT_TEST'
  print '  Normal end of execution.'

  return

def dif1_inverse ( n ):

#*****************************************************************************80
#
## DIF1_INVERSE returns the inverse of the DIF1 matrix.
#
#  Discussion:
#
#    The inverse only exists when N is even.
#
#  Example:
#
#    N = 8
#
#    0 -1  0 -1  0 -1  0 -1
#    1  0  0  0  0  0  0  0
#    0  0  0 -1  0 -1  0 -1
#    1  0  1  0  0  0  0  0
#    0  0  0  0  0 -1  0 -1
#    1  0  1  0  1  0  0  0
#    0  0  0  0  0  0  0 -1
#    1  0  1  0  1  0  1  0
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 March 2015
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
  from sys import exit

  if ( ( n % 2 ) != 0 ):
    print ''
    print 'DIF1_INVERSE - Fatal error!'
    print '  Inverse only exists for N even.'
    exit ( 'DIF1_INVERSE - Fatal error!' )

  a = np.zeros ( ( n, n ) )

  for i in range ( 0, n - 1, 2 ):
    for j in range ( i + 1, n, 2 ):
      a[i,j] = -1.0

  for i in range ( 1, n, 2 ):
    for j in range ( 0, i, 2 ):
      a[i,j] = 1.0

  return a

def dif1_null_left ( m, n ):

#*****************************************************************************80
#
## DIF1_NULL_LEFT returns a left null vector for the DIF1 matrix.
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
  from sys import exit

  x = np.zeros ( m )

  if ( ( m % 2 ) == 0 ):
    print ''
    print 'DIF1_NULL_LEFT - Fatal error!'
    print '  The matrix is not singular for even M.'
    exit ( 'DIF1_NULL_LEFT - Fatal error!' )

  for i in range ( 0, m, 2 ):
    x[i] = 1.0

  return x

def dif1_null_right ( m, n ):

#*****************************************************************************80
#
## DIF1_NULL_RIGHT returns a right null vector for the DIF1 matrix.
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
  from sys import exit

  x = np.zeros ( n )

  if ( ( n % 2 ) == 0 ):
    print ''
    print 'DIF1_NULL_RIGHT - Fatal error!'
    print '  The matrix is not singular for even N.'
    exit ( 'DIF1_NULL_RIGHT - Fatal error!' )

  for i in range ( 0, n, 2 ):
    x[i] = 1.0

  return x

def dif1_test ( ):

#*****************************************************************************80
#
## DIF1_TEST tests DIF1.
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
  from r8mat_print import r8mat_print

  print ''
  print 'DIF1_TEST'
  print '  DIF1 computes the DIF1 matrix.'

  m = 5
  n = m

  a = dif1 ( m, n )
 
  r8mat_print ( m, n, a, '  DIF1 matrix:' )

  print ''
  print 'DIF1_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  dif1_test ( )
  timestamp ( )
