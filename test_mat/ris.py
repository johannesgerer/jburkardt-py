#! /usr/bin/env python
#
def ris ( n ):

#*****************************************************************************80
#
## RIS returns the RIS matrix.
#
#  Discussion:
#
#    This is sometimes called the "dingdong" matrix, invented by F N Ris.
#
#  Formula:
#
#    A(I,J) = 1 / ( 3 + 2 * N - 2 * I - 2 * J )
#
#  Example:
#
#    N = 5
#
#    1/9  1/7  1/5  1/3   1
#    1/7  1/5  1/3   1   -1
#    1/5  1/3   1   -1  -1/3
#    1/3   1   -1  -1/3 -1/5
#     1   -1  -1/3 -1/5 -1/7
#
#  Properties:
#
#    A is a Cauchy matrix.
#
#    A is a Hankel matrix: constant along anti-diagonals.
#
#    A is symmetric: A' = A.
#
#    Because A is symmetric, it is normal.
#
#    Because A is normal, it is diagonalizable.
#
#    The eigenvalues of A cluster around PI/2 and -PI/2.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    23 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    John Nash,
#    Compact Numerical Methods for Computers: Linear Algebra and
#    Function Minimisation,
#    John Wiley, 1979, page 210.
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
      a[i,j] = 1.0 / float ( 2 * n - 2 * i - 2 * j - 1 )

  return a

def ris_determinant ( n ):

#*****************************************************************************80
#
## RIS_DETERMINANT computes the determinant of the RIS matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    23 February 2015
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
  top = 1.0
  for i in range ( 1, n + 1 ):
    for j in range ( i + 1, n + 1 ):
      top = top * float ( 4 * ( i - j ) * ( i - j ) )

  bottom = 1.0
  for i in range ( 1, n + 1 ):
    for j in range ( 1, n + 1 ):
      bottom = bottom * float ( 3 + 2 * n - 2 * i - 2 * j )

  value = top / bottom

  return value

def ris_determinant_test ( ):

#*****************************************************************************80
#
## RIS_DETERMINANT_TEST tests RIS_DETERMINANT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    23 February 2015
#
#  Author:
#
#    John Burkardt
#
  from ris import ris
  from r8mat_print import r8mat_print

  print ''
  print 'RIS_DETERMINANT_TEST'
  print '  RIS_DETERMINANT computes the RIS determinant.'

  m = 5
  n = m
 
  a = ris ( n )

  r8mat_print ( m, n, a, '  RIS matrix:' )

  value = ris_determinant ( n )

  print ''
  print '  Value =  %g' % ( value )

  print ''
  print 'RIS_DETERMINANT_TEST'
  print '  Normal end of execution.'

  return

def ris_inverse ( n ):

#*****************************************************************************80
#
## RIS_INVERSE returns the inverse of the RIS matrix.
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

      top = 1.0
      bot1 = 1.0
      bot2 = 1.0

      for k in range ( 0, n ):

        top = top * float ( 3 + 2 * n - 2 * ( j + 1 ) - 2 * ( k + 1 ) ) \
          * ( 3 + 2 * n - 2 * ( k + 1 ) - 2 * ( i + 1 ) )

        if ( k != j ):
          bot1 = bot1 * float ( 2 * ( k - j ) )

        if ( k != i ):
          bot2 = bot2 * float ( 2 * ( k - i ) )

      a[i,j] = top / ( float ( 3 + 2 * n - 2 * ( j + 1 ) - 2 * ( i + 1 ) ) \
        * bot1 * bot2 );

  return a

def ris_test ( ):

#*****************************************************************************80
#
## RIS_TEST tests RIS.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    23 February 2015
#
#  Author:
#
#    John Burkardt
#
  from r8mat_print import r8mat_print

  print ''
  print 'RIS_TEST'
  print '  RIS computes the RIS matrix.'

  m = 5
  n = m

  a = ris ( n )
 
  r8mat_print ( m, n, a, '  RIS matrix:' )

  print ''
  print 'RIS_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  ris_test ( )
  timestamp ( )
