#! /usr/bin/env python
#
def lietzke ( n ):

#*****************************************************************************80
#
## LIETZKE returns the LIETZKE matrix.
#
#  Formula:
#
#    A(I,J) = N - abs ( I - J )
#
#  Example:
#
#    N = 5
#
#     5  4  3  2  1
#     4  5  4  3  2
#     3  4  5  4  3
#     2  3  4  5  4
#     1  2  3  4  5
#
#  Properties:
#
#    A is integral, therefore det ( A ) is integral, and 
#    det ( A ) * inverse ( A ) is integral.
#
#    A is symmetric: A' = A.
#
#    Because A is symmetric, it is normal.
#
#    Because A is normal, it is diagonalizable.
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
#  Reference:
#
#    M Lietzke, R Stoughton, Marjorie Lietzke,
#    A Comparison of Several Methods for Inverting Large Symmetric
#    Positive Definite Matrices,
#    Mathematics of Computation,
#    Volume 18, Number 87, pages 449-456.
#
#  Parameters:
#
#    Input, integer N, the number of rows and columns 
#    of the matrix.
#
#    Output, real A(N,N), the matrix.
#
  import numpy as np

  a = np.zeros ( ( n, n ) )

  for i in range ( 0, n ):
    for j in range ( 0, n ):
      a[i,j] = float ( n - abs ( i - j ) )

  return a

def lietzke_condition ( n ):

#*****************************************************************************80
#
## LIETZKE_CONDITION returns the L1 condition of the LIETZKE matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 April 2015
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
  s = 0
  k = n
  for i in range ( 0, n ):
    s = s + k
    if ( ( i % 2 ) == 0 ):
      k = k - 1
  a_norm = float ( s )
  if ( n == 1 ):
    b_norm = 0.25
  elif ( n == 2 ):
    b_norm = 5.0 / 6.0
  else:
    b_norm = 2.0

  value = a_norm * b_norm
    
  return value

def lietzke_determinant ( n ):

#*****************************************************************************80
#
## LIETZKE_DETERMINANT computes the determinant of the LIETZKE matrix.
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
#  Parameters:
#
#    Input, integer N, the order of the matrix.
#
#    Output, real VALUE, the determinant.
#
  value = float ( n + 1 ) * 2.0 ** ( n - 2 )

  return value

def lietzke_determinant_test ( ):

#*****************************************************************************80
#
## LIETZKE_DETERMINANT_TEST tests LIETZKE_DETERMINANT.
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
  from lietzke import lietzke
  from r8mat_print import r8mat_print

  print ''
  print 'LIETZKE_DETERMINANT_TEST'
  print '  LIETZKE_DETERMINANT computes the LIETZKE determinant.'

  m = 5
  n = m
 
  a = lietzke ( n )

  r8mat_print ( m, n, a, '  LIETZKE matrix:' )

  value = lietzke_determinant ( n )

  print ''
  print '  Value =  %g' % ( value )

  print ''
  print 'LIETZKE_DETERMINANT_TEST'
  print '  Normal end of execution.'

  return

def lietzke_inverse ( n ):

#*****************************************************************************80
#
## LIETZKE_INVERSE returns the inverse of the LIETZKE matrix.
#
#  Example:
#
#    N = 5
#
#   0.5833   -0.5000         0         0    0.0833
#  -0.5000    1.0000   -0.5000         0         0
#        0   -0.5000    1.0000   -0.5000         0
#        0         0   -0.5000    1.0000   -0.5000
#   0.0833         0         0   -0.5000    0.5833
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    15 October 2007
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of rows and columns 
#    of the matrix.
#
#    Output, real A(N,N), the matrix.
#
  import numpy as np

  a = np.zeros ( ( n, n ) )

  a[0,0] = float ( n + 2 ) / float ( 2 * n + 2 )
  for i in range ( 1, n - 1 ):
    a[i,i] = 1.0
  a[n-1,n-1] = float ( n + 2 ) / float ( 2 * n + 2 )

  if ( n == 2 ):

    for i in range ( 0, n - 1 ):
      a[i,i+1] = - 1.0 / 3.0

    for i in range ( 1, n ):
      a[i,i-1] = - 1.0 / 3.0

  else:

    for i in range ( 0, n - 1 ):
      a[i,i+1] = - 0.5

    for i in range ( 1, n ):
      a[i,i-1] = - 0.5

  a[0,n-1] = 1.0 / float ( 2 * n + 2 )
  a[n-1,0] = 1.0 / float ( 2 * n + 2 )

  return a

def lietzke_test ( ):

#*****************************************************************************80
#
## LIETZKE_TEST tests LIETZKE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    07 February 2015
#
#  Author:
#
#    John Burkardt
#
  from r8mat_print import r8mat_print

  print ''
  print 'LIETZKE_TEST'
  print '  LIETZKE computes the LIETZKE matrix.'

  m = 5
  n = m

  a = lietzke ( n )
 
  r8mat_print ( m, n, a, '  LIETZKE matrix:' )

  print ''
  print 'LIETZKE_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  lietzke_test ( )
  timestamp ( )
