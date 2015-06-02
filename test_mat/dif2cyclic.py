#! /usr/bin/env python
#
def dif2cyclic ( n ):

#*****************************************************************************80
#
## DIF2CYCLIC returns the cyclic second difference matrix.
#
#  Example:
#
#    N = 5
#
#    2 -1  .  . -1
#   -1  2 -1  .  .
#    . -1  2 -1  .
#    .  . -1  2 -1
#   -1  .  . -1  2
#
#  Square Properties:
#
#    A is symmetric: A' = A.
#
#    Because A is symmetric, it is normal.
#
#    Because A is normal, it is diagonalizable.
#
#    A is persymmetric: A(I,J) = A(N+1-J,N+1-I).
#
#    A is centrosymmetric: A(I,J) = A(N+1-I,N+1-J).
#
#    A is a circulant: each row is shifted once to get the next row.
#
#    A is (weakly) row diagonally dominant.
#
#    A is (weakly) column diagonally dominant.
#
#    A is singular.
#
#    det ( A ) = 0.
#
#    (1,1,...,1) is a null vector of A.
#
#    A is cyclic tridiagonal.
#
#    A is Toeplitz: constant along diagonals.
#
#    A has constant row sum = 0.
#
#    A has constant column sum = 0.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the order of A.
#
#    Output, real A(N,N), the matrix.
#
  import numpy as np
  from i4_wrap import i4_wrap

  a = np.zeros ( [ n, n ] )

  for i in range ( 0, n ):

    im1 = i4_wrap ( i - 1, 0, n - 1 )
    a[i,im1] = -1.0

    a[i,i] = 2.0

    ip1 = i4_wrap ( i + 1, 0, n - 1 )
    a[i,ip1] = -1.0

  return a

def dif2cyclic_determinant ( n ):

#*****************************************************************************80
#
## DIF2CYCLIC_DETERMINANT computes the determinant of the DIF2CYCLIC matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    19 January 2015
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

def dif2cyclic_determinant_test ( ):

#*****************************************************************************80
#
## DIF2CYCLIC_DETERMINANT_TEST tests DIF2CYCLIC_DETERMINANT.
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
  from dif2cyclic import dif2cyclic
  from r8mat_print import r8mat_print

  print ''
  print 'DIF2CYCLIC_DETERMINANT_TEST'
  print '  DIF2CYCLIC_DETERMINANT computes the DIF2CYCLIC determinant.'

  m = 5
  n = m
 
  a = dif2cyclic ( n )

  r8mat_print ( m, n, a, '  DIF2 matrix:' )

  value = dif2cyclic_determinant ( n )

  print '  Value =  %g' % ( value )

  print ''
  print 'DIF2CYCLIC_DETERMINANT_TEST'
  print '  Normal end of execution.'

  return

def dif2cyclic_null_left ( m, n ):

#*****************************************************************************80
#
## DIF2CYCLIC_NULL_LEFT returns a left null vector for the DIF2CYCLIC matrix.
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
#    Output, real X(M), a right null vector.
#
  import numpy as np

  x = np.ones ( m )

  return x

def dif2cyclic_null_right ( m, n ):

#*****************************************************************************80
#
## DIF2CYCLIC_NULL_RIGHT returns a right null vector for the DIF2CYCLIC matrix.
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

  x = np.ones ( n )

  return x

def dif2cyclic_test ( ):

#*****************************************************************************80
#
## DIF2CYCLIC_TEST tests DIF2CYCLIC.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    19 January 2015
#
#  Author:
#
#    John Burkardt
#
  from r8mat_print import r8mat_print

  print ''
  print 'DIF2CYCLIC_TEST'
  print '  DIF2CYCLIC computes the DIF2CYCLIC matrix.'

  m = 5
  n = m

  a = dif2cyclic ( n )
 
  r8mat_print ( m, n, a, '  DIF2CYCLIC matrix:' )

  print ''
  print 'DIF2CYCLIC_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  dif2cyclic_test ( )
  dif2cyclic_determinant_test ( )
  timestamp ( )
