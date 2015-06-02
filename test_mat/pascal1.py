#! /usr/bin/env python
#
def pascal1 ( n ):

#*****************************************************************************80
#
## PASCAL1 returns the PASCAL1 matrix.
#
#  Formula:
#
#    if ( J = 1 )
#      A(I,J) = 1
#    elseif ( I = 0 )
#      A(1,J) = 0
#    else
#      A(I,J) = A(I-1,J) + A(I-1,J-1)
#
#  Example:
#
#    N = 5
#
#    1  0  0  0  0
#    1  1  0  0  0
#    1  2  1  0  0
#    1  3  3  1  0
#    1  4  6  4  1
#
#  Properties:
#
#    A is a "chunk" of the Pascal binomial combinatorial triangle.
#
#    A is generally not symmetric: A' /= A.
#
#    A is nonsingular.
#
#    A is lower triangular.
#
#    A is integral, therefore det ( A ) is integral, and 
#    det ( A ) * inverse ( A ) is integral.
#
#    det ( A ) = 1.
#
#    A is unimodular.
#
#    LAMBDA(1:N) = 1.
#
#    (0, 0, ..., 0, 1) is an eigenvector.
#
#    The inverse of A is the same as A, except that entries in "odd"
#    positions have changed sign:
#
#      B(I,J) = (-1)^(I+J) * A(I,J)
#
#    The product A*A' is a Pascal matrix
#    of the sort created by subroutine PASCAL2.
#
#    Let the matrix C have the same entries as A, except that
#    the even columns are negated.  Then Inverse(C) = C, and
#    C' * C = the Pascal matrix created by PASCAL2.
#
#    The family of matrices is nested as a function of N.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Robert Gregory, David Karney,
#    Example 3.15,
#    A Collection of Matrices for Testing Computational Algorithms,
#    Wiley, 1969, page 43, 
#    LC: QA263.G68.
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

      if ( j == 0 ):
        a[i,j] = 1.0
      elif ( i == 0 ):
        a[i,j] = 0.0
      else:
        a[i,j] = a[i-1,j-1] + a[i-1,j]

  return a

def pascal1_condition ( n ):

#*****************************************************************************80
#
## PASCAL1_CONDITION returns the L1 condition of the PASCAL1 matrix.
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
#    Input, integer N, the order of the matrix.
#
#    Output, real VALUE, the L1 condition.
#
  from r8_choose import r8_choose

  nhalf = ( ( n + 1 ) // 2 )
  a_norm = r8_choose ( n, nhalf )
  b_norm = r8_choose ( n, nhalf )
  value = a_norm * b_norm

  return value

def pascal1_determinant ( n ):

#*****************************************************************************80
#
## PASCAL1_DETERMINANT computes the determinant of the PASCAL1 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 February 2015
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

def pascal1_determinant_test ( ):

#*****************************************************************************80
#
## PASCAL1_DETERMINANT_TEST tests PASCAL1_DETERMINANT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 February 2015
#
#  Author:
#
#    John Burkardt
#
  from pascal1 import pascal1
  from r8mat_print import r8mat_print

  print ''
  print 'PASCAL1_DETERMINANT_TEST'
  print '  PASCAL1_DETERMINANT computes the PASCAL1 determinant.'

  m = 5
  n = m
 
  a = pascal1 ( n )

  r8mat_print ( m, n, a, '  PASCAL1 matrix:' )

  value = pascal1_determinant ( n )

  print '  Value =  %g' % ( value )

  print ''
  print 'PASCAL1_DETERMINANT_TEST'
  print '  Normal end of execution.'

  return

def pascal1_inverse ( n ):

#*****************************************************************************80
#
## PASCAL1_INVERSE returns the inverse of the PASCAL1 matrix.
#
#  Formula:
#
#    if ( J = 1 )
#      A(I,J) = (-1)^(I+J)
#    elseif ( I = 1 )
#      A(I,J) = 0
#    else
#      A(I,J) = A(I-1,J) - A(I,J-1)
#
#  Example:
#
#    N = 5
#
#     1  0  0  0  0
#    -1  1  0  0  0
#     1 -2  1  0  0
#    -1  3 -3  1  0
#     1 -4  6 -4  1
#
#  Properties:
#
#    A is nonsingular.
#
#    A is lower triangular.
#
#    A is integral, therefore det ( A ) is integral, and 
#    det ( A ) * inverse ( A ) is integral.
#
#    det ( A ) = 1.
#
#    A is unimodular.
#
#    LAMBDA(1:N) = 1.
#
#    (0, 0, ..., 0, 1) is an eigenvector.
#
#    The inverse of A is the same as A, except that entries in "odd"
#    positions have changed sign:
#
#      B(I,J) = (-1)^(I+J) * A(I,J)
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    18 March 2015
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
  from r8_mop import r8_mop

  a = np.zeros ( ( n, n ) )

  for i in range ( 0, n ):
    for j in range ( 0, n ):

      if ( j == 0 ):
        a[i,j] = r8_mop ( i + j )
      elif ( 0 < i ):
        a[i,j] = a[i-1,j-1] - a[i-1,j]

  return a

def pascal1_test ( ):

#*****************************************************************************80
#
## PASCAL1_TEST tests PASCAL1.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 February 2015
#
#  Author:
#
#    John Burkardt
#
  from r8mat_print import r8mat_print

  print ''
  print 'PASCAL1_TEST'
  print '  PASCAL1 computes the PASCAL1 matrix.'

  m = 5
  n = m

  a = pascal1 ( n )
 
  r8mat_print ( m, n, a, '  PASCAL1 matrix:' )

  print ''
  print 'PASCAL1_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  pascal1_test ( )
  timestamp ( )
