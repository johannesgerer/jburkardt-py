#! /usr/bin/env python
#
def summation ( m, n ):

#*****************************************************************************80
#
## SUMMATION returns the summation matrix.
#
#  Example:
#
#    M = 5, N = 5
#
#    1  0  0  0  0
#    1  1  0  0  0
#    1  1  1  0  0
#    1  1  1  1  0
#    1  1  1  1  1
#
#  Properties:
#
#    A is generally not symmetric: A' /= A.
#
#    A is lower triangular.
#
#    A is a 0/1 matrix.
#
#    The vector Y = A * X contains the partial sums of the vector X.
#
#    A is Toeplitz: constant along diagonals.
#
#    A is nonsingular.
#
#    det ( A ) = 1.
#
#    A is unimodular.
#
#    LAMBDA(1:N) = 1.
#
#    A is persymmetric: A(I,J) = A(N+1-J,N+1-I).
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    17 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, N, the order of the matrix.
#
#    Output, real A(M,N), the matrix.
#
  import numpy as np

  a = np.zeros ( [ m, n ] )

  for j in range ( 0, n ):
    for i in range ( 0, m ):
      if ( j <= i ):
        a[i,j] = 1.0

  return a

def summation_condition ( n ):

#*****************************************************************************80
#
## SUMMATION_CONDITION returns the L1 condition of the SUMMATION matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    17 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the order of the matrix.
#
#    Output, real COND, the L1 condition.
#
  if ( n == 1 ):
    cond = 1.0
  else:
    cond = 2.0 * float ( n )

  return cond

def summation_condition_test ( ):

#*****************************************************************************80
#
## SUMMATION_CONDITION_TEST tests SUMMATION_CONDITION.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    17 December 2014
#
#  Author:
#
#    John Burkardt
#
  from summation import summation
  from r8mat_print import r8mat_print

  print ''
  print 'SUMMATION_CONDITION_TEST'
  print '  SUMMATION_CONDITION computes the condition of the SUMMATION matrix.'
  print ''

  n = 4
  a = summation ( n, n )
  r8mat_print ( n, n, a, '  SUMMATION matrix:' )

  value = summation_condition ( n )

  print ''
  print '  Value =  %g' % ( value )

  print ''
  print 'SUMMATION_CONDITION_TEST'
  print '  Normal end of execution.'

  return

def summation_determinant ( n ):

#*****************************************************************************80
#
## SUMMATION_DETERMINANT returns the determinant of the SUMMATION matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    24 February 2015
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

def summation_determinant_test ( ):

#*****************************************************************************80
#
## SUMMATION_DETERMINANT_TEST tests SUMMATION_DETERMINANT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    24 February 2015
#
#  Author:
#
#    John Burkardt
#
  from summation import summation
  from r8mat_print import r8mat_print

  print ''
  print 'SUMMATION_DETERMINANT_TEST'
  print '  SUMMATION_DETERMINANT computes the determinant of the SUMMATION matrix.'
  print ''

  n = 4
  a = summation ( n, n )
  r8mat_print ( n, n, a, '  SUMMATION matrix:' )

  value = summation_determinant ( n )

  print ''
  print '  Value =  %g' % ( value )

  print ''
  print 'SUMMATION_DETERMINANT_TEST'
  print '  Normal end of execution.'

  return

def summation_inverse ( n ):

#*****************************************************************************80
#
## SUMMATION_INVERSE returns the inverse of the summation matrix.
#
#  Example:
#
#    N = 5
#
#    1  0  0  0  0
#   -1  1  0  0  0
#    0 -1  1  0  0
#    0  0 -1  1  0
#    0  0  0 -1  1
#
#  Properties:
#
#    A is lower triangular.
#
#    A is lower bidiagonal.
#
#    Because A is bidiagonal, it has property A (bipartite).
#
#    A is Toeplitz: constant along diagonals.
#
#    A is nonsingular.
#
#    det ( A ) = 1.
#
#    A is unimodular.
#
#    LAMBDA(1:N) = 1.
#
#    A is persymmetric: A(I,J) = A(N+1-J,N+1-I).
#
#    A is the inverse of the summation matrix.
#
#    The family of matrices is nested as a function of N.
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
#    Input, integer N, the order of the matrix.
#
#    Output, real A(N,N), the matrix.
#
  import numpy as np

  a = np.zeros ( ( n, n ) )

  for i in range ( 0, n ):
    for j in range ( 0, n ):
      if ( i == j ):
        a[i,j] = 1.0
      elif ( i == j + 1 ):
        a[i,j] = -1.0

  return a

def summation_test ( ):

#*****************************************************************************80
#
## SUMMATION_TEST tests SUMMATION.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    17 December 2014
#
#  Author:
#
#    John Burkardt
#
  from r8mat_print import r8mat_print

  print ''
  print 'SUMMATION_TEST'
  print '  SUMMATION computes the SUMMATION matrix.'

  m = 5
  n = 4
  a = summation ( m, n )
  r8mat_print ( m, n, a, '  SUMMATION matrix:' )

  print ''
  print 'SUMMATION_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  summation_test ( )
  timestamp ( )
