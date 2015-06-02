#! /usr/bin/env python
#
def tri_upper ( alpha, n ):

#*****************************************************************************80
#
## TRI_UPPER returns the TRI_UPPER matrix.
#
#  Discussion:
#
#    This matrix is known as the Wilkinson upper triangular matrix.
#
#  Formula:
#
#    if ( I = J )
#      A(I,J) = 1
#    if ( I < J )
#      A(I,J) = ALPHA
#    else
#      A(I,J) = 0
#
#  Example:
#
#    ALPHA = 3, N = 5
#
#    1 3 3 3 3
#    0 1 3 3 3
#    0 0 1 3 3
#    0 0 0 1 3
#    0 0 0 0 1
#
#  Properties:
#
#    A is generally not symmetric: A' /= A.
#
#    A is nonsingular.
#
#    A is upper triangular.
#
#    det ( A ) = 1.
#
#    A is unimodular.
#
#    LAMBDA(1:N) = 1.
#
#    A is Toeplitz: constant along diagonals.
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
#    17 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real ALPHA, value used on the superdiagonals.
#
#    Input, integer N, the order of A.
#
#    Output, real A(N,N), the matrix.
#
  import numpy as np

  a = np.zeros ( ( n, n ) )

  for i in range ( 0, n ):
    for j in range ( 0, n ):
      if ( i == j ):
        a[i,j] = 1.0
      elif ( i < j ):
        a[i,j] = alpha
      else:
        a[i,j] = 0.0
 
  return a

def tri_upper_condition ( alpha, n ):

#*****************************************************************************80
#
## TRI_UPPER_CONDITION returns the L1 condition of the TRI_UPPER matrix.
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
#    Input, real ALPHA, value used on the superdiagonals.
#
#    Input, integer N, the order of the matrix.
#
#    Output, real COND, the L1 condition number.
#
  a_norm = ( n - 1 ) * abs ( alpha ) + 1.0

  b_norm = 1.0 + abs ( alpha ) \
    * ( ( abs ( alpha - 1.0 ) ) ** ( n - 1 ) - 1.0 ) \
    / ( abs ( alpha - 1.0 ) - 1.0 )

  cond = a_norm * b_norm

  return cond

def tri_upper_condition_test ( ):

#*****************************************************************************80
#
## TRI_UPPER_CONDITION_TEST tests TRI_UPPER_CONDITION.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 February 2015
#
#  Author:
#
#    John Burkardt
#
  from tri_upper import tri_upper
  from r8_uniform_01 import r8_uniform_01
  from r8mat_print import r8mat_print

  print ''
  print 'TRI_UPPER_CONDITION_TEST'
  print '  TRI_UPPER_CONDITION computes the condition of the TRI_UPPER matrix.'
  print ''

  m = 5
  n = m

  r8_lo = -5.0
  r8_hi = +5.0
  seed = 123456789
  alpha, seed = r8_uniform_ab ( r8_lo, r8_hi, seed )

  a = tri_upper ( alpha, n )
  r8mat_print ( n, n, a, '  TRI_UPPER matrix:' )

  value = tri_upper_condition ( alpha, n )

  print ''
  print '  Value =  %g' % ( value )

  print ''
  print 'TRI_UPPER_CONDITION_TEST'
  print '  Normal end of execution.'

  return

def tri_upper_determinant ( alpha, n ):

#*****************************************************************************80
#
## TRI_UPPER_DETERMINANT returns the determinant of the TRI_UPPER matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real ALPHA, value used on the superdiagonals.
#
#    Input, integer N, the order of the matrix.
#
#    Output, real VALUE, the determinant.
#
  value = 1.0

  return value

def tri_upper_determinant_test ( ):

#*****************************************************************************80
#
## TRI_UPPER_DETERMINANT_TEST tests TRI_UPPER_DETERMINANT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 February 2015
#
#  Author:
#
#    John Burkardt
#
  from tri_upper import tri_upper
  from r8_uniform_ab import r8_uniform_ab
  from r8mat_print import r8mat_print

  print ''
  print 'TRI_UPPER_DETERMINANT_TEST'
  print '  TRI_UPPER_DETERMINANT computes the determinant of the TRI_UPPER matrix.'
  print ''

  m = 5
  n = m

  r8_lo = -5.0
  r8_hi = +5.0
  seed = 123456789
  alpha, seed = r8_uniform_ab ( r8_lo, r8_hi, seed )

  a = tri_upper ( alpha, n )
  r8mat_print ( n, n, a, '  TRI_UPPER matrix:' )

  value = tri_upper_determinant ( alpha, n )

  print ''
  print '  Value =  %g' % ( value )

  print ''
  print 'TRI_UPPER_DETERMINANT_TEST'
  print '  Normal end of execution.'

  return

def tri_upper_inverse ( alpha, n ):

#*****************************************************************************80
#
## TRI_UPPER_INVERSE returns the inverse of the TRI_UPPER matrix.
#
#  Formula:
#
#    if ( I = J )
#      A(I,J) = 1
#    elseif ( I = J - 1 )
#      A(I,J) = -ALPHA
#    elseif ( I < J )
#      A(I,J) = - ALPHA * ( 1-ALPHA)^(J-I-1)
#    else
#      A(I,J) = 0
#
#  Example:
#
#    ALPHA = 3, N = 5
#
#    1 -3  6 -12  24
#    0  1 -3   6 -12
#    0  0  1  -3   6
#    0  0  0   1  -3
#    0  0  0   0   1
#
#  Properties:
#
#    A is generally not symmetric: A' /= A.
#
#    A is nonsingular.
#
#    A is upper triangular.
#
#    A is Toeplitz: constant along diagonals.
#
#    A is persymmetric: A(I,J) = A(N+1-J,N+1-I).
#
#    det ( A ) = 1.
#
#    A is unimodular.
#
#    LAMBDA(1:N) = 1.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 October 2007
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real ALPHA, value used on the superdiagonals.
#
#    Input, integer N, the order of A.
#
#    Output, real A(N,N), the matrix.
#
  import numpy as np

  a = np.zeros ( ( n, n ) )

  for i in range ( 0, n ):
    for j in range ( 0, n ):

      if ( i == j ):
        a[i,j] = 1.0
      elif ( i == j - 1 ):
        a[i,j] = - alpha
      elif ( i < j ):
        a[i,j] = - alpha * ( 1.0 - alpha ) ** ( j - i - 1 )

  return a

def tri_upper_test ( ):

#*****************************************************************************80
#
## TRI_UPPER_TEST tests TRI_UPPER.
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
  from r8_uniform_01 import r8_uniform_01
  from r8mat_print import r8mat_print

  print ''
  print 'TRI_UPPER_TEST'
  print '  TRI_UPPER computes the TRI_UPPER matrix.'

  seed = 123456789

  n = 5
  alpha, seed = r8_uniform_01 ( seed )
  a = tri_upper ( alpha, n )
  r8mat_print ( n, n, a, '  TRI_UPPER matrix:' )

  print ''
  print 'TRI_UPPER_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  tri_upper_test ( )
  timestamp ( )
