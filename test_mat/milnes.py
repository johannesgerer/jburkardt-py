#! /usr/bin/env python
#
def milnes ( m, n, x ):

#*****************************************************************************80
#
## MILNES returns the MILNES matrix.
#
#  Formula:
#
#    If ( I <= J )
#      A(I,J) = 1
#    else
#      A(I,J) = X(J)
#
#  Example:
#
#    M = 5, N = 5, X = ( 4, 7, 3, 8 )
#
#    1 1 1 1 1
#    4 1 1 1 1
#    4 7 1 1 1
#    4 7 3 1 1
#    4 7 3 8 1
#
#    M = 3, N = 6, X = ( 5, 7 )
#
#    1 1 1 1 1
#    5 1 1 1 1
#    5 7 1 1 1
#
#    M = 5, N = 3, X = ( 5, 7, 8 )
#
#    1 1 1
#    5 1 1
#    5 7 1
#    5 7 8
#    5 7 8
#
#  Properties:
#
#    A is generally not symmetric: A' /= A.
#
#    det ( A ) = ( 1 - X(1) ) * ( 1 - X(2) ) * ... * ( 1 - X(N-1) ).
#
#    A is singular if and only if X(I) = 1 for any I.
#
#    The family of matrices is nested as a function of N.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    19 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Robert Gregory, David Karney,
#    Example 3.14, Example 5.24,
#    A Collection of Matrices for Testing Computational Algorithms,
#    Wiley, 1969, page 52, page 105,
#    LC: QA263.G68.
#
#  Parameters:
#
#    Input, integer M, N, the number of rows and columns of A.
#
#    Input, real X(*), the lower column values.
#    If M <= N, then X should be dimensioned M-1.
#    If N < M, X should be dimensioned N.
#
#    Output, real A(M,N), the matrix.
#
  import numpy as np

  a = np.zeros ( ( m, n ) )

  for i in range ( 0, m ):
    for j in range ( 0, n ):
      if ( i <= j ):
        a[i,j] = 1.0
      else:
        a[i,j] = x[j]

  return a

def milnes_determinant ( n, x ):

#*****************************************************************************80
#
## MILNES_DETERMINANT computes the determinant of the MILNES matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    19 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the order of the matrix.
#
#    Input, real X(N), the parameter vector.
#
#    Output, real VALUE, the determinant.
#
  value = 1.0

  if ( 1 < n ):
    for i in range ( 0, n - 1 ):
      value = value * ( 1.0 - x[i] )

  return value

def milnes_determinant_test ( ):

#*****************************************************************************80
#
## MILNES_DETERMINANT_TEST tests MILNES_DETERMINANT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    19 February 2015
#
#  Author:
#
#    John Burkardt
#
  from milnes import milnes
  from r8vec_uniform_ab import r8vec_uniform_ab
  from r8mat_print import r8mat_print

  print ''
  print 'MILNES_DETERMINANT_TEST'
  print '  MILNES_DETERMINANT computes the MILNES determinant.'

  m = 5
  n = m
  r8_lo = -5.0
  r8_hi = +5.0
  seed = 123456789
  x, seed = r8vec_uniform_ab ( n, r8_lo, r8_hi, seed )

  a = milnes ( m, n, x )

  r8mat_print ( m, n, a, '  MILNES matrix:' )

  value = milnes_determinant ( n, x )

  print ''
  print '  Value =  %g' % ( value )

  print ''
  print 'MILNES_DETERMINANT_TEST'
  print '  Normal end of execution.'

  return

def milnes_inverse ( n, x ):

#*****************************************************************************80
#
#% MILNES_INVERSE returns the inverse of the MILNES matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Robert Gregory, David Karney,
#    Example 3.24,
#    A Collection of Matrices for Testing Computational Algorithms,
#    Wiley, 1969, page 52, 
#    LC: QA263.G68.
#
#  Parameters:
#
#    Input, integer N, the order of A.
#
#    Input, real X(N-1), the lower column values.
#
#    Output, real A(N,N), the matrix.
#
  import numpy as np

  a = np.zeros ( ( n, n ) )

  for i in range ( 0, n ):
    for j in range ( 0, n ):
      if ( i == j and i != n - 1 ):
        a[i,j] = 1.0 / ( 1.0 - x[i] )
      elif ( j == i + 1 and i != n - 1 ):
        a[i,j] = -1.0 / ( 1.0 - x[i] )
      elif ( i == n - 1 and j != 0 and j != n - 1 ):
        a[i,j] = ( x[j-1] - x[j] ) / ( ( 1.0 - x[j] ) * ( 1.0 - x[j-1] ) )
      elif ( i == n - 1 and j == 0 ):
        a[i,j] = - x[0] / ( 1.0 - x[0] )
      elif ( i == n - 1 and j == n - 1 ):
        a[i,j] = 1.0 / ( 1.0 - x[n-2] )

  return a

def milnes_test ( ):

#*****************************************************************************80
#
## MILNES_TEST tests MILNES.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    18 February 2015
#
#  Author:
#
#    John Burkardt
#
  from r8vec_uniform_ab import r8vec_uniform_ab
  from r8mat_print import r8mat_print

  print ''
  print 'MILNES_TEST'
  print '  MILNES computes the MILNES matrix.'

  m = 5
  n = m
  r8_lo = -5.0
  r8_hi = +5.0
  seed = 123456789
  x, seed = r8vec_uniform_ab ( n, r8_lo, r8_hi, seed )

  a = milnes ( m, n, x )
 
  r8mat_print ( m, n, a, '  MILNES matrix:' )

  print ''
  print 'MILNES_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  milnes_test ( )
  timestamp ( )
