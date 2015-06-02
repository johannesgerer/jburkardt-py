#! /usr/bin/env python
#
def lotkin ( m, n ):

#*****************************************************************************80
#
## LOTKIN returns the LOTKIN matrix.
#
#  Formula:
#
#    if ( I = 1 )
#      A(I,J) = 1
#    else
#      A(I,J) = 1 / ( I + J - 1 )
#
#  Example:
#
#    N = 5
#
#     1   1   1   1   1
#    1/2 1/3 1/4 1/5 1/6
#    1/3 1/4 1/5 1/6 1/7
#    1/4 1/5 1/6 1/7 1/8
#    1/5 1/6 1/7 1/8 1/9
#
#  Properties:
#
#    A is the Hilbert matrix with the first row set to all 1's.
#
#    A is generally not symmetric: A' /= A.
#
#    A is ill-conditioned.
#
#    A has many negative eigenvalues of small magnitude.
#
#    The inverse of A has all integer elements, and is known explicitly.
#
#    For N = 6, the eigenvalues are:
#       2.132376,
#      -0.2214068,
#      -0.3184330 D-1,
#      -0.8983233 D-3,
#      -0.1706278 D-4,
#      -0.1394499 D-6.
#
#    det ( A(N) ) = ( -1 )^(N-1) / DELTA(N)
#
#    where
#
#      DELTA(N) = COMB ( 2*N-2, N-2 ) * COMB ( 2*N-2, N-1 )
#        * ( 2*N-1) * DELTA(N-1),
#      DELTA(1) = 1.
#
#    The family of matrices is nested as a function of N.
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
#    Robert Gregory, David Karney,
#    Example 3.9,
#    A Collection of Matrices for Testing Computational Algorithms,
#    Wiley, 1969, page 38,
#    LC: QA263.G68.
#
#    Max Lotkin,
#    A set of test matrices,
#    Mathematics Tables and Other Aids to Computation,
#    Volume 9, 1955, pages 153-161.
#
#    Joan Westlake,
#    A Handbook of Numerical Matrix Inversion and Solution of 
#    Linear Equations,
#    John Wiley, 1968,
#    ISBN13: 978-0471936756,
#    LC: QA263.W47.
#
#  Parameters:
#
#    Input, integer M, N, the number of rows and columns of A.
#
#    Output, real A(M,N), the matrix.
#
  import numpy as np

  a = np.zeros ( ( n, n ) )

  for i in range ( 0, m ):
    for j in range ( 0, n ):

      if ( i == 0 ):
        a[i,j] = 1.0
      else:
        a[i,j] = 1.0 / float ( i + j + 1 )

  return a

def lotkin_determinant ( n ):

#*****************************************************************************80
#
## LOTKIN_DETERMINANT returns the determinant of the LOTKIN matrix.
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
  from r8_choose import r8_choose

  delta = 1.0

  for i in range ( 2, n + 1 ):
    delta = - r8_choose ( 2 * i - 2, i - 2 ) * r8_choose ( 2 * i - 2, i - 1 ) \
      * float ( 2 * i - 1 ) * delta

  value = 1.0 / delta

  return value

def lotkin_determinant_test ( ):

#*****************************************************************************80
#
## LOTKIN_DETERMINANT_TEST tests LOTKIN_DETERMINANT.
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
  from lotkin import lotkin
  from r8mat_print import r8mat_print
 
  print ''
  print 'LOTKIN_DETERMINANT_TEST'
  print '  LOTKIN_DETERMINANT computes the determinant of the LOTKIN matrix.'
  print ''

  m = 4
  n = m

  a = lotkin ( m, n )
  r8mat_print ( m, n, a, '  LOTKIN matrix:' )

  value = lotkin_determinant ( n )

  print ''
  print '  Value =  %g' % ( value )

  print ''
  print 'LOTKIN_DETERMINANT_TEST'
  print '  Normal end of execution.'

  return

def lotkin_inverse ( n ):

#*****************************************************************************80
#
## LOTKIN_INVERSE returns the inverse of the LOTKIN matrix.
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
  from r8_choose import r8_choose
  from r8_mop import r8_mop

  a = np.zeros ( ( n, n ) )

  for i in range ( 0, n ):
    for j in range ( 0, n ):

      if ( j == 0 ):

        a[i,j] = r8_mop ( n - i - 1 ) \
          * r8_choose ( n + i, i ) \
          * r8_choose ( n, i + 1 )

      else:

        a[i,j] = r8_mop ( i - j + 1 ) * float ( i + 1 ) \
          * r8_choose ( i + j + 1, j ) \
          * r8_choose ( i + j, j - 1 ) \
          * r8_choose ( n + i, i + j + 1 ) \
          * r8_choose ( n + j, i + j + 1 )

  return a

def lotkin_test ( ):

#*****************************************************************************80
#
## LOTKIN_TEST tests LOTKIN.
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
  from r8mat_print import r8mat_print

  print ''
  print 'LOTKIN_TEST'
  print '  LOTKIN computes the LOTKIN matrix.'

  m = 4
  n = m

  a = lotkin ( m, n )
  r8mat_print ( m, n, a, '  LOTKIN matrix:' )

  print ''
  print 'LOTKIN_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  lotkin_test ( )
  timestamp ( )
