#! /usr/bin/env python
#
def herndon ( n ):

#*****************************************************************************80
#
## HERNDON returns the HERNDON matrix.
#
#  Formula:
#
#    c = ( n * ( n + 1 ) * ( 2 * n - 5 ) ) / 6
#    a(n,n) = - 1 / c
#    for i = 1 : n - 1
#      a(i,n) = a(n,i) = i / c
#      a(i,i) = ( c - i*i ) / c
#      for j = 1, i - 1
#        a(i,j) = a(j,i) = - i * j / c
#       end
#     end
#
#  Example:
#
#    N = 5
#
#     0.96  -0.08  -0.12  -0.16   0.04
#    -0.08   0.84  -0.24  -0.32   0.08
#    -0.12  -0.24   0.64  -0.48   0.12
#    -0.16  -0.32  -0.48   0.36   0.16
#     0.04   0.08   0.12   0.16  -0.04
#
#  Properties:
#
#    A is symmetric: A' = A.
#
#    Because A is symmetric, it is normal: A' * A = A * A'.
#
#    The eigenvalues of A are:
#
#      1 (multiplicity N-2),
#      6 / ( P * ( N + 1 ),
#      P / ( N * ( 5 - 2 * N ) ),
#
#    where
#
#      P = 3 + sqrt ( ( 4 * N - 3 ) * ( N - 1 ) * 3 / ( N + 1 ) ).
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    12 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    John Herndon,
#    Algorithm 52, A Set of Test Matrices,
#    Communications of the ACM,
#    April, 1961.
#
#  Parameters:
#
#    Input, integer N, the order of A.
#
#    Output, real A(N,N), the matrix.
#
  import numpy as np

  a = np.zeros ( ( n, n ) )

  c = float ( n * ( n + 1 ) * ( 2 * n - 5 ) ) / 6.0

  a[n-1,n-1] = - 1.0 / c

  for i in range ( 0, n - 1 ):

    a[i,n-1] = float ( i + 1 ) / c
    a[n-1,i] = float ( i + 1 ) / c
    a[i,i]   = ( c - float ( ( i + 1 ) * ( i + 1 ) ) ) / c

    for j in range ( 0, i ):

      a[i,j] = - float ( ( i + 1 ) * ( j + 1 ) ) / c
      a[j,i] = - float ( ( i + 1 ) * ( j + 1 ) ) / c

  return a

def herndon_determinant ( n ):

#*****************************************************************************80
#
## HERNDON_DETERMINANT computes the determinant of the HERNDON matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    12 February 2015
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
  value = 6.0 / float ( ( n + 1 ) * n * ( 5 - 2 * n ) )

  return value

def herndon_determinant_test ( ):

#*****************************************************************************80
#
## HERNDON_DETERMINANT_TEST tests HERNDON_DETERMINANT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    12 February 2015
#
#  Author:
#
#    John Burkardt
#
  from herndon import herndon
  from r8mat_print import r8mat_print

  print ''
  print 'HERNDON_DETERMINANT_TEST'
  print '  HERNDON_DETERMINANT computes the HERNDON determinant.'

  m = 5
  n = m
 
  a = herndon ( n )

  r8mat_print ( m, n, a, '  HERNDON matrix:' )

  value = herndon_determinant ( n )

  print ''
  print '  Value =  %g' % ( value )

  print ''
  print 'HERNDON_DETERMINANT_TEST'
  print '  Normal end of execution.'

  return

def herndon_inverse ( n ):

#*****************************************************************************80
#
## HERNDON_INVERSE returns the inverse of the Herndon matrix.
#
#  Formula:
#
#    if ( I == N )
#      A(I,J) = J
#    else if ( J == N )
#      A(I,J) = I
#    else if ( I == J )
#      A(I,J) = 1
#    else
#      A(I,J) = 0
#
#  Example:
#
#    N = 5
#
#    1  0  0  0  1
#    0  1  0  0  2
#    0  0  1  0  3
#    0  0  0  1  4
#    1  2  3  4  5
#
#  Properties:
#
#    A is symmetric.
#
#    A is border-banded.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    John Herndon,
#    Algorithm 52, A Set of Test Matrices,
#    Communications of the ACM,
#    April, 1961.
#
#  Parameters:
#
#    Input, integer N, the order of A.
#
#    Output, real A(N,N), the matrix.
#
  import numpy as np

  a = np.zeros ( ( n, n ) )

  for i in range ( 0, n - 1 ):
    a[i,i] = 1.0

  for i in range ( 0, n - 1 ):
    a[i,n-1] = float ( i + 1 )

  for j in range ( 0, n - 1 ):
    a[n-1,j] = float ( j + 1 )

  a[n-1,n-1] = float ( n )

  return a

def herndon_test ( ):

#*****************************************************************************80
#
## HERNDON_TEST tests HERNDON.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    12 February 2015
#
#  Author:
#
#    John Burkardt
#
  from r8mat_print import r8mat_print

  print ''
  print 'HERNDON_TEST'
  print '  HERNDON computes the HERNDON matrix.'

  m = 5
  n = m

  a = herndon ( n )
 
  r8mat_print ( m, n, a, '  HERNDON matrix:' )

  print ''
  print 'HERNDON_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  herndon_test ( )
  timestamp ( )
